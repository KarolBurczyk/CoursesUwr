#include <iostream>
#include "kolor.h++"
#include "kolortransparentny.h++"
#include "kolornazwany.h++"
#include "kolornt.h++"
#include "piksel.h++"
#include "pikselkolorowy.h++"

int main()
{
    KolorNt a(1, 2, 3, 10, "niebieski");
    cout<<a.getNazwa()<<endl;
    Piksel p(3, 99);
    cout<<p.getLeft()<<endl;
    KolorTransparentny t(2, 3, 6, 9);
    cout<<t.getR()<<" "<<t.getG()<<" "<<t.getB()<<endl;
    Kolor c(0, 1, 1);
    cout<<c.getG()<<endl;
    KolorNazwany n(1, 3, 5, "czerwony");
    cout<<n.getNazwa()<<endl;
    PikselKolorowy pk(11, 11, 11, 6, 7, 8);
    cout<<pk.getUp()<<" "<<pk.getLeft()<<endl;
    pk.przesuniecie(10, 10);
    cout<<pk.getUp()<<" "<<pk.getLeft()<<endl;
    cout<<c.getR()<<" "<<c.getG()<<" "<<c.getB()<<endl;
    c.polacz(pk);
    cout<<c.getR()<<" "<<c.getG()<<" "<<c.getB()<<endl;
    c.przyciemnij(0.5);
    cout<<c.getR()<<" "<<c.getG()<<" "<<c.getB()<<endl;
}
