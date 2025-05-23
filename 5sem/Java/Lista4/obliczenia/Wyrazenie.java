package obliczenia;

abstract public class Wyrazenie implements Obliczalny {
    public static double suma(Wyrazenie... wyrazenia) {
        double wynik = 0;
        for (Wyrazenie wyr : wyrazenia) {
            wynik += wyr.oblicz();
        }
        return wynik;
    }

    public static double iloczyn(Wyrazenie... wyrazenia) {
        double wynik = 1;
        for (Wyrazenie wyr : wyrazenia) {
            wynik *= wyr.oblicz();
        }
        return wynik;
    }
}
