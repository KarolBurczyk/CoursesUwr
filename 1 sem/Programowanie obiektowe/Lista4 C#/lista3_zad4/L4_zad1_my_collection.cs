//Karol Burczyk
//Programowanie obiektowe, lista 4: zad. 1
//program pisałem i kompilowałem przy użyciu Rider'a

using System;
using System.Collections;

interface ListCollection
{
    string[] _ciag;
    private int[] values = new int[1];
    private string[] keys = new string[1];
    private int space = 0;
    
}

public class SlowaFibonacciego : IEnumerable : ListCollection
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

public class MyDictionary
{
    private int[] values = new int[1];
    //tablica wartości (na początku 1-elementowa)
    private string[] keys = new string[1];
    //tablica kluczy (na początku 1-elementowa)
    private int space = 0;
    //wskaźnik na najbliższe wolne miejsce w tablicach kluczy i wartości

    public void setElement(string key, int value)
    //metoda do dodawania elementu do słownika
    {
        bool czy = false;
        //wartość zmieniająca się, jeżeli istnieje już wartość o takim kluczu
        for (int i = 0; i < keys.Length; i++)
        {
            if (keys[i] == key)
            {
                czy = true;
                break;
                //jeżeli już istnieje, to kończymy przeglądanie słownika 
            }
        }

        if (czy == false)
        {
            //jeżeli nie istnieje element o podanym kluczu, wykonujemy: 
            values[space] = value;
            keys[space] = key;
            //wartość i klucz dodajemy na wolne pole wskazane przez "space"
            space++;
            //następnie zwiększamy wartość wskazującą wolne pole
            Array.Resize(ref values, values.Length + 1);
            Array.Resize(ref keys, keys.Length + 1);
            //oraz zwiększamy wielkość tablic
        }
        else
        {
            Console.WriteLine("Istnieje juz element o takim kluczu");
            //w innym przypadku wypisujemy, że istnieje taki klucz w słowniku
        }
    }

    public int searchElement(string key)
    //metoda wyszukująca element o podanym kluczu
    {
        for (int i = 0; i < space; i++)
        {
            if (key == keys[i])
            {
                //gdy znajdziemy element o podanym kluczu, zwracamy zapisaną pod nim wartość
                return values[i];
            }
        }
        Console.WriteLine("Nie ma wartosci dla podanego klucza");
        //w innym przypadku wypisujemy, że nie ma takiego elementu i zwracamy 0
        return 0;
    }

    public void popElement(string key)
    {
        int[] v1 = new int[values.Length-1];
        string[] k1 = new string[keys.Length-1];
        //definiujemy nowe tablice o rozmiarze o jeden mniejszym
        bool czy = false;
        //wartość zmieniająca się, jeżeli istnieje już wartość o takim kluczu
        for (int i = 0; i < space; i++)
        {
            if (keys[i] == key)
            {
                czy = true;
                //kiedy znajdziemy wartość pod podanym kluczem,
                //zmieniamy wartość "czy" na true
            }
            else
            {
                //w każdym innym przypadku przenosimy wartość i klczue z
                //naszego słownika do nowo utworzonych tablic, oczywiście 
                //oprócz tych, które chemy usunąć
                v1[i] = values[i];
                k1[i] = keys[i];
            }
        }
        
        if (czy)
        {
            //jeżeli znaleźliśmy wartość pod podanym kluczem, to
            //zastępujemy tablice kluczów i wartość tymi nowo utworzonymi,
            //bez elementów, które chcieliśmy usunąć
            values = v1;
            keys = k1;
            //następnie zmniejszamy wskaźnik wolnego pola, z racji, że
            //cała tablica nam się zmniejszyła
            space--;
        }
        else
        {
            //w innym przypadku wypisujemy poniższą informację
            Console.WriteLine("Nie ma wartosci dla podanego klucza");
        }
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