//Karol Burczyk
//Programowanie obiektowe, lista 3: zad. 4
//do uruchomienia programu w systemie Windows 
//zainstalowałem wiersz poleceń Mono
//należy go uruchomić, przejść do lokalizacji plików i wpisać następujące komendy:
// mcs -t:library L3_zad4_klasa_wektor.cs
//mcs L3_zad4_tester.cs -r:L3_zad4_klasa_wektor.dll
//i na końcu:
//mono L3_zad4_tester.exe
using System;

public class Program
{
    public static void Main(string[] args)
    {
        Wektor w1 = new Wektor();
        Wektor w2 = new Wektor();
        float[] tab1 = { 1, 2, 3 };
        w1.DodajWektor(tab1);
        Console.Write("Wektor w1: ");
        w1.wydrukujWektor();
        w2 = w1 * w1;
        Console.Write("Wektor w2 rowny kwadratowi w1 : ");
        w2.wydrukujWektor();
        w2 = w2 * 3;
        Console.Write("Wektor w2 pomnozony przez skalar 3 : ");
        w2.wydrukujWektor();
        w2 = w2 + w1;
        Console.Write("Suma wektora w1 i w2 : ");
        w2.wydrukujWektor();
        Console.WriteLine("Dlugosc wektora w2: " + w2.norma());
    }
}
