#ifndef LISTA5_KOLORNT_H
#define LISTA5_KOLORNT_H
#include "kolornazwany.h++"
#include "kolortransparentny.h++"
class KolorNt
        :public KolorNazwany
        ,public KolorTransparentny
{
public:
    KolorNt();
    KolorNt(int, int, int, int, string);
};
#endif //LISTA5_KOLORNT_H
