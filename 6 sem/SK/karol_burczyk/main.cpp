#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <chrono>
#include <iomanip>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/ip_icmp.h>
#include <netinet/in.h>
#include <unistd.h>
#include <poll.h>
#include <algorithm>
#include <stdexcept>

using namespace std;

class ICMPTraceroute {
private:
    int MAX_TTL = 30;
    int TIMEOUT = 1000;
    int sockfd;
    string destination;
    sockaddr_in recipient{};

    // metoda do tworzenia gniazda
    void initialize_socket() {
        sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
        if (sockfd < 0) {
            throw runtime_error("Blad otwierania gniazda");
        }
    }

    // metoda konfigurujaca odbiorce
    void setup_recipient(const string& ip) {
        recipient.sin_family = AF_INET;
        if (inet_pton(AF_INET, ip.c_str(), &recipient.sin_addr) != 1) {
            throw invalid_argument("Bledny adres IP");
        }
    }

    // metoda do liczenia sumy kontrolnej
    static uint16_t compute_checksum(void* buff, int length) {
        uint16_t* ptr = static_cast<uint16_t*>(buff);
        uint32_t sum = 0;
        for (; length > 1; length -= 2)
            sum += *ptr++;
        if (length == 1) {
            sum += *reinterpret_cast<uint8_t*>(ptr);
        }
        sum = (sum >> 16U) + (sum & 0xffffU);
        return ~(sum + (sum >> 16U));
    }

    // metoda do wysyłania pakietów icmp
    bool send_icmp_packet(int ttl, int seq) {
        icmp header{};
        header.icmp_type = ICMP_ECHO;
        header.icmp_code = 0;
        header.icmp_hun.ih_idseq.icd_id = getpid() & 0xFFFF;
        header.icmp_hun.ih_idseq.icd_seq = seq;
        header.icmp_cksum = compute_checksum(&header, sizeof(header));

        if (setsockopt(sockfd, IPPROTO_IP, IP_TTL, &ttl, sizeof(ttl)) < 0) {
            cerr << "Blad ustawiania TTL" << endl;
            return false;
        }

        ssize_t sent = sendto(
                                sockfd, 
                                &header, 
                                sizeof(header), 
                                0, 
                                (struct sockaddr*)&recipient, 
                                sizeof(recipient)
                            );
        if (sent < 0) {
            cerr << "Blad wysylania pakietu" << endl;
            return false;
        }
        return true;
    }

    //metoda do odbierania odpowiedzi
    vector<string> receive_icmp_response(double& rtt) {
        vector<string> ips;
        char buffer[1024];
        sockaddr_in sender{};
        socklen_t sender_len = sizeof(sender);
        pollfd pfd = {sockfd, POLLIN, 0};
        auto start_time = chrono::high_resolution_clock::now();

        int poll_result = poll(&pfd, 1, TIMEOUT);
        if (poll_result > 0) {
            ssize_t bytes_received = recvfrom(sockfd, buffer, sizeof(buffer), 0, reinterpret_cast<sockaddr*>(&sender), &sender_len);
            if (bytes_received > 0) {
                char ip[INET_ADDRSTRLEN];
                inet_ntop(AF_INET, &sender.sin_addr, ip, sizeof(ip));
                ips.emplace_back(ip);
            }
        } else if (poll_result < 0) {
            cerr << "Blad poll()" << endl;
        }

        auto end_time = chrono::high_resolution_clock::now();
        rtt = ips.empty() ? -1.0 : chrono::duration<double, milli>(end_time - start_time).count();
        return ips;
    }

    // metoda do przetwarzania odpowiedzi dla kolejnego ttl
    void process_ttl(int ttl) {
        cout << ttl << ". ";
        vector<string> unique_ips;
        double total_rtt = 0.0;
        int successful_pings = 0;
        
        for (int i = 0; i < 3; i++) {
            if (!send_icmp_packet(ttl, ttl * 3 + i)) continue;
            double rtt = 0.0;
            auto responses = receive_icmp_response(rtt);
            unique_ips.insert(unique_ips.end(), responses.begin(), responses.end());
            if (rtt >= 0) {
                total_rtt += rtt;
                successful_pings++;
            }
        }

        if (unique_ips.empty()) {
            cout << "*" << endl;
        } else {
            unique_ips.erase(unique(unique_ips.begin(), unique_ips.end()), unique_ips.end());
            for (const auto& ip : unique_ips) cout << ip << " ";
            cout << fixed << setprecision(2) << (successful_pings ? total_rtt / successful_pings : -1.00) << "ms" << endl;
        }

        if (!unique_ips.empty() && find(unique_ips.begin(), unique_ips.end(), destination) != unique_ips.end()) {
            throw runtime_error("Koniec dzialania programu");
        }
    }

public:
    // konstruktor klasy ICMPTraceroute
    explicit ICMPTraceroute(const string& ip) : destination(ip) {
        initialize_socket();
        setup_recipient(ip);
    }

    // destruktor
    ~ICMPTraceroute() {
        close(sockfd);
    }

    // metoda do wywołania pełnego traceroute
    void execute() {
        try {
            for (int ttl = 1; ttl <= MAX_TTL; ttl++) {
                process_ttl(ttl);
            }
        } catch (const runtime_error&) {}
    }
};

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Niepoprawna skladnia" << endl;
    }
    try {
        ICMPTraceroute tracer(argv[1]);
        tracer.execute();
    } catch (const exception& e) {
        cerr << "Blad: " << e.what() << endl;
        return 1;
    }
    return 0;
}
