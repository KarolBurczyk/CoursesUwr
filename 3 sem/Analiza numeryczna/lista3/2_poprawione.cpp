//#include <cmath>
//#include <iostream>
//
//using namespace std;
//
//void zadanie2przed(double a, double b, double c) {
//    cout << (-b - sqrt(pow(b, 2) - 4*a*c)) / (2*a) << " " << (-b + sqrt(pow(b, 2) - 4*a*c)) / (2*a) << endl;
//}
//
//void zadanie2po(double a, double b, double c) {
//    if(b < 0) {
//        cout << 2*c/(- b + sqrt(pow(b, 2) - 4*a*c)) << " " << (- b + sqrt(pow(b, 2) - 4*a*c)) / (2*a) << endl;
//    }
//    else {
//        cout << (- b - sqrt(pow(b, 2) - 4*a*c)) / (2*a) << " " << 2*c/(- b - sqrt(pow(b, 2) - 4*a*c)) << endl;
//    }
//}
//
//int main() {
//    cout << "Wynik dla x^2 + 10000000x + 1" << endl;
//    zadanie2przed(1, 1000000000, 1);
//    zadanie2po(1, 1000000000, 1);
//    cout << "Wynik dla x^2 - 10000000x + 1" << endl;
//    zadanie2przed(1, -1000000000, 1);
//    zadanie2po(1, -1000000000, 1);
//}