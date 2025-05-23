public interface IService
{
    string GetData();
}

public class RealService : IService
{
    public string GetData()
    {
        Console.WriteLine("Getting data...");
        return "Data";
    }
}

public class RetryProxy : IService
{
    private readonly IService _service;
    private readonly int _maxRetries;

    public RetryProxy(IService service, int maxRetries = 3)
    {
        _service = service;
        _maxRetries = maxRetries;
    }

    public string GetData()
    {
        int attempts = 0;
        while (true)
        {
            try
            {
                return _service.GetData();
            }
            catch
            {
                attempts++;
                if (attempts >= _maxRetries)
                    throw;
            }
        }
    }
}

public class LoggingProxy : IService
{
    private readonly IService _service;

    public LoggingProxy(IService service)
    {
        _service = service;
    }
    public string GetData()
    {
        Console.WriteLine($"[{DateTime.Now}] Calling GetData()");

        try
        {
            var result = _service.GetData();
            Console.WriteLine($"[{DateTime.Now}] Returned: {result}");
            return result;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[{DateTime.Now}] Exception occurred: {ex.Message}");
            return "ERROR";
        }
    }
}

public static class ServiceFactory
{
    public static IService CreateServiceWithRetryAndLogging()
    {
        IService retry = new RetryProxy(new LoggingProxy(new RealService()));
        return retry;
    }
}

public class Program
{
    static void Main()
    {
        ServiceFactory.CreateServiceWithRetryAndLogging().GetData();
    }
}
