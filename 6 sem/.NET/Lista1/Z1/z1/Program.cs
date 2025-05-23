class Program
{
    static void Main()
    {
        List<int> result = new List<int>();

        for (int i = 1; i <= 100000; i++)
        {
            if (IsValidNumber(i))
            {
                result.Add(i);
            }
        }

        Console.WriteLine(string.Join(", ", result));
    }

    static bool IsValidNumber(int number)
    {
        int sumOfDigits = 0;
        int temp = number;

        while (temp > 0)
        {
            int digit = temp % 10;

            if (digit == 0 || number % digit != 0)
            {
                return false;
            }

            sumOfDigits += digit;
            temp /= 10;
        }

        return number % sumOfDigits == 0;
    }
}
