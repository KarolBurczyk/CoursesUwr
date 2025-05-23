using NLog;

class Program
{
    private static readonly Logger logger = LogManager.GetCurrentClassLogger();

    static void Main()
    {
        logger.Info("Aplikacja uruchomiona");
        logger.Warn("To jest ostrzeżenie");
        logger.Error("To jest błąd");
        logger.Info("Koniec działania aplikacji");

        Console.ReadLine();
    }
}

