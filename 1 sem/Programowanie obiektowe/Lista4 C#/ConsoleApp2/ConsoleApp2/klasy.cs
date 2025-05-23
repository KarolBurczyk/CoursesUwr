using System;

public class Wektor
{
    private static int liczbaWymiarow;
    
    private float[] wymiary = new float[liczbaWymiarow];

    public void DodajWektor(float[] tablica)
    {
        liczbaWymiarow = tablica.Length;
        wymiary = tablica;
    }
    public float[] zwrocWektor()
    {
        return wymiary;
    }

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

    public int zwrocRozmiar()
    {
        return liczbaWymiarow;
    }

    public static Wektor operator +(Wektor w1, Wektor w2)
    {
        if (w1.zwrocRozmiar() != w2.zwrocRozmiar())
        {
            Console.WriteLine("Nie mozna dodac wektorow o roznych rozmiarach");
            return w1;
        }
        else
        {
            Wektor w3 = new Wektor();
            float[] tablica = new float[w1.zwrocRozmiar()];
            for (int i = 0; i < w1.zwrocRozmiar(); i++)
            {
                tablica[i] = w1.zwrocWektor()[i] + w2.zwrocWektor()[i];
            }
            w3.DodajWektor(tablica);
            return w3;
        }
    }
    
    public static Wektor operator *(Wektor w1, Wektor w2)
    {
        if (w1.zwrocRozmiar() != w2.zwrocRozmiar())
        {
            Console.WriteLine("Nie mozna dodac wektorow o roznych rozmiarach");
            return w1;
        }
        else
        {
            Wektor w3 = new Wektor();
            float[] tablica = new float[w1.zwrocRozmiar()];
            for (int i = 0; i < w1.zwrocRozmiar(); i++)
            {
                tablica[i] = w1.zwrocWektor()[i] * w2.zwrocWektor()[i];
            }
            w3.DodajWektor(tablica);
            return w3;
        }
    }
    
    public static Wektor operator *(Wektor w1, float skalar)
    {
        Wektor w2 = new Wektor();
        float[] tablica = new float[w1.zwrocRozmiar()];
        for (int i = 0; i < w1.zwrocRozmiar(); i++)
        {
            tablica[i] = w1.zwrocWektor()[i] * skalar;
        }
        w2.DodajWektor(tablica);
        return w2;
    }

    public float norma()
    {
        Wektor w2 = new Wektor();
        w2.DodajWektor(wymiary);
        w2 *= w2;
        float[] tablica = w2.zwrocWektor();
        float suma = 0;
        for (int i = 0; i < w2.zwrocRozmiar(); i++)
        {
            suma += tablica[i];
        }
        suma = (float)Math.Sqrt(suma);
        return suma;
    }
}
    