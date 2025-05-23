#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <utility>

using namespace std;

int main() {
    int n, q, a, b, tmp;
    cin >> n >> q;

    pair<int, int> edges[n-1];
    pair<int, int> times[n];
    int vertices[n];
    bool visited[n];
    for(int i = 0; i < n; i++) {
        vertices[i] = -1;
        visited[i] = false;
    }

    for (int i = 0; i < n - 1; i++) {
        cin >> tmp;
        edges[i] = (pair(tmp - 1, i + 1));
    }

    sort(edges, edges + n);

    int prev = -1;
    for (int i = 0; i < n-1; i++) {
        int curr = edges[i].first;
        if (curr != prev) {
            vertices[curr] = i;
            prev = curr;
        }
    }

    stack<int> stos;
    stos.push(0);
    visited[0] = true;
    int time = 1;

    while (!stos.empty()) {
        int v = stos.top();
        if (!visited[v]) {
            times[v].first = time;
            time++;
            visited[v] = true;
        }
        int i = vertices[v];
        bool all_visited = true;
        if(i != -1) {
            while (i < n - 1 && edges[i].first == v) {
                if (!visited[edges[i].second]) {
                    stos.push(edges[i].second);
                    all_visited = false;
                }
                i++;
            }
        }
        if (all_visited) {
            times[v].second = time;
            time++;
            stos.pop();
        }
    }

    for(int i = 0; i < q; i++) {
        cin>>a>>b;
        if(times[b-1].first > times[a-1].first && times[b-1].second <= times[a-1].second) {
            cout<<"TAK"<<endl;
        }
        else {
            cout<<"NIE"<<endl;
        }
    }
    return 0;
}