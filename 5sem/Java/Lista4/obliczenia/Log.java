package obliczenia;

public class Log extends Fun2{
    private Wyrazenie podstawa;
    private Wyrazenie x;

    public Log(Wyrazenie x, Wyrazenie podstawa) {
        this.x = x;
        this.podstawa = podstawa;
    }

    @Override
    public double oblicz() {
        return Math.log(x.oblicz()) / Math.log(podstawa.oblicz());
    }

    @Override
    public String toString() {
        return "Log" + podstawa + "(" + x + ")";
    }
}
