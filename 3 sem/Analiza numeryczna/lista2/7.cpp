#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    return 4046/(sqrt(pow(x, 14) + 1) + 1);
}

int main() {
    cout<<f(1)<<endl;
    cout<<f(0.1)<<endl;
    cout<<f(0.01)<<endl;
    cout<<f(0.001)<<endl;
    cout<<f(0.0001)<<endl;
}
