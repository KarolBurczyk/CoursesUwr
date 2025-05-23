using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        Func<int, int> recursion = null;
        recursion = (int i) =>
        {
            if (i > 2) return recursion(i - 1) + recursion(i - 2);
            else return 1;
        };

        List<int> list = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8};
        foreach (var item in list.Select(i => recursion(i)))
        {
            Console.WriteLine(item);
        }
    }
}