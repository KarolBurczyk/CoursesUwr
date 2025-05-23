class DisposableExample : IDisposable
{
    public DisposableExample()
    {
        Console.WriteLine("DisposableExample: Konstruktor");
    }

    public void Dispose()
    {
        Console.WriteLine("DisposableExample: Dispose wywołane");
        GC.SuppressFinalize(this); // Zapobiega wywołaniu finalizatora
    }

    ~DisposableExample() // Finalizer na wypadek gdyby Dispose() nie został wywołany
    {
        Console.WriteLine("DisposableExample: Finalizer wywołany");
    }
}

class Program
{
    static void Main()
    {
        using (DisposableExample obj = new DisposableExample()) // Lukier syntaktyczny using
        {
            Console.WriteLine("Obiekt DisposableExample jest w użyciu");
        } // Dispose() wywołuje się automatycznie

        Console.WriteLine("Koniec Main");
    }
}

// W przypadku IDisposable mamy kontrolę nad dokładnym momentem wykonania, natomiast w finalizerze
// próba wymuszonego wywołania GC jest mocno niezalecana (działa asynchornicznie i obniża wydajność).
// Dzięki usingm Dispose wykonuje się bezpośrednio po zakończeniu bloku i nie musimy pamiętać o jego ręcznym wykonaniu.
