// Auto-Implemented Properties

class Car
{
    public string Model { get; set; } // Automatyczna właściwość
}

class Program
{
    static void Main()
    {
        Car car = new Car();
        car.Model = "Tesla Model S"; // Ustawienie wartości
        Console.WriteLine(car.Model); // Odczyt wartości
    }
}
