package obliczenia;

public class Przec extends Oper1 {
    private Wyrazenie x;

    public Przec(Wyrazenie x) {
        this.x = x;
    }

    @Override
    public double oblicz() {
        return -x.oblicz();
    }

    @Override
    public String toString() {
        return "-(" + x + ")";
    }
}
