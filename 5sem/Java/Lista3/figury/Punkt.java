package figury;

public class Punkt {
    private double x;
    private double y;

    public Punkt(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    private static double round(double val, int zaokraglenie) {
        if (zaokraglenie < 0) throw new IllegalArgumentException();
        double skala = Math.pow(10, zaokraglenie);
        return Math.round(val * skala) / skala;
    }

    public void przesun(Wektor v) {
        this.x += v.dx;
        this.y += v.dy;
    }

    public void obroc(Punkt p, double kat) {
        double rad = Math.toRadians(kat);
        double xPrim = p.getX() + (this.x - p.getX()) * Math.cos(rad) - (this.y - p.getY()) * Math.sin(rad);
        double yPrim = p.getY() + (this.x - p.getX()) * Math.sin(rad) + (this.y - p.getY()) * Math.cos(rad);
        this.x = xPrim;
        this.y = yPrim;
    }

    public void odbij(Prosta p) {
        double d = (p.a * this.x + p.b * this.y + p.c) / (p.a * p.a + p.b * p.b);
        this.x = this.x - 2 * p.a * d;
        this.y = this.y - 2 * p.b * d;
    }

    @Override
    public String toString() {
        return "(" + round(x, 8) + ", " + round(y, 8) + ")";
    }
}
