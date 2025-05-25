#include <iostream>
#include "liczba.h++"

using namespace std;

int main()
{
    Liczba x;
    x.set_liczba(3.14);
    x.set_liczba(4.34);
    x.set_liczba(5.78);
    x.set_liczba(8.568);
    cout<<x.get_liczba()<<endl;
    cout<<x.get_history()<<endl;
    cout<<x.get_history()<<endl;
    cout<<x.get_history()<<endl;
    cout<<x.get_history()<<endl;
//    Liczba y(x);
//    cout<<y.get_liczba()<<endl;
//    y.set_liczba(99.78);
//    cout<<y.get_liczba()<<endl;
//    cout<<y.get_history()<<endl;
//    Liczba z = Liczba(9.99);
//    z.set_liczba(22.22);
//    z.set_liczba(33.33);
//    cout<<z.get_history()<<endl;
//    cout<<z.get_history()<<endl;
//    cout<<z.get_history()<<endl;
//    cout<<z.get_history()<<endl;
//    Liczba v(Liczba(9.99));
//    v.set_liczba(8.88);
//    v = z;
//    cout<<v.get_liczba()<<endl;
//    z = Liczba(7.77);
//    cout<<z.get_liczba()<<endl;

}

