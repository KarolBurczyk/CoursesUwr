using System;
using System.IO;
using System.IO.Compression;
using System.Security.Cryptography;
using System.Text;

class Program
{
    static void Main()
    {
        string inputPath = "input.txt";
        string outputPath = "output.enc";

        
        using (FileStream fs = new FileStream(outputPath, FileMode.Create))
        using (Aes aes = Aes.Create())
        {
            byte[] key = aes.Key;
            byte[] iv = aes.IV;

            fs.Write(key, 0, key.Length);
            fs.Write(iv, 0, iv.Length);

            using (CryptoStream cryptoStream = new CryptoStream(fs, aes.CreateEncryptor(), CryptoStreamMode.Write))
            using (GZipStream gzip = new GZipStream(cryptoStream, CompressionMode.Compress))
            using (StreamWriter writer = new StreamWriter(gzip))
            {
                writer.Write(File.ReadAllText(inputPath));
            }
        }

        
        using (FileStream fs = new FileStream(outputPath, FileMode.Open))
        {
            byte[] key = new byte[32];
            byte[] iv = new byte[16];
            fs.Read(key, 0, 32);
            fs.Read(iv, 0, 16);

            using (Aes aes = Aes.Create())
            using (CryptoStream cryptoStream = new CryptoStream(fs, aes.CreateDecryptor(key, iv), CryptoStreamMode.Read))
            using (GZipStream gzip = new GZipStream(cryptoStream, CompressionMode.Decompress))
            using (StreamReader reader = new StreamReader(gzip))
            {
                string decrypted = reader.ReadToEnd();
                Console.WriteLine(decrypted);
            }
        }


        using (BinaryWriter bw = new BinaryWriter(File.Open("bin.dat", FileMode.Create)))
            bw.Write(1234);
        using (BinaryReader br = new BinaryReader(File.Open("bin.dat", FileMode.Open)))
            Console.WriteLine(br.ReadInt32());


        StringBuilder sb = new StringBuilder();
        using (StringWriter sw = new StringWriter(sb))
            sw.WriteLine("Hello from StringWriter");
        Console.WriteLine(sb.ToString());
    }
}
