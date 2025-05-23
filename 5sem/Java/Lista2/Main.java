public class Main {
    public static void main(String[] args) {
        long startTime = System.nanoTime();

        if (args.length == 0) {
            System.err.println("Podaj liczby do rozkladu na czynniki pierwsze.");
            return;
        }

        for (String arg : args) {
            try {
                long liczba = Long.parseLong(arg);
                long[] czynniki = LiczbyPierwsze.naCzynnikiPierwsze(liczba);
                wypiszRozklad(liczba, czynniki);
            } catch (NumberFormatException e) {
                System.err.println("Niepoprawny format liczby: " + arg);
            }
        }

        long endTime = System.nanoTime();
        long runtime = endTime - startTime;
        
        System.out.println("Czas wykonania programu: " + (runtime/1000000) + " ms");
    }

    public static void wypiszRozklad(long liczba, long[] czynniki) {
        StringBuilder wynik = new StringBuilder();
        wynik.append(liczba).append(" = ");
        for (int i = 0; i < czynniki.length; i++) {
            wynik.append(czynniki[i]);
            if (i < czynniki.length - 1) {
                wynik.append(" * ");
            }
        }
        System.out.println(wynik.toString());
    }
}
