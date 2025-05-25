//Karol Burczyk
//Programowanie obiektowe, lista 3: zad. 2
//do uruchomienia programu w systemie Windows 
//zainstalowałem wiersz poleceń Mono
//należy go uruchomić, przejść do lokalizacji plików i wpisać następujące komendy:
// mcs -t:library L3_zad3_klasa_dictionary.cs
//mcs L3_zad3_tester2.cs -r:L3_zad3_klasa_dictionary.dll
//i na końcu:
//mono L3_zad3_tester2.exe
using System;

public class L3_zad3_tester2
{
    public static void Main(string[] args)
    {
        MyDictionary d1 = new MyDictionary();
        d1.setElement("a", 1);
        d1.setElement("b", 2);
        d1.setElement("c", 3);
        Console.WriteLine(d1.searchElement("b"));
        d1.popElement("c");
        Console.WriteLine(d1.searchElement("c"));
        //po wywoładniu programu na konsoli wyświetla się komunikat o braku 
        //podanego elementu, a po nim 0, które jest związane z tym komunikatem
        d1.setElement("c", 4);
        Console.WriteLine(d1.searchElement("c"));
    }
}