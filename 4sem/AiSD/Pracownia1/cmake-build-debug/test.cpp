#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

bool first(const tuple<int, int>& p, const tuple<int, int>& q) {
    return get<0>(p) < get<0>(q);
}

vector<tuple<int, int>> dfs(const vector<tuple<int, int>>& edges, vector<tuple<int, int>>& times, vector<bool>& visited, vector<int>& vertices) {
    stack<int> stos;
    stos.push(0);
    visited[0] = true;
    int time = 1;

    while (!stos.empty()) {
        int n = stos.top();
        if (!visited[n]) {
            get<0>(times[n]) = time;
            time++;
            visited[n] = true;
        }
        long unsigned int i = vertices[n];
        bool all_visited = true;
        while (i < edges.size() && get<0>(edges[i]) == n) {
            if (!visited[get<1>(edges[i])]) {
                stos.push(get<1>(edges[i]));
                all_visited = false;
            }
            i++;
        }
        if (all_visited) {
            get<1>(times[n]) = time;
            time++;
            stos.pop();
        }
    }
    return times;
}

int main() {
    int n, q, a, b, tmp;
    cin >> n >> q;

    vector<tuple<int, int>> edges;
    vector<tuple<int, int>> times(n);
    vector<int> vertices(n, 0);
    vector<bool> visited(n, false);

    for (int i = 0; i < n - 1; i++) {
        cin >> tmp;
        edges.push_back(make_tuple(tmp - 1, i + 1));
    }

    int prev = -1;
    for (long unsigned int i = 0; i < edges.size(); i++) {
        int curr = get<0>(edges[i]);
        if (curr != prev) {
            vertices[curr] = i;
            prev = curr;
        }
    }

    sort(edges.begin(), edges.end(), first);

    dfs(edges, times, visited, vertices);

    for(int i = 0; i < q; i++) {
        cin>>a>>b;
        if(get<0>(times[b-1]) > get<0>(times[a-1]) && get<1>(times[b-1]) <= get<1>(times[a-1])) {
            cout<<"TAK"<<endl;
        }
        else {
            cout<<"NIE";
        }
    }
    return 0;
}