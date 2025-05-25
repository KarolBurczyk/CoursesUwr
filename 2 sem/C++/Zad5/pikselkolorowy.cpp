#include "pikselkolorowy.h++"
#include <iostream>
#include <cmath>
using namespace std;

PikselKolorowy::PikselKolorowy()
:Piksel(0, 0)
,KolorTransparentny(0, 0, 0, 0)
{}

PikselKolorowy::PikselKolorowy(int r, int g, int b, int t, int x, int y)
:Piksel(x, y)
,KolorTransparentny(r, g, b, t)
{}

void PikselKolorowy::przesuniecie(int a, int b)
{
    if(x+a<=1920 and y+b<=1080 and x+a>=0 and y+b>=0)
    {
        x += a;
        y += b;
    }
    else throw invalid_argument ("Przesuniecie poza wymiarami ekranu");
}

int odleglosc(PikselKolorowy &p, PikselKolorowy &q)
{
    return sqrt(pow(abs(p.getLeft()-q.getLeft()), 2) + pow(abs(p.getUp()-q.getUp()), 2));
}

int odleglosc(PikselKolorowy *p, PikselKolorowy *q)
{
    return sqrt(pow(abs(p -> getLeft()-q -> getLeft()), 2) + pow(abs(p -> getUp()-q -> getUp()), 2));
}