package obliczenia;

public class Cos extends Fun1{
    private Wyrazenie x;

    public Cos(Wyrazenie x) {
        this.x = x;
    }

    @Override
    public double oblicz() {
        return Math.cos(x.oblicz());
    }

    @Override
    public String toString() {
        return "Cos(" + x + ")";
    }
}
