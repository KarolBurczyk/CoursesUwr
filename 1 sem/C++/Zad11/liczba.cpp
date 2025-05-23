#include "liczba.h++"

using namespace std;

Liczba::Liczba(const double& val)
    :Opernad(to_string(val))
{
    this->val = val;
}

