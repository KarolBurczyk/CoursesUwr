#include "liczba.h++"

using namespace std;

Liczba::Liczba()
{
    liczba = 0;
    indeks = 0;
    history_indeks = -1;
    czy_zawijac = false;
}

Liczba::Liczba(double x)
{
    liczba = x;
    indeks = 0;
    history_indeks = -1;
    czy_zawijac = false;
}

Liczba::Liczba(Liczba& x)
{
    liczba = x.liczba;
    indeks = 0;
    history_indeks = -1;
    czy_zawijac = false;
}

Liczba::Liczba(Liczba&& x)
:tablica(nullptr)
,indeks(0)
,history_indeks(-1)
,liczba(0)
{
    liczba = x.liczba;
    tablica = x.tablica;
    indeks = x.indeks;
    history_indeks = x.history_indeks;
    czy_zawijac = x.czy_zawijac;
    x.liczba = 0;
    x.indeks = 0;
    x.history_indeks = 0;
    x.tablica = nullptr;
}

Liczba::~Liczba() { delete[] tablica; }

Liczba & Liczba :: operator=(const Liczba & x)
{
    czy_zawijac = false;
    liczba = x.liczba;
    indeks = 0;
    history_indeks = -1;
}

Liczba & Liczba :: operator=(Liczba && x)
{
    if(this != &x)
    {
        delete[] tablica;
        tablica = x.tablica;
        liczba = x.liczba;
        indeks = x.indeks;
        czy_zawijac = x.czy_zawijac;
        history_indeks = x.history_indeks;
    }
    x.tablica = nullptr;
    x.indeks = 0;
    x.history_indeks = 0;
    x.liczba = 0;
}

double Liczba::get_liczba()  { return liczba; }

void Liczba::set_liczba(double x)
{
    if(indeks < dlugosc)
    {
        tablica[indeks] = liczba;
        liczba = x;
        indeks++;
        history_indeks++;
    }
    else
    {
        indeks = 0;
        tablica[indeks] = liczba;
        liczba = x;
        indeks++;
        history_indeks = 0;
        czy_zawijac = true;
    }

}

double Liczba::get_history()
{
    if(history_indeks >= 0)
    {
        if(not czy_zawijac and indeks == 0)
        {

            throw invalid_argument("brak historii");
        }
        else
        {
            history_indeks--;
            return tablica[history_indeks + 1];
        }
    }
    else if(czy_zawijac)
    {
        history_indeks = dlugosc - 1;
        history_indeks--;
        return tablica[history_indeks + 1];
    }
    else
    {
        history_indeks = indeks - 1;
        history_indeks--;
        return tablica[history_indeks + 1];
    }
}


