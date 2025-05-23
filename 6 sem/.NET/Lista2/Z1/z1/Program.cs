using System;

// 1. Static class - nie można tworzyć obiektu, ale można wywoływać metody
static class Utils
{
    public static void PrintMessage(string message)
    {
        Console.WriteLine(message);
    }
}

// 2. Static field i method - można wywołać metody albo odwołać się do pola
class ExampleStatic
{
    public static int Counter = 0;
    public static void Increment() => Counter++;
}

// 3. Sealed class - nie można dziedziczyć po tej klasie
sealed class FinalClass
{
    public void Show() => Console.WriteLine("Sealed class method");
}

// 4. Abstract class - nie można tworzyć obiektu, klasa powinna być odziedziczona
// 5. Abstract method - metody muszą być nadpisane w klasie pochodnej
abstract class AbstractBase
{
    public abstract void AbstractMethod();
}

class Derived : AbstractBase
{
    public override void AbstractMethod()
    {
        Console.WriteLine("Implemented abstract method");
    }
}

// 6. Virtual - zezwala na nadpisanie metody w klasie dziedziczącej za pomocą override
class BaseClass
{
    public virtual void Show() => Console.WriteLine("Base class method");
}

class DerivedClass : BaseClass
{
    public override void Show() => Console.WriteLine("Overridden method");
}

// 7. Partial class - podzielenie deklarowania klasy 
partial class PartialExample
{
    public void MethodOne() => Console.WriteLine("Partial class - method one");
}

partial class PartialExample
{
    public void MethodTwo() => Console.WriteLine("Partial class - method two");
}

// 8. Readonly field - taka zmienna może być zmieniona tylko przy jej deklarowaniu albo w konstruktorze klasy 
class ReadonlyExample
{
    public readonly int Number;
    public ReadonlyExample(int num) => Number = num;
}

// 9. in, ref, out
class ParameterModifiers
{
    public void Modify(ref int number) => number *= 2; // number może być zmodyfikowany
    public void ReadOnly(in int number) => Console.WriteLine(number); // number nie może być zmodyfikowany
    public void Output(out int number) => number = 42; // number musi być zmodyfikowany 
}

// 10. Params parameter - pozwala przekazać dowolną liczbę argumentów
class ParamsExample
{
    public void PrintValues(params int[] numbers)
    {
        foreach (var num in numbers) Console.Write(num + " ");
        Console.WriteLine();
    }
}

class Program
{
    static void Main()
    {
        // Static class
        Utils.PrintMessage("Hello from static class");

        // Static fields and methods
        ExampleStatic.Increment();
        Console.WriteLine("Counter: " + ExampleStatic.Counter);

        // Sealed class
        FinalClass fc = new();
        fc.Show();

        // Abstract class
        Derived derived = new();
        derived.AbstractMethod();

        // Virtual and override
        BaseClass baseObj = new DerivedClass();
        baseObj.Show();

        // Partial class
        PartialExample pe = new();
        pe.MethodOne();
        pe.MethodTwo();

        // Readonly field
        ReadonlyExample re = new(10);
        Console.WriteLine("Readonly value: " + re.Number);

        // Parameter modifiers
        ParameterModifiers pm = new();
        int val = 10;
        pm.Modify(ref val);
        Console.WriteLine("Modified: " + val);
        pm.ReadOnly(val);
        pm.Output(out val);
        Console.WriteLine("Output: " + val);

        // Params
        ParamsExample paramEx = new();
        paramEx.PrintValues(1, 2, 3, 4, 5);
    }
}
