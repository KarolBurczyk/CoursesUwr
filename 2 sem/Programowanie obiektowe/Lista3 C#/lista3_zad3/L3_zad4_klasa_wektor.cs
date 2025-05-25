using System;

public class Wektor 
    //deklaracja klasy wektora
{
    private static int liczbaWymiarow; 
    //prywatna liczba wymiarow wektora
    
    private float[] wymiary = new float[liczbaWymiarow]; 
    //wymiary wektora zapisane w tablicy "wymiary" o rozmiarze "liczbaWymiarow"

    public void DodajWektor(float[] tablica)
    {
        liczbaWymiarow = tablica.Length;
        wymiary = tablica;
    }
    //metoda dodająca liczbę wymiarów i ich wartości do obiektu
    public float[] zwrocWektor()
    {
        return wymiary;
    }
    //metoda zwracająca tablicę z wymiarami wektora 

    public void wydrukujWektor()
    {
        Console.Write("(");
        for (int i = 0; i < liczbaWymiarow-1; i++)
        {
            Console.Write(wymiary[i] + ", ");
        }
        Console.Write(wymiary[liczbaWymiarow-1] + ")");
        Console.WriteLine();
    }
    //metoda wypisująca na wyjściu konsoli wektor 

    public int zwrocRozmiar()
    {
        return liczbaWymiarow;
    }
    //metoda zwracająca liczbę wymiarów wektora 
        
    //metoda dodająca dwa wektory:
    public static Wektor operator +(Wektor w1, Wektor w2)
    //definiujemy operator "+" operujący na dwóch obiektach typu Wektor
    //zwracający dodawanie wektorów
    {
        if (w1.zwrocRozmiar() != w2.zwrocRozmiar())
        {
            Console.WriteLine("Nie mozna dodac wektorow o roznych rozmiarach");
            return w1;
            //jezeli rozmiary dodawanych wektorow sa
            //rozne to nie mozemy ich dodac
        }
        else
        {
            Wektor w3 = new Wektor(); //definiujemy trzeci wektor, który 
            //będzie sumą dwóch podanych na wejściu
            float[] tablica = new float[w1.zwrocRozmiar()];
            //tworzymy tablicę o rozmiarze dodawanych wektorów
            for (int i = 0; i < w1.zwrocRozmiar(); i++)
            {
                tablica[i] = w1.zwrocWektor()[i] + w2.zwrocWektor()[i];
                //do i-tego elementu tablicy wstawiamy sumę i-tych wymiarów
                //wektorów w1 i w2
            }
            w3.DodajWektor(tablica);
            return w3;
            //definiujemy wymiary wektora przez tablicę wypełnioną przed chwilą
            //następnie ją zwracamy 
        }
    }
    
    //metoda mnożąca dwa wektory:
    public static Wektor operator *(Wektor w1, Wektor w2)
        //definiujemy operator "*" operujący na dwóch obiektach typu Wektor
        //zwracający mnożenie wektorów
    {
        if (w1.zwrocRozmiar() != w2.zwrocRozmiar())
        {
            Console.WriteLine("Nie mozna dodac wektorow o roznych rozmiarach");
            return w1;
            //jezeli rozmiary mnożonych wektorow sa
            //rozne to nie mozemy ich pomnożyć
        }
        else
        {
            Wektor w3 = new Wektor(); //definiujemy trzeci wektor, który 
            //będzie iloczynem dwóch podanych na wejściu
            float[] tablica = new float[w1.zwrocRozmiar()];
            //tworzymy tablicę o rozmiarze mnożonych wektorów
            for (int i = 0; i < w1.zwrocRozmiar(); i++)
            {
                tablica[i] = w1.zwrocWektor()[i] * w2.zwrocWektor()[i];
                //do i-tego elementu tablicy wstawiamy iloczyn i-tych wymiarów
                //wektorów w1 i w2
            }
            w3.DodajWektor(tablica);
            return w3;
            //definiujemy wymiary wektora przez tablicę wypełnioną przed chwilą
            //następnie ją zwracamy 
        }
    }
    
    //metoda mnożąca wektor przez skalar:
    public static Wektor operator *(Wektor w1, float skalar)
    //definiujemy operację "*" na obiektach Wektor i float jako
    //mnozenie wektora przez skalar
    {
        Wektor w2 = new Wektor(); //definiujemy trzeci wektor, który 
        //będzie iloczynem dwóch podanych na wejściu
        float[] tablica = new float[w1.zwrocRozmiar()];
        //tworzymy tablicę o rozmiarze mnożonych wektorów
        for (int i = 0; i < w1.zwrocRozmiar(); i++)
        {
            tablica[i] = w1.zwrocWektor()[i] * skalar;
            //do i-tego elementu tablicy wrzucamy iloczyn skalara i 
            //i-tego wymiaru wektora
        }
        w2.DodajWektor(tablica);
        return w2;
        //opisujemy wektor wymiarami z tablicy i następnie zwracamy
    }

    //metoda zwracająca długość wektora:
    public float norma()
    {
        Wektor w2 = new Wektor();
        //definiujemy nowy wektor
        w2.DodajWektor(wymiary);
        //definiujemy jego wymiary jako takie same, jak tego, którego 
        //długość mamy obliczyć
        w2 *= w2;
        //podnosimy go do kwadratu 
        float[] tablica = w2.zwrocWektor();
        //tworzymy nową wtablicę i zapisujemy pod nią wymiary naszego wektora
        //podniesione do kwadratu
        float suma = 0;
        for (int i = 0; i < w2.zwrocRozmiar(); i++)
        {
            suma += tablica[i];
            //sumujemy wszystkie wymiaru wektora
        }
        suma = (float)Math.Sqrt(suma);
        //następnie je pierwiastkujemy 
        return suma;
        //i zwracamy 
    }
}
    