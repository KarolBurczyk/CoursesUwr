public class main
{
    static void Main(string[] args)
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
        numbers.ConvertAll(x => x * 3).ForEach(Console.WriteLine);
        numbers.FindAll(x => x % 2 == 0).ForEach(Console.WriteLine);
        numbers.ForEach(x => Console.WriteLine(x + " "));
        numbers.RemoveAll(x => x > 3);
        numbers.ForEach(x => Console.WriteLine(x + " "));
        numbers.Sort((a, b) => b - a);
        numbers.ForEach(x => Console.WriteLine(x + " "));
    }
}