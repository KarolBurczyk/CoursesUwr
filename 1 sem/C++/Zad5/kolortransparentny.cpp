#include "kolortransparentny.h++"
KolorTransparentny::KolorTransparentny()
{
    transparentnosc = 255;
}

KolorTransparentny::KolorTransparentny(int a, int b, int c, int x)
:Kolor(a, b, c)
{
    if(x>=0 and x<=255) { transparentnosc = x; }
    else throw("Niepoprawna wartość");
}

int KolorTransparentny::getTransparentnosc()
{
    return transparentnosc;
}

void KolorTransparentny::setTransparentnosc(int x)
{
    transparentnosc = x;
}