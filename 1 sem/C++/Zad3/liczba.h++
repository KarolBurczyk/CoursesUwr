#ifndef CLASSES_HPP
#define CLASSES_HPP
#include <iostream>
#include <cmath>
#include <new>
#include <vector>

using namespace std;

class Liczba
{
private:
    double liczba;
    bool czy_zawijac;
    static const int dlugosc = 3;
    double *tablica = new double[dlugosc];
    int indeks;
    int history_indeks;

public:
    Liczba();
    Liczba(double);
    Liczba(Liczba&);
    Liczba(Liczba&&);
    ~Liczba();

    Liczba& operator=(const Liczba &);

    Liczba& operator=(Liczba &&);

    double get_liczba();
    void set_liczba(double x);
    double get_history();
};


#endif
