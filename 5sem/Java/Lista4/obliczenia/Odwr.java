package obliczenia;

public class Odwr extends Oper1 {
    private Wyrazenie x;

    public Odwr(Wyrazenie x) {
        this.x = x;
    }

    @Override
    public double oblicz() {
        return 1/x.oblicz();
    }

    @Override
    public String toString() {
        return "1/" + x;
    }
}
