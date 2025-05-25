#ifndef ZAD6_TYPY_H
#define ZAD6_TYPY_H

#include "wyrazenie.h++"
#include<vector>

//KLASA LICZBA

class Liczba final
        :public Wyrazenie
{
protected:
    double val;
public:
    explicit Liczba(double);
    double oblicz() override;
    string zapis() override;

};

class Stala
        :public Wyrazenie
{
protected:
    double val;
    string name;
public:
    explicit Stala(double, string);
    double oblicz() override;
    string zapis() override;
};

class Zmienna final
        :public Wyrazenie
{
private:
    static vector<pair<string, double>> zmienne;
protected:
    string key;
public:
    explicit Zmienna(string);
    double oblicz() override;
    string zapis() override;
    friend void add_zmienna(string s, double x);
    friend void delete_zmienna(string s);
    friend void edit_zmienna(string s, double x);

};

void add_zmienna(string s, double x);

void delete_zmienna(string s);

void edit_zmienna(string s, double x);



#endif
