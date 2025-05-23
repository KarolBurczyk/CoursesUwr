#include <iostream>
#include <cmath>
#include <functional>

using namespace std;

double wylicz(double x, double a, int precyzja) {
    if (abs(x*x - a) <= pow(10, precyzja)) {
        return x;
    }
    else {
        cout<<x<<endl;
        return wylicz((x + a/x)/2, a, precyzja);
    }
}

double pierwiastek(double m, int c, int precyzja) {
    if (abs(c) % 2 == 0) {
        return pow(2, c/2) * wylicz(m, m, precyzja);
    }
    else {
        return pow(2, (c - 1)/2) * wylicz(m, m, precyzja) * wylicz(2, 2, precyzja);
    }
}

void pierwiastek() {
    double m = 0.5;
    int c = 2;
    int precyzja = -8;
    cout<<pierwiastek(m, c, precyzja);
}

void eksperyment() {
//    cout << wylicz(-1, -1, -8) << endl;
    cout << wylicz(-10, -10, -8) << endl;
}

int main() {
    pierwiastek();
//    eksperyment();
}