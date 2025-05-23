package figury;

public class Prosta {
    public final double a;
    public final double b;
    public final double c;

    public Prosta(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public static Prosta przesun(Prosta p, Wektor v) {
        return new Prosta(p.a, p.b, p.c - p.a * v.dx - p.b * v.dy);
    }

    public static boolean czyRownolegle(Prosta p1, Prosta p2) {
        return Math.abs(p1.a * p2.b - p1.b * p2.a) <= Math.pow(10, -8);
    }

    public static boolean czyProstopadle(Prosta p1, Prosta p2) {
        return Math.abs(p1.a * p2.a + p1.b * p2.b) <= Math.pow(10, -8);
    }

    public static Punkt punktPrzeciecia(Prosta p1, Prosta p2) {
        if (czyRownolegle(p1, p2)) {
            return null;
        }
        
        double x = (p1.b * p2.c - p2.b * p1.c) / (p1.a * p2.b - p2.a * p1.b);
        double y = (p2.a * p1.c - p1.a * p2.c) / (p1.a * p2.b - p2.a * p1.b);

        return new Punkt(x, y);
    }

    @Override
    public String toString() {
        return "Prosta: " + a + "x + " + b + "y + " + c + " = 0";
    }
}
