#include <avr/io.h>
#include <avr/interrupt.h>

#define LED PB5
#define LED_DDR DDRB
#define LED_PORT PORTB

#define BTN PB4
#define BTN_PIN PINB
#define BTN_PORT PORTB

#define BUFFER_SIZE 16
#define TIME_OFFSET 1000UL
#define CTC_MATCH_OVERFLOW ((F_CPU / 1000) / 64)

typedef struct {
    uint8_t btn_state;
    unsigned long timestamp;
} State;

volatile unsigned long timer_millis = 0;

ISR(TIMER1_COMPA_vect) {
    timer_millis++;
}

void timer_init(void) {
    cli();
    TCCR1B = (1 << WGM12) | (1 << CS11) | (1 << CS10);
    OCR1A = CTC_MATCH_OVERFLOW - 1;
    TIMSK1 = (1 << OCIE1A);
    sei();
}

int main(void) {
    BTN_PORT |= (1 << BTN);
    LED_DDR |= (1 << LED);
    timer_init();

    State buffer[BUFFER_SIZE];
    int buffer_begin = 0;
    int buffer_end = 0;

    uint8_t last_state = (BTN_PIN & (1 << BTN)) ? 1 : 0;

    while (1) {
        uint8_t curr_state = (BTN_PIN & (1 << BTN)) ? 1 : 0;

        if (curr_state != last_state) {
            last_state = curr_state;

            unsigned long play_time = timer_millis + TIME_OFFSET;

            int next_end = (buffer_end + 1) % BUFFER_SIZE;
            if (next_end == buffer_begin) {
                buffer_begin = (buffer_begin + 1) % BUFFER_SIZE;
            }

            buffer[buffer_end].btn_state = curr_state;
            buffer[buffer_end].timestamp = play_time;
            buffer_end = next_end;
        }

        if (buffer_begin != buffer_end) {
            if (timer_millis >= buffer[buffer_begin].timestamp) {
                if (buffer[buffer_begin].btn_state)
                    LED_PORT &= ~(1 << LED);
                else
                    LED_PORT |= (1 << LED);

                buffer_begin = (buffer_begin + 1) % BUFFER_SIZE;
            }
        }
    }
}
