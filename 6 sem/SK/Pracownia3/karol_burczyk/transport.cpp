// Karol Burczyk 340614

#include <arpa/inet.h>
#include <cstring>
#include <fcntl.h>
#include <iostream>
#include <poll.h>
#include <stdexcept>
#include <string>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <vector>
#include <map>

using namespace std;

constexpr int MAX_REQUEST_SIZE = 1000;
constexpr int MAX_WINDOW_SIZE = 1000;
constexpr int TIMEOUT_MS = 900;

struct Block {
    size_t start;
    size_t length;
    vector<char> data;
    bool received = false;
    uint64_t last_request_time = 0;
};

uint64_t current_time_ms() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return static_cast<uint64_t>(ts.tv_sec) * 1000 + ts.tv_nsec / 1000000;
}

void send_request(int sockfd, sockaddr_in &server_addr, size_t start, size_t length) {
    char buf[64];
    int len = snprintf(buf, sizeof(buf), "GET %zu %zu\n", start, length);
    if (sendto(sockfd, buf, len, 0, (sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("sendto");
        exit(1);
    }
}

bool parse_data_packet(const char *buffer, ssize_t recv_len, size_t &start, size_t &length, const char *&payload_start) {
    if (recv_len < 10 || strncmp(buffer, "DATA ", 5) != 0)
        return false;

    const char *ptr = buffer + 5;
    start = strtoull(ptr, (char **)&ptr, 10);
    if (*ptr != ' ') return false;
    ++ptr;
    length = strtoull(ptr, (char **)&ptr, 10);
    if (*ptr != '\n') return false;
    ++ptr;

    payload_start = ptr;
    return true;
}

void fill_window(int sockfd, sockaddr_in &server_addr, map<size_t, Block> &blocks, size_t &next_block_start, size_t total_size, uint64_t now) {
    while (next_block_start < total_size && blocks.size() < MAX_WINDOW_SIZE) {
        size_t block_len = min<size_t>(MAX_REQUEST_SIZE, total_size - next_block_start);
        Block blk{next_block_start, block_len, vector<char>(), false, now};
        send_request(sockfd, server_addr, blk.start, blk.length);
        blocks[blk.start] = blk;
        next_block_start += block_len;
    }
}

void resend_timeouted_requests(int sockfd, sockaddr_in &server_addr, map<size_t, Block> &blocks, uint64_t now) {
    for (auto &[start, blk] : blocks) {
        if (!blk.received && now - blk.last_request_time > TIMEOUT_MS) {
            send_request(sockfd, server_addr, blk.start, blk.length);
            blk.last_request_time = now;
        }
    }
}

void handle_received_packet(int fd, map<size_t, Block> &blocks, const char *buffer, ssize_t recv_len, size_t &bytes_written, size_t &next_block_start, size_t total_size, int sockfd, sockaddr_in &server_addr) {
    size_t start, length;
    const char *payload;
    if (!parse_data_packet(buffer, recv_len, start, length, payload))
        return;

    auto it = blocks.find(start);
    if (it == blocks.end() || length != it->second.length)
        return;

    it->second.data.assign(payload, payload + (recv_len - (payload - buffer)));
    it->second.received = true;

    while (!blocks.empty() && blocks.begin()->second.received) {
        Block &b = blocks.begin()->second;
        if ((size_t)write(fd, b.data.data(), b.length) != b.length) {
            perror("write");
            exit(1);
        }
        bytes_written += b.length;
        blocks.erase(blocks.begin());

        fill_window(sockfd, server_addr, blocks, next_block_start, total_size, current_time_ms());
    }
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        cerr << "Użycie: " << argv[0] << " <IP> <port> <nazwa pliku> <rozmiar>\n";
        return 1;
    }

    const char *ip = argv[1];
    string filename = argv[3];
    uint16_t port;
    size_t total_size;

    try {
        size_t pos;
        int p = stoi(argv[2], &pos);
        if (pos != strlen(argv[2]) || p <= 0 || p > 65535) {
            throw invalid_argument("invalid port");
        }
        port = static_cast<uint16_t>(p);
    } catch (...) {
        cerr << "Niepoprawny adres portu";
        return 1;
    }

    try {
        size_t pos;
        total_size = stoull(argv[4], &pos);
        if (pos != strlen(argv[4]) || total_size == 0) {
            throw invalid_argument("invalid size");
        }
    } catch (...) {
        cerr << "Niepoprawny rozmiar pliku do pobrania";
        return 1;
    }

    sockaddr_in server_addr{};
    if (inet_pton(AF_INET, ip, &server_addr.sin_addr) != 1) {
        cerr << "Niepoprawny adres IP";
        return 1;
    }
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);

    int sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    int fd = open(filename.c_str(), O_WRONLY | O_CREAT | O_TRUNC, 0666);
    if (fd < 0) {
        perror("open");
        return 1;
    }

    map<size_t, Block> blocks;
    size_t next_block_start = 0;
    uint64_t now = current_time_ms();
    fill_window(sockfd, server_addr, blocks, next_block_start, total_size, now);

    struct pollfd pfd{sockfd, POLLIN, 0};
    size_t bytes_written = 0;

    while (!blocks.empty()) {
        int ret = poll(&pfd, 1, TIMEOUT_MS);
        now = current_time_ms();

        if (ret > 0 && (pfd.revents & POLLIN)) {
            char buffer[1500];
            sockaddr_in src_addr{};
            socklen_t addrlen = sizeof(src_addr);
            ssize_t recv_len = recvfrom(sockfd, buffer, sizeof(buffer), 0, (sockaddr *)&src_addr, &addrlen);
            if (recv_len < 0) {
                perror("recvfrom");
                return 1;
            }

            if (src_addr.sin_addr.s_addr != server_addr.sin_addr.s_addr || src_addr.sin_port != server_addr.sin_port) {
                continue;
            }

            handle_received_packet(fd, blocks, buffer, recv_len, bytes_written, next_block_start, total_size, sockfd, server_addr);
        }

        resend_timeouted_requests(sockfd, server_addr, blocks, now);
    }

    cout << "Pobrano (" << bytes_written << " baitow).\n";

    close(fd);
    close(sockfd);
    return 0;
}
