#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <util/atomic.h>
#include <stdio.h>

#define F_CPU 16000000UL
#define BAUD 9600
#define UBRR_VALUE ((F_CPU) / 16 / (BAUD) - 1)

#define LED PB5
#define BTN PB4
#define LED_DDR DDRB
#define LED_PORT PORTB
#define BTN_PIN PINB
#define BTN_PORT PORTB

#define UNIT_MS 200
#define DOT_TIME UNIT_MS
#define DASH_TIME (3*UNIT_MS)
#define CHAR_GAP (3*UNIT_MS)
#define WORD_GAP (7*UNIT_MS)

#define CTC_MATCH ((F_CPU / 1000) / 64)

static int uart_transmit(char data, FILE *stream) {
    while (!(UCSR0A & _BV(UDRE0)));
    UDR0 = data;
    return 0;
}

static int uart_receive(FILE *stream) {
    while (!(UCSR0A & _BV(RXC0)));
    return UDR0;
}

static FILE uart_file;

static void uart_init(void) {
    UBRR0 = UBRR_VALUE;
    UCSR0A = 0;
    UCSR0B = _BV(RXEN0) | _BV(TXEN0);
    UCSR0C = _BV(UCSZ00) | _BV(UCSZ01);
    fdev_setup_stream(&uart_file, uart_transmit, uart_receive, _FDEV_SETUP_RW);
    stdin = stdout = stderr = &uart_file;
}

volatile unsigned long long timer_millis = 0;

ISR(TIMER1_COMPA_vect) {
    timer_millis++;
}

static void timer_init_ms(void) {
    TCCR1B = (1 << WGM12) | (1 << CS11) | (1 << CS10);
    OCR1A = (uint16_t)(CTC_MATCH - 1);
    TIMSK1 = (1 << OCIE1A);
}

static unsigned long long millis(void) {
    unsigned long long m;
    ATOMIC_BLOCK(ATOMIC_FORCEON) { m = timer_millis; }
    return m;
}

static const uint8_t morse_letters[26] = {
    0b01000001,0b10001000,0b10001010,0b01100100,0b00100000,0b10000010,
    0b01100110,0b10000000,0b01000000,0b10000111,0b01100101,0b10000100,
    0b01000011,0b01000010,0b01100111,0b10000110,0b10001101,0b01100010,
    0b01100000,0b00100001,0b01100001,0b10000001,0b01100011,0b10001001,
    0b10001011,0b10001100
};

static const uint8_t morse_digits[10] = {
    0b10101111,0b10100111,0b10100011,0b10100001,0b10100000,
    0b10110000,0b10111000,0b10111100,0b10111110,0b10111111
};

static char decode_morse(int pattern, int len) {
    if (len <= 0 || len > 5) return '?';
    uint8_t code = (len << 5) | (pattern & 0b11111);
    for (int i = 0; i < 26; i++) {
        if (morse_letters[i] == code) return 'A' + i;
    }
    for (int i = 0; i < 9; i++) {
        if (morse_digits[i] == code) return '1' + i;
    }
    if (morse_digits[9] == code) return '0';
    return '?';
}

int main(void) {
    BTN_PORT |= _BV(BTN);
    LED_DDR |= _BV(LED);

    uart_init();
    timer_init_ms();
    printf("Morse decoder started\r\n");

    unsigned long last_event = millis();
    int last_btn = (BTN_PIN & _BV(BTN)) ? 1 : 0;

    int pattern = 0;
    int length = 0;
    int word_gap_done = 1;

    while (1) {
        int btn = (BTN_PIN & _BV(BTN)) ? 1 : 0;
        unsigned long now = millis();

        if (!btn && last_btn) {
            LED_PORT |= _BV(LED);
            last_event = now;
            word_gap_done = 0;
            _delay_ms(10);
        }
        if (btn && !last_btn) {
            LED_PORT &= ~_BV(LED);
            unsigned long dur = now - last_event;
            pattern = (pattern << 1) | (dur > DOT_TIME);
            length++;
            last_event = now;
            _delay_ms(10);
        }

        if (btn) {
            unsigned long gap = now - last_event;
            if (length > 0 && gap >= CHAR_GAP) {
                printf("%c ", decode_morse(pattern, length));
                pattern = 0;
                length = 0;
                last_event = now;
                word_gap_done = 0;
            } else if (!word_gap_done && pattern == 0 && gap >= WORD_GAP) {
                printf("\r\n");
                word_gap_done = 1;
                last_event = now;
            }
        }

        last_btn = btn;
    }
}
