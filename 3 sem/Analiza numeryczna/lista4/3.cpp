//#include <iostream>
//#include <cmath>
//
//using namespace std;
//
//double f(double x) {
//    return x - 0.49;
//}
//
//int main() {
//    double fx, x0;
//    double b = 1, a = 0;
//    double b0 = b, a0 = a;
//    double fa = f(a);
//    int i = 0;
//
//    while(i <= 5) {
//        i++;
//        x0 = (a + b) / 2;
//        fx = f(x0);
//        if(fa * fx < 0) {
//            b = x0;
//        }
//        else {
//            a = x0;
//            fa = fx;
//        }
//        cout<<"x0 : "<<x0<<" |en|: "<<pow(2, -i -1) * (b0 - a0)<<endl;
//    }
//}