using System;
using System.Threading;
using static System.Net.Mime.MediaTypeNames;
using Microsoft.VisualStudio.TestTools.UnitTesting;

public sealed class ProcessSingleton
{
    private static readonly Lazy<ProcessSingleton> _instance =
        new Lazy<ProcessSingleton>(() => new ProcessSingleton());

    private ProcessSingleton() { }

    public static ProcessSingleton Instance => _instance.Value;

    public Guid Id { get; } = Guid.NewGuid();
}

public sealed class ThreadSingleton
{
    [ThreadStatic]
    private static ThreadSingleton _instance;

    private ThreadSingleton() { }

    public static ThreadSingleton Instance
    {
        get
        {
            if (_instance == null)
                _instance = new ThreadSingleton();
            return _instance;
        }
    }

    public Guid Id { get; } = Guid.NewGuid();
}

public sealed class TimedSingleton
{
    private static TimedSingleton _instance;
    private static DateTime _validUntil = DateTime.MinValue;

    private TimedSingleton() { }

    public static TimedSingleton Instance
    {
        get
        {
            if (_instance == null || DateTime.Now >= _validUntil)
            {
                _instance = new TimedSingleton();
                _validUntil = DateTime.Now.AddSeconds(5);
            }
            return _instance;
        }
    }

    public Guid Id { get; } = Guid.NewGuid();
}

public class Tests
{
    public static void ProcessSingleton_SameInstance()
    {
        var a = ProcessSingleton.Instance;
        var b = ProcessSingleton.Instance;
        Console.WriteLine($"ProcessSingleton_SameInstance: a = {a}, b = {b}");
        try
        {
            Assert.AreSame(a, b, "Different instances.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void ProcessSingleton_SameId()
    {
        var a = ProcessSingleton.Instance.Id;
        var b = ProcessSingleton.Instance.Id;
        Console.WriteLine($"ProcessSingleton_SameId: a.Id = {a}, b.Id = {b}");
        try
        {
            Assert.AreEqual(a, b, "Different Ids.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void ProcessSingleton_SameInstanceAcrossThreads()
    {
        ProcessSingleton a = null, b = null;
        var t1 = new Thread(() => a = ProcessSingleton.Instance);
        var t2 = new Thread(() => b = ProcessSingleton.Instance);
        t1.Start(); t2.Start(); t1.Join(); t2.Join();
        Console.WriteLine($"ProcessSingleton_SameInstanceAcrossThreads: a = {a}, b = {b}");
        try
        {
            Assert.AreSame(a, b, "Instances from threads are different.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void ThreadSingleton_SameInSameThread()
    {
        var a = ThreadSingleton.Instance;
        var b = ThreadSingleton.Instance;
        Console.WriteLine($"ThreadSingleton_SameInSameThread: a = {a}, b = {b}");
        try
        {
            Assert.AreSame(a, b, "Should be same in same thread.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void ThreadSingleton_DifferentAcrossThreads()
    {
        ThreadSingleton a = null, b = null;
        var t1 = new Thread(() => a = ThreadSingleton.Instance);
        var t2 = new Thread(() => b = ThreadSingleton.Instance);
        t1.Start(); t2.Start(); t1.Join(); t2.Join();
        Console.WriteLine($"ThreadSingleton_DifferentAcrossThreads: a = {a}, b = {b}");
        try
        {
            Assert.AreNotSame(a, b, "Should be different in different threads.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void ThreadSingleton_DifferentIdsAcrossThreads()
    {
        Guid a = Guid.Empty, b = Guid.Empty;
        var t1 = new Thread(() => a = ThreadSingleton.Instance.Id);
        var t2 = new Thread(() => b = ThreadSingleton.Instance.Id);
        t1.Start(); t2.Start(); t1.Join(); t2.Join();
        Console.WriteLine($"ThreadSingleton_DifferentIdsAcrossThreads: a = {a}, b = {b}");
        try
        {
            Assert.AreNotEqual(a, b, "Ids should be different across threads.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void TimedSingleton_SameWithin5Seconds()
    {
        var a = TimedSingleton.Instance;
        Thread.Sleep(1000);
        var b = TimedSingleton.Instance;
        Console.WriteLine($"TimedSingleton_SameWithin5Seconds: a = {a}, b = {b}");
        try
        {
            Assert.AreSame(a, b, "Should be same within 5 seconds.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void TimedSingleton_DifferentAfter5Seconds()
    {
        var a = TimedSingleton.Instance;
        Thread.Sleep(6000);
        var b = TimedSingleton.Instance;
        Console.WriteLine($"TimedSingleton_DifferentAfter5Seconds: a = {a}, b = {b}");
        try
        {
            Assert.AreNotSame(a, b, "Should be different after 5 seconds.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    public static void TimedSingleton_DifferentIdAfter5Seconds()
    {
        var a = TimedSingleton.Instance.Id;
        Thread.Sleep(6000);
        var b = TimedSingleton.Instance.Id;
        Console.WriteLine($"TimedSingleton_DifferentIdAfter5Seconds: a = {a}, b = {b}");
        try
        {
            Assert.AreNotEqual(a, b, "Id should be different after 5 seconds.");
        }
        catch (AssertFailedException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}


class Program
{
    static void Main()
    {
        Tests tests = new Tests();
        Tests.ProcessSingleton_SameInstance();
        Tests.ProcessSingleton_SameId();
        Tests.ProcessSingleton_SameInstanceAcrossThreads();
        Tests.ThreadSingleton_SameInSameThread();
        Tests.ThreadSingleton_DifferentAcrossThreads();
        Tests.ThreadSingleton_DifferentIdsAcrossThreads();
        Tests.TimedSingleton_SameWithin5Seconds();
        Tests.TimedSingleton_DifferentAfter5Seconds();
        Tests.TimedSingleton_DifferentIdAfter5Seconds();
    }
}