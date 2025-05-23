using System;
using System.Linq;
using System.Text;

public static class StringExtensions
{
    public static bool IsPalindrome(this string str)
    {
        if (string.IsNullOrWhiteSpace(str)) return false;
        var normalized = new string(str.Where(char.IsLetterOrDigit).ToArray()).ToLower();

        return normalized.SequenceEqual(normalized.Reverse());
    }
}

class Program
{
    static void Main()
    {
        string s = "Kobyła ma mały bok.";
        bool isPalindrome = s.IsPalindrome();
        Console.WriteLine(isPalindrome); // Output: True
    }
}
