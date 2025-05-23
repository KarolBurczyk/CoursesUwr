
using Library1;
using Library2;

Console.WriteLine("ConsoleApp2-1: Sprawdzanie pojedynczej liczby.");
        
Console.Write("Podaj liczbę: ");
if (int.TryParse(Console.ReadLine(), out int number))
{
    bool isValid = ParityChecker.IsEvenNumber(number);
    Console.WriteLine($"Liczba {number} {(isValid ? "jest" : "nie jest")} parzysta, a jej kwadrat to {NumberSquared.SquareNumber(number)}.");
}
else
{
    Console.WriteLine("Niepoprawna liczba.");
}

Console.WriteLine("\nNaciśnij dowolny klawisz, aby zakończyć.");
Console.ReadKey();