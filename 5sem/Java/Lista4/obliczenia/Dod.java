package obliczenia;

public class Dod extends Oper2 {
    private Wyrazenie lewe;
    private Wyrazenie prawe;

    public Dod(Wyrazenie lewe, Wyrazenie prawe) {
        this.lewe = lewe;
        this.prawe = prawe;
    }

    @Override
    public double oblicz() {
        return lewe.oblicz() + prawe.oblicz();
    }

    @Override
    public String toString() {
        return lewe + " + " + prawe;
    }
}
