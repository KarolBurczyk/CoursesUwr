using System;


public class MyDictionary
{
    private int[] values = new int[1];
    private string[] keys = new string[1];
    private int space = 0;

    public void setElement(string key, int value)
    {
        bool czy = false;
        for (int i = 0; i < keys.Length; i++)
        {
            if (keys[i] == key)
            {
                czy = true;
                break;
            }
        }

        if (czy == false)
        {
            values[space] = value;
            keys[space] = key;
            space++;
            Array.Resize(ref values, values.Length + 1);
            Array.Resize(ref keys, keys.Length + 1);
        }
        else
        {
            Console.WriteLine("Istnieje juz element o takim kluczu");
        }
    }

    public int searchElement(string key)
    {
        for (int i = 0; i < space; i++)
        {
            if (key == keys[i])
            {
                return values[i];
            }
        }
        Console.WriteLine("Nie ma wartosci dla podanego klucza");
        return 0;
    }

    public void popElement(string key)
    {
        int[] v1 = new int[values.Length-1];
        string[] k1 = new string[keys.Length-1];
        bool czy = false;
        for (int i = 0; i < space; i++)
        {
            if (keys[i] == key)
            {
                czy = true;
            }
            else
            {
                v1[i] = values[i];
                k1[i] = keys[i];
            }
        }
        
        if (czy)
        {
            values = v1;
            keys = k1;
            space--;
        }
    }
}