class Program
{
    static void linq()
    {
        var liczby = File.ReadLines("text.txt").Select(int.Parse);

        var wynik = from liczba in liczby
                    where liczba > 100
                    orderby liczba descending
                    select liczba;

        foreach (var liczba in wynik)
        {
            Console.WriteLine(liczba);
        }
    }
    static void linq_to_objects()
    {
        var wynik = File.ReadLines("text.txt")
               .Select(int.Parse)
               .Where(liczba => liczba > 100) // musimy zastosować lambdę
               .OrderByDescending(liczba => liczba); // tak samo przy order by

        foreach (var liczba in wynik)
        {
            Console.WriteLine(liczba);
        }

    }
    static void Main()
    {
        linq();
        linq_to_objects();
    }
}