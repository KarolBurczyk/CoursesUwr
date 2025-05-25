#include "piksel.h++"
#include <iostream>

using namespace std;

Piksel::Piksel()
{
    x = 0;
    y = 0;
}

Piksel::Piksel(int a, int b)
{
    if(a<=wymiary[0] and a>=0 and b<=wymiary[1] and b>=0)
    {
        x = a;
        y = b;
    }
    else throw invalid_argument("Poza wymiarami ekranu");
}

int Piksel::getUp()
{
    return y;
}
int Piksel::getDown()
{
    return wymiary[1] - y;
}
int Piksel::getLeft()
{
    return x;
}
int Piksel::getRight()
{
    return wymiary[0] - x;
}