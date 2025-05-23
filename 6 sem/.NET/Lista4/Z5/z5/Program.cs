using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        var daneOsobowe = File.ReadLines("osoby.txt")
                              .Select(line => line.Split(' ', StringSplitOptions.RemoveEmptyEntries))
                              .Where(parts => parts.Length == 3)
                              .Select(parts => new
                              {
                                  Imie = parts[0],
                                  Nazwisko = parts[1],
                                  Pesel = parts[2]
                              });

        var numeryKont = File.ReadLines("konta.txt")
                             .Select(line => line.Split(' ', StringSplitOptions.RemoveEmptyEntries))
                             .Where(parts => parts.Length == 2)
                             .Select(parts => new
                             {
                                 Pesel = parts[0],
                                 NumerKonta = parts[1]
                             });

        var wynik = from osoba in daneOsobowe
                    join konto in numeryKont on osoba.Pesel equals konto.Pesel
                    select new
                    {
                        osoba.Imie,
                        osoba.Nazwisko,
                        osoba.Pesel,
                        konto.NumerKonta
                    };

        foreach (var rekord in wynik)
        {
            Console.WriteLine($"{rekord.Imie} {rekord.Nazwisko} ({rekord.Pesel}) -> {rekord.NumerKonta}");
        }
    }
}
