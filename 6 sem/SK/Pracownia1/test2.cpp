#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/ip_icmp.h>
#include <netinet/in.h>
#include <sys/time.h>
#include <fcntl.h>
#include <errno.h>
#include <poll.h>

#define MAX_TTL 30
#define TIMEOUT 1000
#define PACKETS_PER_TTL 3

// Funkcja obliczająca sumę kontrolną
unsigned short checksum(void *b, int len) {
    unsigned short *buf = b;
    unsigned int sum = 0;
    unsigned short result;
    for (sum = 0; len > 1; len -= 2)
        sum += *buf++;
    if (len == 1)
        sum += *(unsigned char *)buf;
    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    result = ~sum;
    return result;
}

// Główna funkcja programu
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <destination_ip>\n", argv[0]);
        return EXIT_FAILURE;
    }

    struct sockaddr_in dest_addr;
    memset(&dest_addr, 0, sizeof(dest_addr));
    dest_addr.sin_family = AF_INET;
    if (inet_pton(AF_INET, argv[1], &dest_addr.sin_addr) != 1) {
        fprintf(stderr, "Invalid IP address.\n");
        return EXIT_FAILURE;
    }

    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock < 0) {
        perror("socket");
        return EXIT_FAILURE;
    }

    struct timeval timeout = {1, 0};
    setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout));

    printf("Tracing route to %s\n", argv[1]);
    
    for (int ttl = 1; ttl <= MAX_TTL; ttl++) {
        setsockopt(sock, IPPROTO_IP, IP_TTL, &ttl, sizeof(ttl));
        struct sockaddr_in recv_addr;
        socklen_t recv_len = sizeof(recv_addr);
        struct icmp packet;
        memset(&packet, 0, sizeof(packet));
        packet.icmp_type = ICMP_ECHO;
        packet.icmp_code = 0;
        packet.icmp_id = getpid();
        
        for (int i = 0; i < PACKETS_PER_TTL; i++) {
            packet.icmp_seq = ttl + i;
            packet.icmp_cksum = 0;
            packet.icmp_cksum = checksum(&packet, sizeof(packet));
        
            if (sendto(sock, &packet, sizeof(packet), 0, (struct sockaddr*)&dest_addr, sizeof(dest_addr)) < 0) {
                perror("sendto");
            }
        }
        

        struct pollfd fds;
        fds.fd = sock;
        fds.events = POLLIN;
        int ret = poll(&fds, 1, TIMEOUT);
        if (ret > 0) {
            char recv_buf[512];
            if (recvfrom(sock, recv_buf, sizeof(recv_buf), 0, (struct sockaddr*)&recv_addr, &recv_len) > 0) {
                gettimeofday(&end, NULL);
                long time_diff = (end.tv_sec - start.tv_sec) * 1000 + (end.tv_usec - start.tv_usec) / 1000;
                printf("%d. %s %ldms\n", ttl, inet_ntoa(recv_addr.sin_addr), time_diff);
                if (recv_addr.sin_addr.s_addr == dest_addr.sin_addr.s_addr)
                    break;
            } else {
                printf("%d. *\n", ttl);
            }
        } else {
            printf("%d. ???\n", ttl);
        }
    }
    close(sock);
    return EXIT_SUCCESS;
}
