package obliczenia;

public class Ln extends Fun1{
    private Wyrazenie x;

    public Ln(Wyrazenie x) {
        this.x = x;
    }

    @Override
    public double oblicz() {
        return Math.log(x.oblicz());
    }

    @Override
    public String toString() {
        return "Ln(" + x + ")";
    }
}
