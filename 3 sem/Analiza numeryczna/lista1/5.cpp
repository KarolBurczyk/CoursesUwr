//#include <iostream>
//#include <cmath>
//
//using namespace std;
//
//double f (double n) {
//    if (n == 0) {
//        return log(2024/2023);
//    }
//    else {
//        return 1 / n - 2023 * f(n - 1);
//    }
//}
//
//int main () {
//    cout<<"--- Dla I1 do I20: "<<endl;
//    for(int i = 1; i <= 20; i++) {
//        cout<<"Dla "<<i<<": "<<f(i)<<endl;
//    }
//    cout<<"--- Dla I1, I3, I5,...,I19: "<<endl;
//    for(int i = 1; i <= 19; i = i + 2) {
//        cout<<"Dla "<<i<<": "<<f(i)<<endl;
//    }
//    cout<<"--- Dla I2, I4, I6,...,I20: "<<endl;
//    for(int i = 2; i <= 20; i = i + 2) {
//        cout<<"Dla "<<i<<": "<<f(i)<<endl;
//    }
//}