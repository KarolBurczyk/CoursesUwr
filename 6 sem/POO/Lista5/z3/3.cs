﻿using System.Collections;

class Program
{
    static int IntComparer(int x, int y)
    {
        return x.CompareTo(y);
    }

    class ComparisonComparer<T> : IComparer
    {
        private readonly Comparison<T> _comparison;

        public ComparisonComparer(Comparison<T> comparison)
        {
            _comparison = comparison;
        }

        public int Compare(object x, object y)
        {
            return _comparison((T)x, (T)y);
        }
    }

    static void Main(string[] args)
    {
        ArrayList a = new ArrayList() { 1, 5, 3, 3, 2, 4, 3 };

        a.Sort(new ComparisonComparer<int>(IntComparer));

        foreach (var item in a)
        {
            Console.Write(item + " ");
        }

        Console.ReadLine();
    }
}
