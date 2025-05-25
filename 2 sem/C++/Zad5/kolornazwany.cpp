#include "kolornazwany.h++"
KolorNazwany::KolorNazwany()
{
    nazwa = "";
}

KolorNazwany::KolorNazwany(int a, int b, int c, string x)
:Kolor(a, b, c)
{
    string haslo = "";
    for(int i = 0; i<x.size(); i++)
    {
        if(x[i] >= 96 and x[i] <= 122)
        {}
        else throw invalid_argument ("Nazwa musi sie skladac z malych liter alfabetu angielskiego");
    }
    nazwa = x;
}

KolorNazwany::KolorNazwany(string x)
{
    string haslo = "";
    for(int i = 0; i<x.size(); i++)
    {
        if(x[i] >= 97 and x[i] <= 122)
        {}
        else throw invalid_argument ("Nazwa musi sie skladac z malych liter alfabetu angielskiego");
    }
    nazwa = x;
}

string KolorNazwany::getNazwa()
{
    return nazwa;
}

void KolorNazwany::setNazwa(string x)
{
    nazwa = x;
}
