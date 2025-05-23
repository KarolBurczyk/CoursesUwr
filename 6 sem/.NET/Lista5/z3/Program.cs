using System;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

public static class IntAwaiter
{
    public static TaskAwaiter GetAwaiter(this int milliseconds)
    {
        return Task.Delay(milliseconds).GetAwaiter();
    }
}

public class Program
{
    public static async Task Main()
    {
        Console.WriteLine("1");
        await 2000;
        Console.WriteLine("2");
    }
}
