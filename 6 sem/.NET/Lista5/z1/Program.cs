using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

public class Benchmarks
{
    private int a = 5;
    private int b = 10;
    private dynamic da = 5;
    private dynamic db = 10;

    [Benchmark]
    public int DoWork1() => a + b;

    [Benchmark]
    public dynamic DoWork2() => da + db;
}

public class Program
{
    public static void Main(string[] args)
    {
        BenchmarkRunner.Run<Benchmarks>();
    }
}
