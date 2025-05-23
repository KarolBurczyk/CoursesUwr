using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        var logi = File.ReadLines("log.txt")
                       .Select(line => line.Split(' ', StringSplitOptions.RemoveEmptyEntries))
                       .Where(parts => parts.Length >= 4)
                       .Select(parts => parts[1])
                       .GroupBy(ip => ip)
                       .Select(group => new
                       {
                           IP = group.Key,
                           LiczbaZadan = group.Count()
                       })
                       .OrderByDescending(entry => entry.LiczbaZadan)
                       .Take(3);

        foreach (var entry in logi)
        {
            Console.WriteLine($"{entry.IP} {entry.LiczbaZadan}");
        }
    }
}
