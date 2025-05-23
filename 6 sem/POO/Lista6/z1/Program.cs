public interface ILogger
{
    void Log(string message);
}

public enum LogType { None, Console, File }

public class ConsoleLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine($"[Console] {message}");
    }
}

public class FileLogger : ILogger
{
    private readonly string _filePath;

    public FileLogger(string filePath)
    {
        _filePath = filePath;
    }

    public void Log(string message)
    {
        File.AppendAllText(_filePath, $"[File] {message}\n");
    }
}

public class NullLogger : ILogger
{
    public void Log(string message)
    {
        // nic nie robi
    }
}

public class LoggerFactory
{
    private static readonly LoggerFactory _instance = new LoggerFactory();
    public static LoggerFactory Instance => _instance;

    private LoggerFactory() { }

    public ILogger GetLogger(LogType logType, string parameters = null)
    {
        return logType switch
        {
            LogType.Console => new ConsoleLogger(),
            LogType.File => new FileLogger(parameters),
            _ => new NullLogger()
        };
    }
}

public class Program
{
    static void Main()
    {
        // klient:
        ILogger logger1 = LoggerFactory.Instance.GetLogger(LogType.File, "C:\\Users\\burcz\\Desktop\\STUDIA\\6 sem\\POO\\Lista6\\z1\\bin\\Debug\\net8.0\\foo.txt");
        logger1.Log("foo bar");

        ILogger logger2 = LoggerFactory.Instance.GetLogger(LogType.None);
        logger2.Log("qux");

        ILogger logger3 = LoggerFactory.Instance.GetLogger(LogType.Console);
        logger3.Log("foo bar");
    }
}


