#include <avr/io.h>
#include <util/delay.h>
#include <string.h>

#define LED PB5
#define LED_DDR DDRB
#define LED_PORT PORTB

#define DOT_DURATION 250
#define DASH_DURATION (DOT_DURATION * 5)
#define SYMBOL_PAUSE DOT_DURATION
#define LETTER_PAUSE (DOT_DURATION)
#define WORD_PAUSE (DOT_DURATION * 7)

const char* morse_table[37][2] = {
    {"A", ".-"}, {"B", "-..."}, {"C", "-.-."}, {"D", "-.."}, {"E", "."},
    {"F", "..-."}, {"G", "--."}, {"H", "...."}, {"I", ".."}, {"J", ".---"},
    {"K", "-.-"}, {"L", ".-.."}, {"M", "--"}, {"N", "-."}, {"O", "---"},
    {"P", ".--."}, {"Q", "--.-"}, {"R", ".-."}, {"S", "..."}, {"T", "-"},
    {"U", "..-"}, {"V", "...-"}, {"W", ".--"}, {"X", "-..-"}, {"Y", "-.--"},
    {"Z", "--.."},
    {"0", "-----"}, {"1", ".----"}, {"2", "..---"}, {"3", "...--"}, {"4", "....-"},
    {"5", "....."}, {"6", "-...."}, {"7", "--..."}, {"8", "---.."}, {"9", "----."},
    {" ", " "}
};

void uart_init() {
    UBRR0H = 0;
    UBRR0L = 103;
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

char uart_receive_char() {
    while (!(UCSR0A & (1 << RXC0))) {}
    return UDR0;
}

void play_dot() {
    LED_PORT |= _BV(LED);
    _delay_ms(DOT_DURATION);
    LED_PORT &= ~_BV(LED);
}

void play_dash() {
    LED_PORT |= _BV(LED);
    _delay_ms(DASH_DURATION);
    LED_PORT &= ~_BV(LED);
}

void play_symbol(char symbol) {
    if (symbol == '.') play_dot();
    else if (symbol == '-') play_dash();
    _delay_ms(SYMBOL_PAUSE);
}

const char* get_morse_code(char c) {
    if (c >= 'a' && c <= 'z') c -= 32;
    for (int i = 0; i < sizeof(morse_table)/sizeof(morse_table[0]); i++) {
        if (morse_table[i][0][0] == c) return morse_table[i][1];
    }
    return NULL;
}

void play_morse(const char* code) {
    for (int i = 0; code[i] != '\0'; i++) {
        if (code[i] == ' ') {
            _delay_ms(WORD_PAUSE);
            return;
        }
        play_symbol(code[i]);
    }
}

int main(void) {
    char buffer[100];
    int idx = 0;
    LED_DDR |= _BV(LED);
    uart_init();

    while (1) {
        char c = uart_receive_char();
        if (c == '\r' || c == '\n') {
            buffer[idx] = '\0';
            idx = 0;

            for (int i = 0; buffer[i] != '\0'; i++) {
                if (buffer[i] == ' ') {
                    _delay_ms(WORD_PAUSE);
                    continue;
                }

                const char* code = get_morse_code(buffer[i]);
                if (code) {
                    play_morse(code);
                    _delay_ms(LETTER_PAUSE);
                }
            }

        } else if (idx < (int)(sizeof(buffer) - 1)) {
            buffer[idx++] = c;
        }
    }
}
