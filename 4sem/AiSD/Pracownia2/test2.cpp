#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits>
#include <utility>

using namespace std;

struct Mini {
    int a, b, c;
    double obw;
    char id;
};

Mini rek(const pair<int, int> x[], const pair<int, int> y[], int begin, int end, int n){
    if(end - begin < 5) {
        Mini mini{};
        mini.obw = std::numeric_limits<double>::max();
        for( int i = begin; i <= end - 2; i++) {
            for( int j = i + 1; j <= end - 1; j++) {
                for( int k = j + 1; k <= end; k++) {
                    double obw = sqrt(pow(x[i].first - x[j].first, 2) + pow(x[i].second - x[j].second, 2)) +
                                 sqrt(pow(x[i].first - x[k].first, 2) + pow(x[i].second - x[k].second, 2)) +
                                 sqrt(pow(x[k].first - x[j].first, 2) + pow(x[k].second - x[j].second, 2));
                    if(obw <= mini.obw) {
                        mini.obw = obw;
                        mini.a = i;
                        mini.b = j;
                        mini.c = k;
                        mini.id = 'x';
                    }
                }
            }
        }
        return mini;
    }
    else {
        int p = begin + (end - begin)/2;
        Mini r = rek(x, y, p + 1, end, n), l = rek(x, y, begin, p, n);
        Mini mini{};
        if(r.obw < l.obw) {
            mini.obw = r.obw;
            mini.a = r.a;
            mini.b = r.b;
            mini.c = r.c;
            mini.id = r.id;
        }
        else {
            mini.obw = l.obw;
            mini.a = l.a;
            mini.b = l.b;
            mini.c = l.c;
            mini.id = l.id;
        }
        double d = mini.obw/2;

        int strip[end - begin + 1], siz = 0;
        for (int i = 0; i < n; i++) {
            if (abs(y[i].first - x[p].first) <= d) {
                strip[siz] = i;
                siz++;
            }
        }

        for (int i = 0; i < siz - 2; i++) {
            for (int j = i + 1; j < siz - 1 && abs(y[strip[j]].second - y[strip[i]].second) < d; j++) {
                for (int k = j + 1; k < siz && abs(y[strip[k]].second - y[strip[i]].second) < d; k++) {
                    double obw = sqrt(pow(y[strip[i]].first - y[strip[j]].first, 2) + pow(y[strip[i]].second - y[strip[j]].second, 2)) +
                                 sqrt(pow(y[strip[i]].first - y[strip[k]].first, 2) + pow(y[strip[i]].second - y[strip[k]].second, 2)) +
                                 sqrt(pow(y[strip[k]].first - y[strip[j]].first, 2) + pow(y[strip[k]].second - y[strip[j]].second, 2));
                    if (obw < mini.obw) {
                        mini.obw = obw;
                        mini.a = strip[i];
                        mini.b = strip[j];
                        mini.c = strip[k];
                        mini.id = 'y';
                    }
                }
            }
        }
        return mini;
    }
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
    sort(y, y + n, [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    Mini res = rek(x, y, 0, n - 1, n);
    if(res.id == 'x') {
        printf("%d %d\n", x[res.a].first, x[res.a].second);
        printf("%d %d\n", x[res.b].first, x[res.b].second);
        printf("%d %d\n", x[res.c].first, x[res.c].second);
    }
    else {
        printf("%d %d\n", y[res.a].first, y[res.a].second);
        printf("%d %d\n", y[res.b].first, y[res.b].second);
        printf("%d %d\n", y[res.c].first, y[res.c].second);
    }

    return 0;
}
