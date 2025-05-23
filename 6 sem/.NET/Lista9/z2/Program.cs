using System;
using System.Threading;

class Program
{
    static Semaphore barberReady = new Semaphore(0, 1);
    static Semaphore customerReady = new Semaphore(0, 5);
    static Semaphore mutex = new Semaphore(1, 1);
    static int waiting = 0;

    static void Barber()
    {
        while (true)
        {
            customerReady.WaitOne(); // czeka
            mutex.WaitOne();
            waiting--;
            barberReady.Release(); // gotowy
            mutex.Release();
            Console.WriteLine("Barber is cutting hair");
            Thread.Sleep(1000);
        }
    }

    static void Customer(object id)
    {
        mutex.WaitOne();
        if (waiting < 5)
        {
            waiting++;
            customerReady.Release();
            mutex.Release();
            barberReady.WaitOne();
            Console.WriteLine($"Customer {id} is being served");
        }
        else
        {
            Console.WriteLine($"Customer {id} left (no space)");
            mutex.Release();
        }
    }

    static void Main()
    {
        new Thread(Barber).Start();
        for (int i = 0; i < 10; i++)
        {
            Thread.Sleep(500);
            new Thread(Customer).Start(i);
        }
    }
}
