#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int a, b, s;
    cin>>a;
    cin>>b;
    if (a % 2024 == 0) {
        s = a;
    }
    else {
        s = (a/2024 + 1) * 2024;
    }
    while(s <= b) {
        cout<<s<<" ";
        s += 2024;
    }
}
