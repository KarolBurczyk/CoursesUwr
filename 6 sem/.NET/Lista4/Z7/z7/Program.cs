class Program

{
    public class MyItem
    {
        public string Field1 { get; set; }
        public int Field2 { get; set; }
    }

    static void Alt()
    {
        

        var item = new MyItem { Field1 = "The value", Field2 = 5 };
        List<MyItem> theList = new List<MyItem>();

        theList.Add(item);

        Console.WriteLine(theList[0].Field1);
        Console.WriteLine(theList[0].Field2);

    }

    static void Main()
    {
        var item = new { Field1 = "The value", Field2 = 5 };

        List<object> theList = new List<object>();

        theList.Add(item);

        var firstItem = (dynamic)theList[0]; // dynamiczne rzutowanie, żeby mieć dostęp do tego elementu
        Console.WriteLine(firstItem.Field1);
        Console.WriteLine(firstItem.Field2);

        Alt();

    }
}