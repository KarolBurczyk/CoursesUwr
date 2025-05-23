import java.io.Serializable;

public class Ksiazka implements Serializable {
    //klasa bazowa Ksiazka implementująca interfejs Serializable
    protected String tytul;
    protected String autor;
    protected String gatunek;
    //posiada 3 chronione zmienne
    public Ksiazka(String t, String a, String g)
    {
        tytul = t;
        autor = a;
        gatunek = g;
        //konstruktor przypisuje zmiennym wartości argumentów konstruktora
    }
    public String toString()
    {
        return (tytul + " to książka napisana przez " + autor +
            " należy do gatunku " + gatunek);
        //metoda toString zwraca łańcuch znaków opisujący dany obiekt
    }
}

class WydawnictwoCiagle extends Ksiazka
    //klasa dziedzicząca po klasie bazowej
{
    protected int rokWydania;
    //posiada jedną zmienną
    public WydawnictwoCiagle(String t, String a, String g, int r)
    {
        //konstruktor klasy
        super(t, a, g);
        //dla 3 pierwszych argumentów wywołujemy konstruktor klasy bazowej
        rokWydania = r;
        //wartość ostatniego argumentu przypisujemy pod zmienną tej klasy
    }
    @Override
    public String toString()
    {
        //nadpisanie metody toString zwracającej podobną zwartość, poszerzoną o
        //czwartą zmienną
        return (tytul + " to książka napisana przez " + autor +
           " należy do gatunku " + gatunek + " wyadana w roku " + rokWydania);
    }
}

class Czasopismo extends Ksiazka
    //kolejna klasa dziedzicząca, analogiczna do poprzedniej ze zmienioną
    //nazwą czwartej zmiennej
{
    protected int numerMagazynu;
    public Czasopismo(String t, String a, String g, int n)
    {
        super(t, a, g);
        numerMagazynu = n;
    }
    @Override
    public String toString()
    {
        return (tytul + " to książka napisana przez " + autor +
           " należy do gatunku " + gatunek + " o numerze: " + numerMagazynu);
    }
}

