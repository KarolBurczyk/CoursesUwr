#include <iostream>
#include "wyrazenie.h++"
#include "typy.h++"
#include "stale.h++"
#include "1arg.h++"
#include "2arg.h++"



int main()
{
    //((x-1)*x)/2:
    Wyrazenie *w1 = new Dziel(
                    new Mnoz(
                            new Odejmij(
                                    new Zmienna("x"),
                                    new Liczba(1)),
                            new Zmienna("x")),
                    new Liczba(2));
    //(3+5)/(2+x*7):
    Wyrazenie *w2 = new Dziel(
                            new Dodaj(
                                    new Liczba(3),
                                    new Liczba(5)),
                            new Dodaj(
                                    new Liczba(2),
                                    new Mnoz(
                                            new Zmienna("x"),
                                            new Liczba(7)
                                            )
                                    )
                            );
    //2+x*7-(y*3+5):
    Wyrazenie *w3 = new Odejmij(
                        new Dodaj(
                                new Liczba(2),
                                new Mnoz(
                                        new Zmienna("x"),
                                        new Liczba(7)
                                        )
                                ),
                        new Dodaj(
                                new Mnoz(
                                        new Zmienna("y"),
                                        new Liczba(3)
                                ),
                                new Liczba(5)
                        )
    );


    //cos((x+1)*pi)/e^x^2:
    Wyrazenie *w4 = new Dziel(
            new Cos(
                    new Mnoz(
                            new Dodaj(
                                    new Zmienna("x"),
                                    new Liczba(1)
                                    ),
                            new pi()
                    )
            ),
            new Potega(
                    new e(),
                    new Potega(
                                new Zmienna("x"),
                                new Liczba(2)
                            )
            )
    );

    Wyrazenie *w = new Odejmij(
            new pi(),
            new Dodaj(
                    new Liczba(2),
                    new Mnoz(
                            new Zmienna("x"),
                            new Liczba(7)
                    )
            )
    );
    cout<<w->zapis()<<endl;
    for(double x = 0; x <= 1; x =  x + 0.01)
    {
        edit_zmienna("x", x);
        edit_zmienna("y", x);
        cout << "x = " << x << " dla " << w1->zapis() << " = "<< w1->oblicz() << endl;
        cout << "x = " << x << " dla " << w2->zapis() << " = "<< w2->oblicz() << endl;
        cout << "x = " << x << " dla " << w3->zapis() << " = "<< w3->oblicz() << endl;
        cout << "x = " << x << " dla " << w4->zapis() << " = "<< w4->oblicz() << endl;
    }
    cout<<"((x-1)*x)/2"<<endl;
    cout<<"(3+5)/(2+x*7)"<<endl;
    cout<<"2+x*7-(y*3+5)"<<endl;
    cout<<"cos((x+1)*pi)/e^x^2"<<endl;
    cout<<w1->zapis()<<endl;
    cout<<w2->zapis()<<endl;
    cout<<w3->zapis()<<endl;
    cout<<w4->zapis()<<endl;
}

