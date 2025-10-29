#include <avr/io.h>
#include <inttypes.h>
#include <util/delay.h>

#define STEP_DELAY_MS 100

int main() {
    UCSR0B &= ~_BV(RXEN0) & ~_BV(TXEN0);

    DDRD |= 0xFC;
    DDRB |= 0x0F;

    uint16_t pattern = 0b0000000001;
    uint8_t dir_left = 1;

    while (1) {
        PORTD = (PORTD & ~0xFC) | ((pattern & 0x3F) << 2);
        PORTB = (PORTB & ~0x0F) | ((pattern >> 6) & 0x0F);

        _delay_ms(STEP_DELAY_MS);

        if (dir_left) {
            pattern <<= 1;
        } else {
            pattern >>= 1;
        }

        if (pattern == (1 << 9) || pattern == 1) {
            dir_left = 1 - dir_left;
        }
    }
}
