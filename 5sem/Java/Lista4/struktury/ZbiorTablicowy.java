package struktury;

public class ZbiorTablicowy implements Zbior, Cloneable {
    private Para[] zbior;
    private int zapelnienie;

    public ZbiorTablicowy(int rozmiar) {
        zbior = new Para[rozmiar];
        zapelnienie = 0;
    }

    @Override
    public Para szukaj(String klucz) {
        for (Para p : zbior) {
            if (p != null && p.klucz.equals(klucz)) return p;
        }
        return null;
    }

    @Override
    public void wstaw(Para para) {
        Para istniejaca = szukaj(para.klucz);
        if (istniejaca != null) {
            istniejaca.setWartosc(para.getWartosc());
        } else {
            if (zapelnienie >= zbior.length) throw new IllegalStateException("Array is full");
            zbior[zapelnienie++] = para;
        }
    }

    @Override
    public void usun(String klucz) {
        for (int i = 0; i < zapelnienie; i++) {
            if (zbior[i] != null && zbior[i].klucz.equals(klucz)) {
                zbior[i] = zbior[--zapelnienie];
                zbior[zapelnienie] = null;
                return;
            }
        }
    }

    @Override
    public void czysc() {
        zbior = new Para[zbior.length];
        zapelnienie = 0;
    }

    @Override
    public boolean pusty() {
        return zapelnienie == 0;
    }

    @Override
    public int ile() {
        return zapelnienie;
    }

    @Override
    public ZbiorTablicowy clone() {
        ZbiorTablicowy nowy = new ZbiorTablicowy(zbior.length);
        for (int i = 0; i < zapelnienie; i++) {
            nowy.wstaw(zbior[i].clone());
        }
        return nowy;
    }
}
