#include <cmath>
#include <iostream>

using namespace std;

void zadanie_1a(double x) {
    cout << 1/(pow(x, 3) + sqrt(pow(x, 6) + pow(2023, 2))) << endl;
}

void zadanie_1a_Poprawione(double x) {
    if(x < 0)
        cout  << (sqrt(pow(x, 6) + (pow(2023, 2))) - pow(x, 3)) / pow(2023, 2) << endl;
    else
        cout << 1/(pow(x, 3) + sqrt(pow(x, 6) + pow(2023, 2))) << endl;
}

void zadanie_1b(double x) {
    cout << log2(x)-2 << endl;
}

void zadanie_1b_Poprawione(double x) {
    cout << log2(x/4) << endl;
}

void zadanie_1c(double x) {
    cout << (M_PI/2 - x - atan(1/x))/pow(x, 3) << endl;
}

void zadanie_1c_Poprawione(double x) {
    double sum = 0;
    if(abs(x) > 1)
        cout << (M_PI/2 - x - atan(1/x))/pow(x, 3) << endl;
    else {
        for(int i = 0; i < 10000; i++) {
            sum += pow(-1, i + 1) * pow(x, 2 * i) / (2 * i + 3);
        }
        cout << sum << endl;
    }
}

int main() {
    cout  << "Zadanie 1A" << endl;
    zadanie_1a(20000.999999999999);
    zadanie_1a_Poprawione(20000.999999999999);
    cout  << "Zadanie 1B" << endl;
    zadanie_1b(3.999999999999);
    zadanie_1b_Poprawione(3.999999999999);
    cout  << "Zadanie 1C" << endl;
    zadanie_1c(-0.0000001);
    zadanie_1c_Poprawione(-0.0000001);
}