#ifndef LISTA5_PIKSELKOLOROWY_H
#define LISTA5_PIKSELKOLOROWY_H
#include "kolortransparentny.h++"
#include "piksel.h++"
class PikselKolorowy
        :public KolorTransparentny
        ,public Piksel
{
public:
    PikselKolorowy();
    PikselKolorowy(int, int, int, int, int, int);
    void przesuniecie(int, int);
};

int odleglosc(const PikselKolorowy &p, const PikselKolorowy &q);
int odleglosc(const PikselKolorowy *p, const PikselKolorowy *q);

#endif
