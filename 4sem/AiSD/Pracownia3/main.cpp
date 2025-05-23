#include <iostream>
#include <algorithm>

using namespace std;

struct Moneta {
    int p, w;
};


int main() {
    int F, C;
    bool sol = true;
    cin >> F;
    cin >> C;
    Moneta cena[C];
    int maxi_monety[C], mini_monety[C];
    int maxi_path[F], mini_path[F];
    int mini[F + 1], maxi[F + 1];
    for ( int i = 0; i < C; i++) {
        cin >> cena[i].p >> cena[i].w;
        maxi_monety[i] = 0;
        mini_monety[i] = 0;
    }
    for (int i = 0; i < F + 1 ; i++) {
        mini[i] = 0;
        maxi[i] = 0;
        mini_path[i] = -1;
        maxi_path[i] = -1;
    }
    for (int c = 0; c < C ; c++) {
        for (int f = 1; f < F + 1; f++) {
            if (f - cena[c].w >= 0) {
                if (maxi[f - cena[c].w] + cena[c].p > maxi[f]) {
                    maxi[f] = maxi[f - cena[c].w] + cena[c].p;
                    maxi_path[f] = c;
                }
                if (mini[f - cena[c].w] + cena[c].p < mini[f]) {
                    mini[f] = mini[f - cena[c].w] + cena[c].p;
                    mini_path[f] = c;
                }
                else if (mini[f] == 0){
                    mini[f] = mini[f - cena[c].w] + cena[c].p;
                    mini_path[f] = c;
                }
            }
        }
    }
    int id = F;
    while (true) {
        if (maxi_path[id] == -1){
            sol = false;
            cout<<"NIE";
            break;
        }
        maxi_monety[maxi_path[id]] ++;
        id = id - cena[maxi_path[id]].w;
        if (id == 0) {
            cout<<"TAK"<<endl;
            break;
        }
    }
    id = F;
    while (true) {
        if (mini_path[id] == -1){
            sol = false;
            break;
        }
        mini_monety[mini_path[id]] ++;
        id = id - cena[mini_path[id]].w;
        if (id == 0) {
            break;
        }
    }
    if(sol) {
        cout<<mini[F]<<endl;
        for(int i = 0; i < C; i ++) {
            cout<<mini_monety[i]<<" ";
        }
        cout<<endl<<maxi[F]<<endl;
        for(int i = 0; i < C; i ++) {
            cout<<maxi_monety[i]<<" ";
        }
    }


    return 0;
}
