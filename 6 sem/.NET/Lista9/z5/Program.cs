using System;
using System.Diagnostics;
using System.ServiceProcess;
using System.Timers;
using System.IO;

public partial class AppLoggerService : ServiceBase
{
    private System.Timers.Timer timer;
    private string logPath = @"C:\AppLogs\running_apps.txt";

    public AppLoggerService()
    {
        this.ServiceName = "AppLoggerService";
    }

    protected override void OnStart(string[] args)
    {
        Directory.CreateDirectory(Path.GetDirectoryName(logPath));
        timer = new System.Timers.Timer();
        timer.Interval = 60000; // 1 minuta
        timer.Elapsed += new ElapsedEventHandler(OnElapsedTime);
        timer.Start();
    }

    private void OnElapsedTime(object source, ElapsedEventArgs e)
    {
        try
        {
            using (StreamWriter writer = new StreamWriter(logPath, true))
            {
                writer.WriteLine($"[{DateTime.Now}] Running Applications:");
                foreach (Process p in Process.GetProcesses())
                {
                    if (!string.IsNullOrEmpty(p.MainWindowTitle))
                    {
                        writer.WriteLine($" - {p.ProcessName} : {p.MainWindowTitle}");
                    }
                }
                writer.WriteLine(); // pusty wiersz
            }
        }
        catch (Exception ex)
        {
            File.AppendAllText(logPath, $"[{DateTime.Now}] Error: {ex.Message}\n");
        }
    }

    protected override void OnStop()
    {
        timer.Stop();
    }
}
