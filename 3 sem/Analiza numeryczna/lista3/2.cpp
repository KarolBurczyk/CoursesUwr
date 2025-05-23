//#include <iostream>
//#include <cmath>
//
//using namespace std;
//
//double szkolny_x1(double a, double b, double c) {
//    return (-b + sqrt(pow(b, 2) - 4*a*c))/(2*a);
//}
//
//double szkolny_x2(double a, double b, double c) {
//    return (-b - sqrt(pow(b, 2) - 4*a*c))/(2*a);
//}
//
//double nowy_x1(double a, double b, double c) {
//    if(b >= 0) {
//        return (-b + sqrt(pow(b, 2) - 4*a*c))/(2*a);
//    }
//    else {
//        return (2*c)/(-b - sqrt(pow(b, 2) - 4*a*c));
//    }
//}
//
//double nowy_x2(double a, double b, double c) {
//    if(b < 0) {
//        return (2*c)/(-b + sqrt(pow(b, 2) - 4*a*c));
//    }
//    else {
//        return (-b - sqrt(pow(b, 2) - 4*a*c))/(2*a);
//    }
//}
//
//int main() {
//    for(int i = 0; i < 9; i++) {
//        cout<<"Dla b = -10^"<<i<<": "<<endl;
//        cout<<"Szkolny: "<<szkolny_x1(1, pow(-10, i), 1)<<"   "<<szkolny_x2(1, pow(-10, i), 1)<<endl;
//        cout<<"Nowy: "<<nowy_x1(1, pow(-10, i), 1)<<"   "<<nowy_x2(1, pow(-10, i), 1)<<endl;
//    }
//}