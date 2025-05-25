#include "typy.h++"
#include <sstream>
//KLASA LICZBA

Liczba::Liczba(double x)
{
    waga = 10;
    val = x;
}

double Liczba::oblicz() {
    return val;
}

string Liczba::zapis() {
    ostringstream temp;
    temp << this->val;
    return temp.str();
}

Stala::Stala(double x,string s)
{
    waga = 10;
    val = x;
    name = s;
}

double Stala::oblicz() {
    return val;
}

string Stala::zapis() {
    return name;
}

vector<pair<string, double>> Zmienna::zmienne {pair("x", 2), pair("y", 1)};

Zmienna::Zmienna(string s)
{
    waga = 10;
    key = s;
}

double Zmienna::oblicz() {
    for(int i=0; i<zmienne.size(); i++)
    {
        if(zmienne[i].first == key)
        {
            return zmienne[i].second;
        }
    }
}

string Zmienna::zapis() {
    return key;
}

void add_zmienna(string s, double x)
{
    Zmienna::zmienne.emplace_back(s,x);
}

void delete_zmienna(string s)
{
    for(int i=0; i<Zmienna::zmienne.size(); i++)
    {
        if(Zmienna::zmienne[i].first == s)
        {
            Zmienna::zmienne.erase(Zmienna::zmienne.begin()+i);
        }
    }
}

void edit_zmienna(string s, double x)
{
    for(int i=0; i<Zmienna::zmienne.size(); i++)
    {
        if(Zmienna::zmienne[i].first == s)
        {
            Zmienna::zmienne[i].second = x;
        }
    }
}


