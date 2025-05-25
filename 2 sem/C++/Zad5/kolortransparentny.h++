#ifndef LISTA5_KOLORTRANSPARENTNY_H
#define LISTA5_KOLORTRANSPARENTNY_H
#include "kolor.h++"
class KolorTransparentny
        : public Kolor
{
protected:
    int transparentnosc;
public:
    KolorTransparentny();
    KolorTransparentny(int, int, int, int);
    int getTransparentnosc();
    void setTransparentnosc(int);
};
#endif
