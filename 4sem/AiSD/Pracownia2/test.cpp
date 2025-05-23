#include <iostream>
#include <cmath>
#include <limits>

// pomysł: efektywny algorytm na znalezienie dwóch najbliżej położonych punktów x3

using namespace std;

int main() {
    int n;
    cin>>n;
    int x[n];
    int y[n];
    for(int i = 0; i < n; i++) {
        cin>>x[i]>>y[i];
    }
    int mini[3];
    double mini_val = std::numeric_limits<double>::max();
    for( int i = 0; i < n - 2; i++) {
        for( int j = i + 1; j < n - 1; j++) {
            for( int k = j + 1; k < n; k++) {
                double obw = sqrt(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2)) +
                             sqrt(pow(x[i] - x[k], 2) + pow(y[i] - y[k], 2)) +
                             sqrt(pow(x[k] - x[j], 2) + pow(y[k] - y[j], 2));
                if(obw <= mini_val) {
                    mini_val = obw;
                    mini[0] = i;
                    mini[1] = j;
                    mini[2] = k;
                }
            }
        }
    }
    cout<<x[mini[0]]<<" "<<y[mini[0]]<<endl;
    cout<<x[mini[1]]<<" "<<y[mini[1]]<<endl;
    cout<<x[mini[2]]<<" "<<y[mini[2]]<<endl;
    return 0;
}
