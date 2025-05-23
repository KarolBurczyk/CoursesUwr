//#include <iostream>
//#include <cmath>
//
//using namespace std;
//
//double rek(double x) {
//    if (x == 1) {
//        return -1 / 9;
//    }
//    else if (x == 0) {
//        return 1;
//    }
//    else {
//        double tmp = 80 * rek(x - 1) / 9 + rek(x - 2);
//        cout<<"Dla y = "<<x<<" :"<<tmp<<endl;
//        return tmp;
//    }
//}
//
//int main()  {
//    int n = 2;
//    double a = 1.0;
//    double b = (-1.0)/9.0;
//    while(n <= 50) {
//        double c = a;
//        a = b;
//        b = 80.0 * a / 9.0 + c;
//        cout<<"Dla n = "<<n<<": "<<b<<endl;
//        n++;
//    }
//}
