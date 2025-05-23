using System;

public class Person
{
    private string _name;
    private string _surname;

    public event Action<object, string, object> PropertyValueChanged;

    public event Action<string> NameChanged;
    public event Action<string> SurnameChanged;

    public string Name
    {
        get => _name;
        set
        {
            if (_name != value)
            {
                _name = value;
                PropertyValueChanged?.Invoke(this, nameof(Name), value);
                NameChanged?.Invoke(value);
            }
        }
    }

    public string Surname
    {
        get => _surname;
        set
        {
            if (_surname != value)
            {
                _surname = value;
                PropertyValueChanged?.Invoke(this, nameof(Surname), value);
                SurnameChanged?.Invoke(value);
            }
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Person person = new Person();

        // Subskrypcja ogólnego zdarzenia
        person.PropertyValueChanged += Person_PropertyValueChanged;

        // Subskrypcja specyficznych zdarzeń dla poszczególnych właściwości
        person.NameChanged += name => Console.WriteLine($"[NameChanged] Nowe imię: {name}");
        person.SurnameChanged += surname => Console.WriteLine($"[SurnameChanged] Nowe nazwisko: {surname}");

        // Zmiana wartości właściwości (powoduje wywołanie zdarzeń)
        person.Name = "Jan";
        person.Surname = "Kowalski";
        person.Name = "Jan"; // Nie zmieni się, więc nie wywoła zdarzenia
        person.Name = "Adam"; // Zmieni się, więc wywoła zdarzenie

    }

    private static void Person_PropertyValueChanged(object source, string propertyName, object propertyValue)
    {
        Console.WriteLine($"[PropertyValueChanged] {propertyName} zmienione na: {propertyValue}");
    }
}
