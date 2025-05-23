using System;

public class tester2
{
    public static void Main(string[] args)
    {
        MyDictionary d1 = new MyDictionary();
        d1.setElement("a", 1);
        d1.setElement("b", 2);
        d1.setElement("c", 3);
        d1.popElement("c");
        d1.setElement("c", 4);
        Console.WriteLine(d1.searchElement("c"));
    }
}