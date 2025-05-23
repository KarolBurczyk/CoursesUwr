public static class ListHelper
{
    public static List<TOutput> ConvertAll<T, TOutput>(List<T> list, Converter<T, TOutput> converter)
    {
        List<TOutput> result = new List<TOutput>();
        foreach (var item in list)
            result.Add(converter(item));
        return result;
    }

    public static List<T> FindAll<T>(List<T> list, Predicate<T> match)
    {
        List<T> result = new List<T>();
        foreach (var item in list)
            if (match(item)) result.Add(item);
        return result;
    }

    public static void ForEach<T>(List<T> list, Action<T> action)
    {
        foreach (var item in list)
            action(item);
    }

    public static int RemoveAll<T>(List<T> list, Predicate<T> match)
    {
        int count = 0;
        for (int i = list.Count - 1; i >= 0; i--)
        {
            if (match(list[i]))
            {
                list.RemoveAt(i);
                count++;
            }
        }
        return count;
    }

    public static void Sort<T>(List<T> list, Comparison<T> comparison)
    {
        for (int i = 0; i < list.Count - 1; i++)
        {
            for (int j = i + 1; j < list.Count; j++)
            {
                if (comparison(list[i], list[j]) > 0)
                {
                    (list[i], list[j]) = (list[j], list[i]);
                }
            }
        }
    }
}

public class main
{
    static void Main(string[] args)
    {
        List<int> exampleList = new List<int> { 1, 2, 3, 4, 5 };

        List<string> convertedList = ListHelper.ConvertAll(exampleList, x => $"Number {x}");
        List<int> foundItems = ListHelper.FindAll(exampleList, x => x % 2 == 0);
        ListHelper.ForEach(exampleList, x => Console.Write(x + " "));
        int removedCount = ListHelper.RemoveAll(exampleList, x => x > 3);
        ListHelper.Sort(exampleList, (a, b) => b - a);

        // Wyświetlenie wyników
        Console.WriteLine("\nConverted List:");
        convertedList.ForEach(Console.WriteLine);
        Console.WriteLine("\nFound Items:");
        foundItems.ForEach(Console.WriteLine);
        Console.WriteLine("\nList after RemoveAll:");
        exampleList.ForEach(Console.WriteLine);
        Console.WriteLine("\nSorted List:");
        exampleList.ForEach(Console.WriteLine);
    }
}