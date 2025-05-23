package struktury;

public class Para implements Cloneable, Comparable<Para> {
    public final String klucz;
    private double wartosc;

    public Para(String klucz, double wartosc) {
        if (klucz == null || !klucz.matches("[a-z]+")) {
            throw new IllegalArgumentException("Invalid key format.");
        }
        this.klucz = klucz;
        this.wartosc = wartosc;
    }

    public double getWartosc() {
        return wartosc;
    }

    public void setWartosc(double wartosc) {
        this.wartosc = wartosc;
    }

    @Override
    public String toString() {
        return klucz + " = " + wartosc;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj instanceof Para other) {
            return this.klucz.equals(other.klucz);
        }
        return false;
    }

    @Override
    public int compareTo(Para p) {
        return this.klucz.compareTo(p.klucz);
    }

    @Override
    public Para clone() {
        return new Para(this.klucz, this.wartosc);
    }
}
