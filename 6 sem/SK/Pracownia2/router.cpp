// Karol Burczyk, 340614
#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <cstring>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <unistd.h>
#include <thread>
#include <chrono>
#include <csignal>
#include <atomic>

constexpr int PORT = 54321;
constexpr int ROUND_TIME = 15;
constexpr int MAX_TIMEOUT = 3;

std::atomic<bool> running(true);

void signal_handler(int sig) {
    running = false;
}

// ======== Struktury danych ========
struct Interface {
    std::string cidr;
    in_addr ip;
    in_addr netmask;
    in_addr broadcast;
    uint32_t distance;
    int sockfd;
};

struct RouteInfo {
    uint32_t distance;
    in_addr via;
    bool directly_connected;
    int timeout;
};

using RoutingTable = std::unordered_map<std::string, RouteInfo>;

// ======== Pomocnicze funkcje IP ========
in_addr make_netmask(uint8_t prefix_len) {
    in_addr mask;
    uint32_t mask_val = htonl(~((1 << (32 - prefix_len)) - 1));
    mask.s_addr = mask_val;
    return mask;
}

in_addr compute_broadcast(in_addr ip, in_addr mask) {
    in_addr bcast;
    bcast.s_addr = ip.s_addr | ~mask.s_addr;
    return bcast;
}

std::string addr_to_str(const in_addr& addr) {
    char buf[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &addr, buf, sizeof(buf));
    return std::string(buf);
}

// ======== Parsowanie wejścia ========
std::vector<Interface> load_interfaces_from_stdin() {
    int n;
    std::cin >> n;
    std::vector<Interface> interfaces;

    for (int i = 0; i < n; ++i) {
        std::string cidr, discard;
        uint32_t dist;
        std::cin >> cidr >> discard >> dist;

        size_t slash = cidr.find('/');
        std::string ip_str = cidr.substr(0, slash);
        uint8_t prefix_len = std::stoi(cidr.substr(slash + 1));

        in_addr ip;
        inet_pton(AF_INET, ip_str.c_str(), &ip);
        in_addr netmask = make_netmask(prefix_len);
        in_addr bcast = compute_broadcast(ip, netmask);

        interfaces.push_back({cidr, ip, netmask, bcast, dist, -1});
    }

    return interfaces;
}

// ======== Routing table ========
void init_routing_table(RoutingTable& table, const std::vector<Interface>& interfaces) {
    for (const auto& iface : interfaces) {
        table[iface.cidr] = {iface.distance, iface.ip, true, 0};
    }
}

void update_routing_timeouts(RoutingTable& table) {
    for (auto& [net, info] : table) {
        if (!info.directly_connected) {
            info.timeout++;
            if (info.timeout > MAX_TIMEOUT) {
                info.distance = UINT32_MAX;
            }
        }
    }
}

void print_routing_table(const RoutingTable& table) {
    for (const auto& [net, info] : table) {
        std::cout << net << " distance ";
        if (info.distance == UINT32_MAX)
            std::cout << "unreachable";
        else
            std::cout << info.distance;

        if (info.directly_connected)
            std::cout << " connected directly\n";
        else
            std::cout << " via " << addr_to_str(info.via) << "\n";
    }
}

// ======== UDP ========
void setup_sockets(std::vector<Interface>& interfaces) {
    for (auto& iface : interfaces) {
        iface.sockfd = socket(AF_INET, SOCK_DGRAM, 0);
        int yes = 1;
        setsockopt(iface.sockfd, SOL_SOCKET, SO_BROADCAST, &yes, sizeof(yes));

        sockaddr_in addr{};
        addr.sin_family = AF_INET;
        addr.sin_addr = iface.ip;
        addr.sin_port = htons(PORT);
        bind(iface.sockfd, (sockaddr*)&addr, sizeof(addr));
    }
}

void send_updates(const std::vector<Interface>& interfaces, const RoutingTable& table) {
    for (const auto& iface : interfaces) {
        for (const auto& [net, info] : table) {
            in_addr net_ip;
            uint8_t prefix_len = std::stoi(net.substr(net.find('/') + 1));
            std::string net_str = net.substr(0, net.find('/'));
            inet_pton(AF_INET, net_str.c_str(), &net_ip);

            uint8_t packet[9];
            memcpy(packet, &net_ip.s_addr, 4);
            packet[4] = prefix_len;
            uint32_t dist = htonl(info.distance);
            memcpy(packet + 5, &dist, 4);

            sockaddr_in dest{};
            dest.sin_family = AF_INET;
            dest.sin_port = htons(PORT);
            dest.sin_addr = iface.broadcast;

            sendto(iface.sockfd, packet, 9, 0, (sockaddr*)&dest, sizeof(dest));
        }
    }
}

void receive_loop(std::vector<Interface>& interfaces, RoutingTable& table) {
    fd_set fds;
    char buffer[9];

    while (running) {
        FD_ZERO(&fds);
        int max_fd = -1;
        for (const auto& iface : interfaces) {
            FD_SET(iface.sockfd, &fds);
            if (iface.sockfd > max_fd) max_fd = iface.sockfd;
        }

        timeval tv{1, 0};
        int ready = select(max_fd + 1, &fds, nullptr, nullptr, &tv);
        if (ready < 0) continue;

        for (auto& iface : interfaces) {
            if (FD_ISSET(iface.sockfd, &fds)) {
                sockaddr_in sender{};
                socklen_t len = sizeof(sender);
                int r = recvfrom(iface.sockfd, buffer, 9, 0, (sockaddr*)&sender, &len);
                if (r != 9) continue;

                in_addr net_ip;
                uint8_t prefix;
                uint32_t dist;

                memcpy(&net_ip.s_addr, buffer, 4);
                prefix = buffer[4];
                memcpy(&dist, buffer + 5, 4);
                dist = ntohl(dist);

                std::string net_cidr = addr_to_str(net_ip) + "/" + std::to_string(prefix);
                uint32_t new_dist = (dist == UINT32_MAX) ? UINT32_MAX : dist + iface.distance;

                auto it = table.find(net_cidr);
                if (it == table.end() || new_dist < it->second.distance) {
                    table[net_cidr] = {new_dist, sender.sin_addr, false, 0};
                } else if (it->second.via.s_addr == sender.sin_addr.s_addr) {
                    it->second.distance = new_dist;
                    it->second.timeout = 0;
                }
            }
        }
    }
}

// ======== Main ========
int main() {
    signal(SIGINT, signal_handler);
    signal(SIGTERM, signal_handler);

    auto interfaces = load_interfaces_from_stdin();
    setup_sockets(interfaces);

    RoutingTable table;
    init_routing_table(table, interfaces);

    std::thread recv_thread(receive_loop, std::ref(interfaces), std::ref(table));

    while (running) {
        std::this_thread::sleep_for(std::chrono::seconds(ROUND_TIME));
        update_routing_timeouts(table);
        send_updates(interfaces, table);
        print_routing_table(table);
    }

    recv_thread.join();
    return 0;
}
