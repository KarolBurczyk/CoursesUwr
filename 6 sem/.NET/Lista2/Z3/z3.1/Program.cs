using System;

class Person
{
    private string _name; // Pole kopii zapasowej

    public string Name
    {
        get { return _name; } // Zwracanie wartości pola
        set { _name = value; }
    }
}

class Program
{
    static void Main()
    {
        Person person = new Person();
        person.Name = "Adam"; // Ustawienie wartości przez setter
        Console.WriteLine(person.Name); // Odczyt przez getter

        person.Name = ""; // Próba ustawienia pustej wartości (zostanie odrzucona)
    }
}
