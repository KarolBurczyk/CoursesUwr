package figury;

public class Trojkat {
    private Punkt p1;
    private Punkt p2;
    private Punkt p3;

    public Trojkat(Punkt p1, Punkt p2, Punkt p3) {
        if (Math.abs(p1.getX() - p2.getX()) <= Math.pow(10, -8) && Math.abs(p1.getY() - p2.getY()) <= Math.pow(10, -8)) {
            throw new IllegalArgumentException("Punkty muszą być różne.");
        }
        if (Math.abs(p2.getX() - p3.getX()) <= Math.pow(10, -8) && Math.abs(p2.getY() - p3.getY()) <= Math.pow(10, -8)) {
            throw new IllegalArgumentException("Punkty muszą być różne.");
        }
        if (Math.abs(p1.getX() - p3.getX()) <= Math.pow(10, -8) && Math.abs(p1.getY() - p3.getY()) <= Math.pow(10, -8)) {
            throw new IllegalArgumentException("Punkty muszą być różne.");
        }
        if (czyWspolliniowe(p1, p2, p3)) {
            throw new IllegalArgumentException("Punkty nie mogą być współliniowe.");
        }
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }

    private boolean czyWspolliniowe(Punkt p1, Punkt p2, Punkt p3) {
        return Math.abs((p2.getY() - p1.getY()) * (p3.getX() - p1.getX()) - (p3.getY() - p1.getY()) * (p2.getX() - p1.getX())) <= Math.pow(10, -8);
    }

    public void przesun(Wektor v) {
        p1.przesun(v);
        p2.przesun(v);
        p3.przesun(v);
    }

    public void obroc(Punkt p, double kat) {
        p1.obroc(p, kat);
        p2.obroc(p, kat);
        p3.obroc(p, kat);
    }

    public void odbij(Prosta p) {
        p1.odbij(p);
        p2.odbij(p);
        p3.odbij(p);
    }

    @Override
    public String toString() {
        return "Trojkat [" + p1 + ", " + p2 + ", " + p3 + "]";
    }
}
