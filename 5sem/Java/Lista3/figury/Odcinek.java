package figury;

public class Odcinek {
    private Punkt p1;
    private Punkt p2;

    public Odcinek(Punkt p1, Punkt p2) {
        if (Math.abs(p1.getX() - p2.getX()) <= Math.pow(10, -8) && Math.abs(p1.getY() - p2.getY()) <= Math.pow(10, -8)) {
            throw new IllegalArgumentException("Punkty nie mogą być takie same.");
        }
        this.p1 = p1;
        this.p2 = p2;
    }

    public void przesun(Wektor v) {
        p1.przesun(v);
        p2.przesun(v);
    }

    public void obroc(Punkt p, double kat) {
        p1.obroc(p, kat);
        p2.obroc(p, kat);
    }

    public void odbij(Prosta p) {
        p1.odbij(p);
        p2.odbij(p);
    }

    @Override
    public String toString() {
        return "Odcinek [" + p1 + ", " + p2 + "]";
    }
}
