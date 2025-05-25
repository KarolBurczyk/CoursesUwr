#include <iostream>
#include <string>
#include "tab_bit.h++"

using namespace std;

//public:
    tab_bit::tab_bit (int rozm)
    {
        static const int rozmiarSlowa = rozm; // rozmiar slowa w bitach
        int dl = rozm; // liczba bitów
        slowo *tab; // tablica bitów
        for(int i = 0; i<dl/64+1; i++)   tab[i] = 0;
    }// wyzerowana tablica bitow [0...rozm]

    tab_bit::tab_bit (slowo tb)
    {
        const string tmp = to_string(tb);
        static const int rozmiarSlowa = tmp.length(); // rozmiar slowa w bitach
        int dl = rozmiarSlowa; // liczba bitów
        slowo *tab = &tb; // tablica bitów
    }// tablica bitów [0...rozmiarSlowa] zainicjalizowana wzorcem

    tab_bit::tab_bit (const tab_bit &tb)
    {
        static const int rozmiarSlowa = tb.rozmiarSlowa; // rozmiar slowa w bitach
        int dl = tb.dl; // liczba bitów
        slowo *tab = tb.tab; // tablica bitów
    }// konstruktor kopiujący

    tab_bit::tab_bit (tab_bit &&tb)
    :tab(nullptr)
    ,dl(0)
    {
        static const int rozmiarSlowa = tb.rozmiarSlowa; // rozmiar slowa w bitach
        int dl = tb.dl; // liczba bitów
        slowo *tab = tb.tab; // tablica bitów
        tb.tab = nullptr;
        tb.dl = 0;
    }// konstruktor przenoszący

    tab_bit & tab_bit::operator = (const tab_bit &tb)
    {
        static const int rozmiarSlowa = tb.rozmiarSlowa; // rozmiar slowa w bitach
        int dl = tb.dl; // liczba bitów
        slowo *tab = tb.tab; // tablica bitów
        return *this;
    }// przypisanie kopiujące

    tab_bit & tab_bit::operator = (tab_bit &&tb)
    {
        if(this != 0)
        {
            delete[] tab;
            static const int rozmiarSlowa = tb.rozmiarSlowa; // rozmiar slowa w bitach
            int dl = tb.dl; // liczba bitów
            slowo *tab = tb.tab; // tablica bitów
        }
        tb.tab = nullptr;
        tb.dl = 0;
        return *this;
    }// przypisanie przenoszące

//    istream & operator >> (istream &we, tab_bit &tb)
//    {
//        typedef uint64_t slowo;
//        char a;
//        slowo b = 0;
//        for(int i = 0; i < tb.dl; i++)
//        {
//            we>>a;
//            b = stoi(a);
//            tb[i] = 1;
//        }
//    }
    ostream & operator << (ostream &wy, const tab_bit &tb)
    {
        wy<<"{";
        for(int i = 0; i < tb.dl; i++)
        {
            wy<<tb[i]<<" ";
        }
        wy<<"}";
    }

    tab_bit::~tab_bit ()
    {
        delete[] tab;
    }// destruktor

//private:
    bool tab_bit::czytaj (int i) const
    {
        return tab[i];
    }// metoda pomocnicza do odczytu bitu
    bool tab_bit::pisz (int i, bool b)
    {
        tab[i] = b;
    }// metoda pomocnicza do zapisu bitu
//public:
    bool tab_bit::operator[] (int i) const
    {
        return tab[i];
    }// indeksowanie dla stałych tablic bitowych
    ref tab_bit::operator[] (int i)
    {
        ref a;
        a.wczytaj_ref(this, i);
        return a;
    }// indeksowanie dla zwykłych tablic bitowych
    inline int tab_bit::rozmiar () const
    {
        return rozmiarSlowa;
    }// rozmiar tablicy w bitach
//public:
    // operatory bitowe: | i |=, & i &=, ^ i ^= oraz !
//public:
    // zaprzyjaźnione operatory strumieniowe: << i >>