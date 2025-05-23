#ifndef ZAD4_REF_H
#define ZAD4_REF_H
#include <iostream>
#include "tab_bit.h++"
class ref
{
public:
    typedef uint64_t slowo;
    friend class tab_bit;
    slowo *ref_val = nullptr;
    ref();
    ~ref();
    void wczytaj_ref(const tab_bit&, int i);
    ref& operator=(bool x);
};
#endif //ZAD4_REF_H
