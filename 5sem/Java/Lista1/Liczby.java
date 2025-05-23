public class Liczby {
    static String[] jednosci = {
        null, "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem",
        "osiem", "dziewięć"
    };
    static String[] nastki = {
        null, "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście",
        "osiemnaście", "dziewiętnaście"
    };
    static String[] dziesiatki = {
        "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt",
        "osiemdziesiąt", "dziewięćdziesiąt"
    };
    static String[] setki = {
        null, "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset",
        "osiemset", "dziewięćset"
    };
    static String[] mnoznik_1 = {
        "", "miliard", "milion", "tysiąc"
    };
    static String[] mnoznik_2 = {
        "", "miliardy", "miliony", "tysiące"
    };
    static String[] mnoznik_3 = {
        "", "miliardów", "milionów", "tysięcy"
    };
    
    public static String liczba(int akt_tysiac, int t) {
        StringBuilder res = new StringBuilder(100);
        if (akt_tysiac == 1 && t < 3) {
            res.append("");
            return res.toString();
        }
        else if (akt_tysiac > 99)
            res.append(setki[akt_tysiac / 100]).append(" ");
        akt_tysiac = akt_tysiac % 100;
        if (akt_tysiac > 0 && akt_tysiac < 10)
            res.append(jednosci[akt_tysiac]).append(" ");
        else if (akt_tysiac > 10 && akt_tysiac < 20)
            res.append(nastki[akt_tysiac - 10]).append(" ");
        else if (akt_tysiac % 10 == 0 && akt_tysiac != 0)
            res.append(dziesiatki[akt_tysiac / 10 - 1]).append(" ");
        else if (akt_tysiac > 20 && akt_tysiac < 100)
            res.append(dziesiatki[akt_tysiac / 10 - 1]).append(" ").append(jednosci[akt_tysiac % 10]).append(" ");
        return res.toString();
    };

    public static String odmiana(int akt_tysiac, int t) {
        StringBuilder res = new StringBuilder(100);
        if (t < 3) {
            if(akt_tysiac % 10 == 1 && akt_tysiac / 10 == 0) {
                res.append(mnoznik_1[++t]).append(" ");
            }
            else if(akt_tysiac % 10 < 5 && akt_tysiac % 10 > 1 && akt_tysiac / 10 % 10 != 1){
                res.append(mnoznik_2[++t]).append(" ");
            }
            else {
                res.append(mnoznik_3[++t]).append(" ");
            }
        }
        return res.toString();
    };

    public static String konwerter(int n) {
        StringBuilder res = new StringBuilder(100);
        if(n == 0) {
            res.append("zero");
            return res.toString(); 
        }
        if(n == -2147483648) {
            res.append("minus dwa miliardy sto czterdzieści siedem milionów czterysta osiemdziesiąt trzy tysiące sześćset czterdzieści osiem");
            return res.toString(); 
        }
        if(n < 0) {
            res.append("minus ");
            n = n * -1;
        }
    
        int t = 0, akt_tysiac, limit = 1000000000;
        
        for (int i = limit; i > 0; i /= 1000) {
            akt_tysiac = n / i;
            if (akt_tysiac > 0) {
                res.append(liczba(akt_tysiac, t));
                res.append(odmiana(akt_tysiac, t));
            }
            n %= i;
            t++;
        }
    
        return res.toString().trim();
    }
    

    public static void main(String[] args) {
        for (String arg : args) {
            try {
                int liczba = Integer.parseInt(arg);
                String res = konwerter(liczba);
                System.out.println(res);
            } catch (NumberFormatException e) {
                System.out.println(arg + "jest nieprawidłową liczbą.");
            }
        }
    }
}
