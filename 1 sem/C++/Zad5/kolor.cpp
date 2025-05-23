#include "kolor.h++"

Kolor::Kolor()
{
    R = 0;
    G = 0;
    B = 0;
}

Kolor::Kolor(int r, int g, int b)
{
    if(r<=255 and g<255 and b<255 and r>=0 and g>=0 and b>=0)
    {
        R = r;
        G = g;
        B = b;
    }
    else throw("Niepoprawne wartości");
}

int Kolor::getR()   { return R; }
int Kolor::getG()   { return G; }
int Kolor::getB()   { return B; }
void Kolor::setR(int r) { R = r; }
void Kolor::setG(int g) { G = g; }
void Kolor::setB(int b) { B = b; }
void Kolor::przyciemnij(double x)
{
    if(x>1 or x<0) throw("Wymagana liczba z zakresu od 0 do 1");
    else
    {
        R = (int)(R*x);
        G = (int)(G*x);
        B = (int)(B*x);
    }
}
void Kolor::polacz(Kolor x)
{
    R = (int)(R + x.getR())/2;
    G = (int)(G + x.getG())/2;
    B = (int)(B + x.getB())/2;
}
