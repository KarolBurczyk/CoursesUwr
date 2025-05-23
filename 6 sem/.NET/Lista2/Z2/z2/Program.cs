class FinalizerExample
{
    public FinalizerExample()
    {
        Console.WriteLine("FinalizerExample: Konstruktor");
    }

    ~FinalizerExample() // Finalizer (destruktor)
    {
        Console.WriteLine("FinalizerExample: Finalizer wywołany przez GC");
    }
}

class Program
{
    static void Main()
    {
        FinalizerExample obj = new FinalizerExample();
        obj = null; // Obiekt gotowy do usunięcia przez GC

        GC.Collect();  // Próba wymuszenia GC (NIEZALECANE)
        GC.WaitForPendingFinalizers();

        Console.WriteLine("Koniec Main");
    }
}
