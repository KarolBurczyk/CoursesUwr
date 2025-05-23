#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits>
#include <utility>
#include <vector>

using namespace std;

struct Mini {
    pair<int, int> a, b, c;
    double obw;
};

Mini brute(const pair<int, int> y[], int n) {
    Mini mini{};
    mini.obw = std::numeric_limits<double>::max();
    for( int i = 0; i < n - 2; i++) {
        for( int j = i + 1; j < n - 1 && (y[j].second - y[i].second) < mini.obw/2; j++) {
            for( int k = j + 1; k < n && (y[k].second - y[j].second) < mini.obw/2; k++) {
                double obw = sqrt(pow(y[i].first - y[j].first, 2) + pow(y[i].second - y[j].second, 2)) +
                             sqrt(pow(y[i].first - y[k].first, 2) + pow(y[i].second - y[k].second, 2)) +
                             sqrt(pow(y[k].first - y[j].first, 2) + pow(y[k].second - y[j].second, 2));
                if(obw <= mini.obw) {
                    mini.obw = obw;
                    mini.a = y[i];
                    mini.b = y[j];
                    mini.c = y[k];
                }
            }
        }
    }
    return mini;
}

Mini rek(const pair<int, int> x[], const pair<int, int> y[], int n) {
    if(n <= 5) {
        return brute(y, n);
    }
    int p = n / 2;
    pair<int, int> yl[p], yr[n-p];
    int li = 0, ri = 0;
    for (int i = 0; i < n; i++) {
        if ((y[i].first < x[p].first || (y[i].first == x[p].first && y[i].second < x[p].second)) && li < p)
            yl[li++] = y[i];
        else
            yr[ri++] = y[i];
    }
    Mini r = rek(x + p, yr, n-p), l = rek(x, yl, p);
    Mini mini{};
    if(r.obw < l.obw) {
        mini = r;
    }
    else {
        mini = l;
    }
    double d = mini.obw/2;

    pair<int, int> strip[n];
    int id = 0;
    for (int i = 0; i < n; i++) {
        if (abs(y[i].first - x[p].first) <= d) {
            strip[id++] = y[i];
        }
    }

    Mini res = brute(strip, id);
    if(res.obw < mini.obw) {
        mini = res;
    }
    return mini;
}

int main() {

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n;
    scanf("%d", &n);

    pair<int, int> x[n], y[n];
    for (int i = 0; i < n; ++i) {
        scanf("%d %d", &x[i].first, &x[i].second);
    }
    copy(x, x + n, y);
    sort(x, x + n);
    sort(y, y + n, [](pair<int, int> a, pair<int, int> b) {return a.second < b.second;});

    Mini res = rek(x, y, n);
    printf("%d %d\n", res.a.first, res.a.second);
    printf("%d %d\n", res.b.first, res.b.second);
    printf("%d %d\n", res.c.first, res.c.second);

    return 0;
}
