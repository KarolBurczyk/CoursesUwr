package obliczenia;

public class Mnoz extends Oper2 {
    private Wyrazenie lewe;
    private Wyrazenie prawe;

    public Mnoz(Wyrazenie lewe, Wyrazenie prawe) {
        this.lewe = lewe;
        this.prawe = prawe;
    }

    @Override
    public double oblicz() {
        return lewe.oblicz() * prawe.oblicz();
    }

    @Override
    public String toString() {
        if (lewe == null || lewe.getClass().getName().equals("obliczenia.Dod") || lewe.getClass().getName().equals("obliczenia.Odejm")) {
            if (prawe == null || prawe.getClass().getName().equals("obliczenia.Dod") || prawe.getClass().getName().equals("obliczenia.Odejm")) {
                return "(" + lewe + ") * (" + prawe + ")";
            }
            return "(" + lewe + ") * " + prawe;
        }
        if (prawe == null || prawe.getClass().getName().equals("obliczenia.Dod") || prawe.getClass().getName().equals("obliczenia.Odejm")) {
            return lewe + " * (" + prawe + ")";
        }
        return lewe + " * " + prawe;
    }
}
