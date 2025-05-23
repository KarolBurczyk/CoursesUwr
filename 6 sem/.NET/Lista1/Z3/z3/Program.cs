using System;

namespace TestProgram
{
    /// <summary>
    /// Delegat do obsługi zdarzeń, przekazuje komunikat tekstowy.
    /// </summary>
    /// <param name="message">Komunikat do wyświetlenia.</param>
    public delegate void TestDelegate(string message);

    /// <summary>
    /// Klasa demonstracyjna zawierająca przykłady zdarzeń, pętli, instrukcji warunkowych i switch.
    /// </summary>
    public class TestClass
    {
        /// <summary>
        /// Zdarzenie wywoływane, gdy coś się dzieje.
        /// </summary>
        public event TestDelegate TestEvent;

        private int _number;

        /// <summary>
        /// Właściwość przechowująca liczbę.
        /// </summary>
        public int Number
        {
            get { return _number; }
            set { _number = value; }
        }

        /// <summary>
        /// Indeksator zwracający wartość w postaci tekstowej na podstawie indeksu.
        /// </summary>
        /// <param name="index">Indeks w tablicy.</param>
        /// <returns>Łańcuch tekstowy zawierający numer indeksu.</returns>
        public string this[int index]
        {
            get { return $"Index {index}"; }
        }

        /// <summary>
        /// Wywołuje zdarzenie <see cref="TestEvent"/>.
        /// </summary>
        public void TriggerEvent()
        {
            TestEvent?.Invoke("Event triggered!");
        }

        /// <summary>
        /// Metoda demonstrująca działanie pętli for.
        /// </summary>
        public void Loop()
        {
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Loop iteration: {i}");
            }
        }

        /// <summary>
        /// Sprawdza wartość liczby i wyświetla odpowiedni komunikat.
        /// </summary>
        /// <param name="x">Liczba do sprawdzenia.</param>
        public void Condition(int x)
        {
            if (x > 0)
                Console.WriteLine("Positive");
            else if (x < 0)
                Console.WriteLine("Negative");
            else
                Console.WriteLine("Zero");
        }

        /// <summary>
        /// Wyświetla nazwę dnia tygodnia na podstawie przekazanej wartości.
        /// </summary>
        /// <param name="day">Numer dnia tygodnia.</param>
        public void Switch(int day)
        {
            switch (day)
            {
                case 1:
                    Console.WriteLine("Monday");
                    break;
                case 2:
                    Console.WriteLine("Tuesday");
                    break;
                default:
                    Console.WriteLine("Other day");
                    break;
            }
        }
    }

    /// <summary>
    /// Klasa zawierająca metodę główną programu.
    /// </summary>
    class Program
    {
        /// <summary>
        /// Metoda główna programu.
        /// </summary>
        static void Main()
        {
            TestClass obj = new TestClass();
            obj.TestEvent += msg => Console.WriteLine(msg);
            obj.TriggerEvent();
            obj.Loop();
            obj.Condition(-5);
            obj.Switch(1);
            Console.WriteLine(obj[2]);
        }
    }
}
