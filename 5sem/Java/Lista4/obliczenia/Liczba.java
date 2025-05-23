package obliczenia;

public class Liczba extends Operand {
    private final double wartosc;

    public Liczba(double wartosc) {
        this.wartosc = wartosc;
    }

    @Override
    public double oblicz() {
        return wartosc;
    }

    @Override
    public String toString() {
        return String.valueOf(wartosc);
    }
}