package obliczenia;

public class Pot extends Fun2{
    private Wyrazenie podstawa;
    private Wyrazenie wykladnik;

    public Pot(Wyrazenie podstawa, Wyrazenie wykladnik) {
        this.podstawa = podstawa;
        this.wykladnik = wykladnik;
    }

    @Override
    public double oblicz() {
        return Math.pow(podstawa.oblicz(), wykladnik.oblicz());
    }

    @Override
    public String toString() {
        return "Pow" + "(" + podstawa + ", " + wykladnik + ")";
    }
}
