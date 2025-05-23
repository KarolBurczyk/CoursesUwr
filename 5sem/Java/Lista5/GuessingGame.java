import java.io.*;
import java.util.*;
import java.util.logging.*;

public class GuessingGame {

    private static final Logger logger = Logger.getLogger("GuessingGame");
    private static final int MIN_N = 3;
    private static final int MAX_N = 9;

    public static void main(String[] args) {
        configureLogging();

        Scanner scanner = new Scanner(System.in);
        System.out.println("Wybierz poziom trudnosci od 3 do 9:");

        int n = getValidInput(scanner, MIN_N, MAX_N);
        GameState game = new GameState(n);

        logger.info("Wybrany poziom trudnosci N=" + n);

        while (true) {
            if (game.isGameOver()) {
                System.out.println("Przekroczyes maksymalna liczbe prob. Koniec gry!");
                logger.info("Koniec gry - przekroczono liczbe prob.");
                break;
            }

            System.out.println("Zgadnij permutacje (oddziel liczby spacjami):");
            try {
                List<Integer> guess = parseGuess(scanner.nextLine(), n);
                game.incrementAttempts();

                boolean success = game.evaluateGuess(guess);
                if (success) {
                    System.out.println("Gratulacje! Zgadles prawidlowa permutacje!");
                    logger.info("Poprawna permutacja.");
                    break;
                } else {
                    int incorrectPositions = game.getIncorrectPositionsCount(guess);
                    String hint = game.getHint(guess);
                    System.out.println("Bledne pozycje: " + incorrectPositions);
                    System.out.println("Podpowiedz: " + hint);
                }
            } catch (InvalidInputException e) {
                System.out.println(e.getMessage());
                logger.warning("Niepoprawne dane wejsciowe: " + e.getMessage());
            }
        }

        logger.info("Koniec gry");
        game.logHistory();
        scanner.close();
    }

    private static int getValidInput(Scanner scanner, int min, int max) {
        while (true) {
            try {
                int input = Integer.parseInt(scanner.nextLine());
                if (input >= min && input <= max) {
                    return input;
                } else {
                    System.out.println("Podaj liczbe z zakresu od " + min + " do " + max);
                }
            } catch (NumberFormatException e) {
                System.out.println("To nie jest liczba, sprobuj ponownie");
            }
        }
    }

    private static List<Integer> parseGuess(String input, int n) throws InvalidInputException {
        String[] parts = input.trim().split("\\s+");
        if (parts.length != n) {
            throw new InvalidInputException("Niepoprawna liczba elementow, oczekiwano " + n + " liczb");
        }

        List<Integer> guess = new ArrayList<>();
        for (String part : parts) {
            try {
                int number = Integer.parseInt(part);
                if (number < 1 || number > n) {
                    throw new InvalidInputException("Liczby musza byc z zakresu 1 do " + n);
                }
                if (guess.contains(number)) {
                    throw new InvalidInputException("Nie mozna powtarzac liczb w ciagu");
                }
                guess.add(number);
            } catch (NumberFormatException e) {
                throw new InvalidInputException("Wprowadzone dane musza byc liczbami");
            }
        }
        return guess;
    }

    private static void configureLogging() {
        try {
            LogManager.getLogManager().readConfiguration(new FileInputStream("logging.properties"));
        } catch (IOException e) {
            System.err.println("Nie udalo sie zaladowac konfiguracji logowania");
        }
    }
}

class GameState {
    private final int n;
    private final List<Integer> permutation;
    private final int maxAttempts;
    private int attempts;
    private final List<String> history;

    public GameState(int n) {
        this.n = n;
        this.permutation = generatePermutation(n);
        this.maxAttempts = n * n;
        this.attempts = 0;
        this.history = new ArrayList<>();
    }

    private List<Integer> generatePermutation(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            list.add(i);
        }
        Collections.shuffle(list);
        return list;
    }

    public boolean evaluateGuess(List<Integer> guess) {
        boolean success = permutation.equals(guess);
        history.add("Proba: " + guess + ", wynik: " + (success ? "trafiona" : "nietrafiona"));
        return success;
    }

    public int getIncorrectPositionsCount(List<Integer> guess) {
        int incorrectCount = 0;
        for (int i = 0; i < n; i++) {
            if (!guess.get(i).equals(permutation.get(i))) {
                incorrectCount++;
            }
        }
        return incorrectCount;
    }

    public String getHint(List<Integer> guess) {
        List<Integer> incorrectIndices = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!guess.get(i).equals(permutation.get(i))) {
                incorrectIndices.add(i);
            }
        }
    
        if (incorrectIndices.isEmpty()) {
            return "Brak podpowiedzi";
        }
    
        Random random = new Random();
        int randomIncorrectIndex = incorrectIndices.get(random.nextInt(incorrectIndices.size()));
    
        int incorrectNumber = guess.get(randomIncorrectIndex);
        int actualIndex = permutation.indexOf(incorrectNumber);
    
        return "Liczba " + incorrectNumber + " powinna znajdowac sie "
                + (actualIndex < randomIncorrectIndex ? "bardziej w lewo" : "bardziej w prawo");
    }
    

    public void incrementAttempts() {
        attempts++;
        assert attempts <= maxAttempts : "Przekroczono maksymalna liczbe prob";
    }

    public boolean isGameOver() {
        return attempts >= maxAttempts;
    }

    public void logHistory() {
        history.forEach(Logger.getLogger(GuessingGame.class.getName())::info);
    }
}

class InvalidInputException extends Exception {
    public InvalidInputException(String message) {
        super(message);
    }
}
