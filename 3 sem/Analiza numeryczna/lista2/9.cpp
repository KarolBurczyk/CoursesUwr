//#include <iostream>
//#include <cmath>
//
//using namespace std;
//
//double rek(int k) {
//    if (k == 1) {
//        return 2.0;
//    }
//    else {
//        return pow(2, (k - 1)) * sqrt(2 * (1 - sqrt(1 - pow(rek(k - 1) / pow(2, (k - 1)), 2))));
//    }
//}
//
//double rek_poprawiona(int k) {
//    if (k == 1) {
//        return 2.0;
//    }
//    else {
//        double xk = rek_poprawiona(k -1);
//        return xk * sqrt(2/ (1 + sqrt(1 - pow(xk / pow(2, (k - 1)), 2))));
//    }
//}
//
//int main() {
//    cout<<rek(1000)<<endl;
//    cout<<rek_poprawiona(1000)<<endl;
//}
