//#include <iostream>
//#include <cmath>
//#include <functional>
//
//using namespace std;
//
//double f(double x) {
//    return pow(x, 4) - log(x + 4);
//}
//
//double wylicz(double a, double b, double p) {
//    double x0 = (a + b) / 2;
//    double fx = f(x0);
//    double fa = f(a);
//
//    int i = 0;
//    while(abs(fx) >= p) {
//        i++;
//        if(fa * fx < 0) {
//            b = x0;
//        }
//        else {
//            a = x0;
//            fa = fx;
//        }
//        x0 = (a + b) / 2;
//        fx = f(x0);
//        //cout << "fx : " << abs(fx) << " x: " << x0 << " a: " << a << " b: " << b << endl;
//    }
//    cout << i << endl;
//    return x0;
//}
//
//int main() {
//    cout << "X1: " << wylicz(-2, -1, pow(10, -8)) << endl;
//    cout << "X2: " << wylicz(1, 2, pow(10, -8));
//}