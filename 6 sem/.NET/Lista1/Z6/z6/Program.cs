using System;

namespace OverloadingDemo
{
    class BaseClass
    {
        public virtual void ShowMessage()
        {
            Console.WriteLine("Wiadomość z klasy bazowej");
        }
    }

    class DerivedClass : BaseClass
    {
        private string _name;
        private int _age;

        public void Display()
        {
            Console.WriteLine("Brak parametrów");
        }

        public void Display(int number)
        {
            Console.WriteLine($"Liczba: {number}");
        }

        public void Display(int number, string text)
        {
            Console.WriteLine($"Liczba: {number}, Tekst: {text}");
        }

        public void Display(string text)
        {
            Display(13, text);
        }

        public override void ShowMessage()
        {
            base.ShowMessage();
            Console.WriteLine("Dodatkowa wiadomość z klasy pochodnej");
        }

        public DerivedClass()
        {
            _name = "Anonim";
            _age = 0;
        }

        public DerivedClass(string name)
        {
            _name = name;
            _age = 0;
        }

        public DerivedClass(string name, int age) : this(name)
        {
            _age = age;
        }

        public void ShowInfo()
        {
            Console.WriteLine($"Imię: {_name}, Wiek: {_age}");
        }
    }

    class Program
    {
        static void Main()
        {
            DerivedClass obj = new DerivedClass();
            obj.Display();
            obj.Display(10);
            obj.Display(7, "Hello");
            obj.Display("Przykładowy tekst");

            Console.WriteLine("\n--- Wywołanie metody z klasy bazowej ---");
            obj.ShowMessage();

            Console.WriteLine("\n--- Testowanie przeciążonych konstruktorów ---");
            DerivedClass person1 = new DerivedClass();
            DerivedClass person2 = new DerivedClass("Jan");
            DerivedClass person3 = new DerivedClass("Anna", 25);

            person1.ShowInfo();
            person2.ShowInfo();
            person3.ShowInfo();
        }
    }
}
