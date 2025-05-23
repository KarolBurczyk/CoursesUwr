package obliczenia;

public class Exp extends Fun1{
    private Wyrazenie x;

    public Exp(Wyrazenie x) {
        this.x = x;
    }

    @Override
    public double oblicz() {
        return Math.exp(x.oblicz());
    }

    @Override
    public String toString() {
        return "Exp(" + x + ")";
    }
}
