#ifndef LISTA5_KOLORNAZWANY_H
#define LISTA5_KOLORNAZWANY_H
#include "kolor.h++"
#include <iostream>

using namespace std;

class KolorNazwany
        :public Kolor
{
protected:
    string nazwa;
public:
    KolorNazwany();
    KolorNazwany(int, int, int, string);
    KolorNazwany(string);
    string getNazwa();
    void setNazwa(string);
};
#endif
