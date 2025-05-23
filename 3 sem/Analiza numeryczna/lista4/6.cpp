#include <iostream>
#include <cmath>
#include <functional>

using namespace std;

double wylicz(double x, double a, int precyzja) {
    if (abs(x*x - 1/a) <= pow(10, precyzja)) {
        return x;
    }
    else {
        cout<<x<<endl;
        return wylicz((a*x*x + 1)/(2*a*x), a, precyzja);
    }
}

void pierwiastek() {
    double a = 0.25; // czyli 1/4 zatem a to 4
    int precyzja = -8;
    cout<<wylicz(4, 4, precyzja);
}

void eksperyment() {
//    cout << wylicz(-10, -10, -8) << endl;
    cout << wylicz(0, 0, -8) << endl;
}

int main() {
    pierwiastek();
//    eksperyment();
}