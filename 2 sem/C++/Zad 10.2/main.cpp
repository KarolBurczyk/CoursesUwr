#include <iostream>
#include <stdexcept>
#include "Wejscie.hpp"
#include "Wyjscie.hpp"

using namespace std;

int main()
{
    string filename = "test.bin";

    {
        Wyjscie out(filename);
        out.write(42);
        out.write(123);
        out.write(85);
    }

    {
        Wejscie in1(filename);

        int a, b, c;

        in1.read(a);
        in1.read(b);
        in1.read(c);

        cout << a << endl;
        cout << b << endl;
        cout << c << endl;
    }

    {
        Wejscie in2(filename);

        char byte;
        while (!in2.eof())
        {
            in2.read(byte);
            cout << "Int: " << static_cast<int>(byte);
            cout << " Hex: "  << hex << static_cast<int>(byte);
            cout << " Char: '" << static_cast<char>(byte) << "'" << endl;
        }
    }
}

