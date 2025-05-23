//Katarzyna Jodłowska
//Programowanie obiektowe, lista 3 zadanie 4
//aby uruchomić program na systemie linux należy wpisac w terminal:
// mcs -t:library klasy.cs
//następnie:
//mcs Program.cs -r:klasy.dll
//oraz,aby zobaczyć wynik programu:
//mono Program.exe
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
