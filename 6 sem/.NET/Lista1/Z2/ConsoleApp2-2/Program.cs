
using Library1;
using Library2;

Console.WriteLine("ConsoleApp2-1: Sprawdzanie pojedynczej liczby.");
        
Console.Write("Podaj liczbę: ");
if (int.TryParse(Console.ReadLine(), out int number))
{
    bool isValid = ParityChecker.IsEvenNumber(number/2);
    int tmp = 0;
    Console.WriteLine($"Liczba {number} podzielona przez 2 {(isValid ? "jest" : "nie jest")} parzysta, a podniesiona do 4 potęgi wytnosi {NumberSquared.SquareNumber(NumberSquared.SquareNumber(number))}.");
}
else
{
    Console.WriteLine("Niepoprawna liczba.");
}

Console.WriteLine("\nNaciśnij dowolny klawisz, aby zakończyć.");
Console.ReadKey();