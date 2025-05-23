using System.Net.Http;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

public static class AwaitableUrl
{
    private static readonly HttpClient _client = new HttpClient();

    public static TaskAwaiter<string> GetAwaiter(this string url)
    {
        return _client.GetStringAsync(url).GetAwaiter();
    }
}

public class Program
{
    public static async Task Main()
    {
        string content = await "https://www.google.com";
        Console.WriteLine(content.Substring(0, 200));
    }
}
