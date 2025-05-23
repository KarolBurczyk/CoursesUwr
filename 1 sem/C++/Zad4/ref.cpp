#include "ref.h++"
#include <iostream>

using namespace std;

ref::ref()
{
    ref_val = nullptr;
}
ref::~ref()
{
    ref_val = nullptr;
}

void ref::wczytaj_ref(const tab_bit& x, int i)
{
    ref_val = &x.tab[i];
}

ref & ref::operator = (bool x)
{
    ref_val = reinterpret_cast<slowo *>(x);
}

bool operator =(ref x)
{

}

