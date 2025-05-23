using System;
using System.Collections.Generic;

public class Reusable
{
    public void DoWork()
    {
        Console.WriteLine("Working...");
    }
}

public sealed class ObjectPool
{
    private readonly int _poolSize;
    private readonly List<Reusable> _pool = new List<Reusable>();
    private readonly List<Reusable> _acquired = new List<Reusable>();

    public ObjectPool(int poolSize)
    {
        if (poolSize <= 0)
        {
            throw new ArgumentException("Rozmiar puli musi być dodatni.");
        }
        _poolSize = poolSize;
    }

    public Reusable AcquireReusable()
    {
        if (_acquired.Count == _poolSize)
        {
            throw new ArgumentException("Brak wolnych zasobów w puli.");
        }

        if (_pool.Count == 0)
        {
            var reusable = new Reusable();
            _pool.Add(reusable);
        }

        var element = _pool[0];
        _pool.RemoveAt(0);
        _acquired.Add(element);
        return element;
    }

    public void ReleaseReusable(Reusable reusable)
    {
        if (!_acquired.Contains(reusable))
        {
            throw new ArgumentException("Zasób nie pochodzi z tej puli.");
        }

        _acquired.Remove(reusable);
        _pool.Add(reusable);
    }
}

public class BetterReusableForTest
{
    private readonly ObjectPool _pool;
    private Reusable _reusable;
    private bool _isReleased = false;

    public BetterReusableForTest(ObjectPool pool)
    {
        _pool = pool;
        _reusable = _pool.AcquireReusable();
    }

    public Reusable InnerReusable => _reusable;

    public void Release()
    {
        if (_isReleased)
        {
            throw new InvalidOperationException("Już zwolniony.");
        }
        _pool.ReleaseReusable(_reusable);
        _isReleased = true;
    }

    public void DoWork()
    {
        if (_isReleased)
        {
            throw new InvalidOperationException("Obiekt został zwolniony, nie można użyć.");
        }
        _reusable.DoWork();
    }
}

public class Tests
{
    public static void InvalidSize()
    {
        Console.Write("InvalidSize: ");
        try
        {
            var pool = new ObjectPool(0);
            Console.WriteLine("FAILED (Expected exception but none was thrown)");
        }
        catch (ArgumentException)
        {
            Console.WriteLine("PASSED");
        }
    }

    public static void ValidSize()
    {
        Console.Write("ValidSize: ");
        var tempPool = new ObjectPool(2);
        var br = new BetterReusableForTest(tempPool);
        Console.WriteLine(br != null ? "PASSED" : "FAILED");
    }

    public static void CapacityDepleted()
    {
        Console.Write("CapacityDepleted: ");
        var tempPool = new ObjectPool(1);
        var br1 = new BetterReusableForTest(tempPool);

        try
        {
            var br2 = new BetterReusableForTest(tempPool);
            Console.WriteLine("FAILED (Expected exception but none was thrown)");
        }
        catch (ArgumentException)
        {
            Console.WriteLine("PASSED");
        }
    }

    public static void ReusedInstance()
    {
        Console.Write("ReusedInstance: ");
        var tempPool = new ObjectPool(1);
        var br1 = new BetterReusableForTest(tempPool);
        var firstReusable = br1.InnerReusable;
        br1.Release();

        var br2 = new BetterReusableForTest(tempPool);
        var secondReusable = br2.InnerReusable;

        Console.WriteLine(firstReusable == secondReusable ? "PASSED" : "FAILED");
    }

    public static void ReleaseInvalidInstance()
    {
        Console.Write("ReleaseInvalidInstance: ");
        var tempPool = new ObjectPool(1);
        var alienReusable = new Reusable();

        try
        {
            tempPool.ReleaseReusable(alienReusable);
            Console.WriteLine("FAILED (Expected exception but none was thrown)");
        }
        catch (ArgumentException)
        {
            Console.WriteLine("PASSED");
        }
    }

    public static void DoWorkAfterReleaseShouldThrow()
    {
        Console.Write("DoWorkAfterReleaseShouldThrow: ");
        var tempPool = new ObjectPool(1);
        var br = new BetterReusableForTest(tempPool);
        br.Release();

        try
        {
            br.DoWork();
            Console.WriteLine("FAILED (Expected exception but none was thrown)");
        }
        catch (InvalidOperationException)
        {
            Console.WriteLine("PASSED");
        }
    }
}

class Program
{
    static void Main()
    {
        Tests.InvalidSize();
        Tests.ValidSize();
        Tests.CapacityDepleted();
        Tests.ReusedInstance();
        Tests.ReleaseInvalidInstance();
        Tests.DoWorkAfterReleaseShouldThrow();
    }
}
