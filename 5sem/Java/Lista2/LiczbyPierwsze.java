
import java.util.ArrayList;
import java.util.List;

public final class LiczbyPierwsze {

    private final static int POTEGA2 = 21;
    private final static int[] SITO = new int[1 << POTEGA2];
    private final static long MAX_LICZBA_SITO = 1L << POTEGA2;

    static {
        for (int i = 2; i < SITO.length; i++) {
            SITO[i] = i;
        }
        for (int i = 2; i * i < SITO.length; i++) {
            if (SITO[i] == i) {
                for (int j = 2 * i; j < SITO.length; j += i) {
                    if (SITO[j] == j) {
                        SITO[j] = i;
                    }
                }  
            }
        }
    }

    public static boolean czyPierwsza(long n) {
        if (n < 2) return false;
        if (n < MAX_LICZBA_SITO) return SITO[(int) n] == n;
        if (n % 2 == 0) return false;
        for (long i = 3; i * i <= n; i+=2) {
            if (n % i == 0) return false;
        }
        
        return true;
    }
    
    public static long[] naCzynnikiPierwsze(long n) {
        if (n == 0) return new long[]{0};
        if (n == 1) return new long[]{1};
        if (n == -1) return new long[]{-1};

        List<Long> czynniki = new ArrayList<>();
        
        if (n == Long.MIN_VALUE) {
            czynniki.add(-1L);
            n /= 2;
            czynniki.add(2L);
            n = -n;
        }

        if (n < 0) {
            czynniki.add(-1L);
            n = -n;
        }

        if(n < SITO.length && czyPierwsza(n)) {
            czynniki.add(n);
            return czynniki.stream().mapToLong(Long::longValue).toArray();
        }

        for (long i = 2; i * i <= n && n > 1; i++) {
            while (n % i == 0) {
                czynniki.add(i);
                n /= i;
            }
        }

        if (n > 1) {
            czynniki.add(n);
        }

        return czynniki.stream().mapToLong(Long::longValue).toArray();
    }
}