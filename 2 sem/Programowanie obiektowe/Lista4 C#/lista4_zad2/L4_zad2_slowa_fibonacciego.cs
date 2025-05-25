//Karol Burczyk
//Programowanie obiektowe, lista 4: zad. 2
//program pisałem i kompilowałem przy użyciu Rider'a

using System;
using System.Collections;

public class SlowaFibonacciego : IEnumerable
//definicja SlowaFibonacciego
{
    private string[] _ciag = {"Null"};
    //defuniuję tablicę stringów z jedną wartością (Null), w razie wywołania
    //SlowaFibonacciego(0)

    public SlowaFibonacciego(int x)
        //konstruktor z jedynm argumentem oznaczającym długość naszego ciągu
    {
        if(x <= 0)
        {
            Console.WriteLine("Niepoprawny argument");
            //w razie wywołania dla 0 wypisuje niepoprawny argument
        }
        else
        {
            string[] slowa = new string[x];
            //definiuję innę tablicę stringów
            slowa[0] = "b";
            //jej pierwszym elementem będzie na pewno 'b'
            if (x >= 2) slowa[1] = "a";
            //jeżeli do konstruktora dostaliśmy liczbę >=2 to będzie tam 
            //również 'a'
            if (x > 2)
            {
                for (int i = 2; i < x; i++)
                {
                    slowa[i] = slowa[i - 1] + slowa[i - 2];
                }
                //w każdym innym przypadku kolejne elementy tablicy otrzymuję
                //ze złożenia dwóch wcześniejszych słów
            }

            _ciag = slowa;
            //na koniec wrzucam nową tablicę na miejsce zdefiniowanej powyżej
        }
    }
    public IEnumerator GetEnumerator()
        //implementacja z GetEnumerator 
    {
        return _ciag.GetEnumerator();
        //zwracanie elementu z naszej tablicy
    }

}

public class Program
{
    public static void Main(string[] args)
    {
        SlowaFibonacciego sf = new SlowaFibonacciego(12);
        foreach (string s in sf)
        {
            Console.WriteLine(s);
        }
    }
}