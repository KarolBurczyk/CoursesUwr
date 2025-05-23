package obliczenia;

public class Sin extends Fun1{
    private Wyrazenie x;

    public Sin(Wyrazenie x) {
        this.x = x;
    }

    @Override
    public double oblicz() {
        return Math.sin(x.oblicz());
    }

    @Override
    public String toString() {
        return "Sin(" + x + ")";
    }
}
