using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        string folderPath = @"C:\Users\burcz\Desktop\STUDIA\6 sem\.NET\Lista4\Z4\z4";

        if (Directory.Exists(folderPath))
        {
            long totalSize = Directory.GetFiles(folderPath)
                                      .Select(file => new FileInfo(file).Length)
                                      .Aggregate(0L, (sum, fileSize) => sum + fileSize);

            Console.WriteLine($"Łączna wielkość plików: {totalSize} bajtów");
        }
        else
        {
            Console.WriteLine("Podany folder nie istnieje");
        }
    }
}
