using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Threading;
using System.Collections.Concurrent;

public interface ITask
{
    void Run();
}

public class FileService
{
    public void FetchFromFtp(string sourceUrl, string destinationPath)
    {
        new WebClient().DownloadFile(sourceUrl, destinationPath);
        Console.WriteLine($"[FTP] Downloaded {sourceUrl} → {destinationPath}");
    }

    public void FetchFromHttp(string sourceUrl, string destinationPath)
    {
        var content = new HttpClient().GetByteArrayAsync(sourceUrl).Result;
        File.WriteAllBytes(destinationPath, content);
        Console.WriteLine($"[HTTP] Downloaded {sourceUrl} → {destinationPath}");
    }

    public void GenerateFile(string filePath, int byteCount)
    {
        var buffer = new byte[byteCount];
        new Random().NextBytes(buffer);
        File.WriteAllBytes(filePath, buffer);
        Console.WriteLine($"[RANDOM] Created {filePath} ({byteCount} bytes)");
    }

    public void DuplicateFile(string sourcePath, string targetPath)
    {
        File.Copy(sourcePath, targetPath, true);
        Console.WriteLine($"[COPY] {sourcePath} → {targetPath}");
    }
}

public class FtpTask : ITask
{
    string url, destination; FileService service;
    public FtpTask(FileService service, string url, string destination) => (this.service, this.url, this.destination) = (service, url, destination);
    public void Run() => service.FetchFromFtp(url, destination);
}

public class HttpTask : ITask
{
    string url, destination; FileService service;
    public HttpTask(FileService service, string url, string destination) => (this.service, this.url, this.destination) = (service, url, destination);
    public void Run() => service.FetchFromHttp(url, destination);
}

public class RandomFileTask : ITask
{
    string filePath; int size; FileService service;
    public RandomFileTask(FileService service, string filePath, int size) => (this.service, this.filePath, this.size) = (service, filePath, size);
    public void Run() => service.GenerateFile(filePath, size);
}

public class CopyTask : ITask
{
    string source, target; FileService service;
    public CopyTask(FileService service, string source, string target) => (this.service, this.source, this.target) = (service, source, target);
    public void Run() => service.DuplicateFile(source, target);
}

public class TaskQueue
{
    private readonly BlockingCollection<ITask> _tasks = new();

    public void AddTask(ITask task) => _tasks.Add(task);

    public void LaunchWorkers(int threadCount = 2)
    {
        for (int i = 0; i < threadCount; i++)
        {
            new Thread(() =>
            {
                foreach (var task in _tasks.GetConsumingEnumerable())
                {
                    try { task.Run(); } catch (Exception ex) { Console.WriteLine($"[ERROR] {ex.Message}"); }
                }
            })
            { IsBackground = true }.Start();
        }
    }

    public void Complete() => _tasks.CompleteAdding();
}

public class App
{
    static void Main()
    {
        var fileOps = new FileService();
        var queue = new TaskQueue();
        queue.LaunchWorkers();

        queue.AddTask(new RandomFileTask(fileOps, "file.bin", 512));
        queue.AddTask(new CopyTask(fileOps, "file.bin", "file_copy.bin"));
        queue.AddTask(new HttpTask(fileOps, "https://example.com", "download.html"));

        Thread.Sleep(3000);
        queue.Complete();
    }
}
