package obliczenia;

import struktury.Para;
import struktury.ZbiorTablicowy;

public class Zmienna extends Wyrazenie {
    private final String nazwa;
    private static final ZbiorTablicowy zbiorZmiennych = new ZbiorTablicowy(100);

    public Zmienna(String nazwa) {
        if (nazwa == null || nazwa.isEmpty()) {
            throw new IllegalArgumentException("Nazwa zmiennej nie może być pusta");
        }
        this.nazwa = nazwa;
    }

    public static void ustawZmienna(String nazwa, double wartosc) {
        Para para = new Para(nazwa, wartosc);
        zbiorZmiennych.wstaw(para);
    }

    public static double pobierzWartosc(String nazwa) {
        Para para = zbiorZmiennych.szukaj(nazwa);
        if (para == null) {
            throw new IllegalArgumentException("Zmienna o nazwie " + nazwa + " nie została zdefiniowana");
        }
        return para.getWartosc();
    }

    @Override
    public double oblicz() {
        return pobierzWartosc(this.nazwa);
    }

    @Override
    public String toString() {
        return this.nazwa;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Zmienna zmienna = (Zmienna) obj;
        return nazwa.equals(zmienna.nazwa);
    }
}
