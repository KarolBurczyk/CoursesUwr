class Program
{
    static void Main()
    {
        var pierwszeLitery = File.ReadLines("nazwiska.txt")
                         .Where(nazwisko => !string.IsNullOrWhiteSpace(nazwisko))
                         .GroupBy(nazwisko => nazwisko[0])
                         .OrderBy(grupa => grupa.Key)
                         .Select(grupa => grupa.Key);

        foreach (var litera in pierwszeLitery)
        {
            Console.WriteLine(litera);
        }

    }
}