using System;
using System.ComponentModel;
using System.Threading;
using System.Windows.Forms;

namespace Task3_ProgressBar
{
    internal static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new MainForm());
        }
    }

    public class MainForm : Form
    {
        private ProgressBar progressBar;
        private Button startAsyncButton;
        private Button startThreadButton;
        private BackgroundWorker worker;

        public MainForm()
        {
            Text = "Task 3 – ProgressBar with Threads";
            Size = new System.Drawing.Size(400, 200);

            progressBar = new ProgressBar { Location = new(30, 30), Width = 300 };
            startAsyncButton = new Button { Text = "Start (BackgroundWorker)", Location = new(30, 70) };
            startThreadButton = new Button { Text = "Start (Thread)", Location = new(200, 70) };

            startAsyncButton.Click += StartWithBackgroundWorker;
            startThreadButton.Click += StartWithThread;

            Controls.Add(progressBar);
            Controls.Add(startAsyncButton);
            Controls.Add(startThreadButton);

            worker = new BackgroundWorker
            {
                WorkerReportsProgress = true
            };
            worker.DoWork += Worker_DoWork;
            worker.ProgressChanged += Worker_ProgressChanged;
        }

        private void StartWithBackgroundWorker(object sender, EventArgs e)
        {
            if (!worker.IsBusy)
            {
                progressBar.Value = 0;
                worker.RunWorkerAsync();
            }
        }

        private void Worker_DoWork(object sender, DoWorkEventArgs e)
        {
            for (int i = 1; i <= 100; i++)
            {
                Thread.Sleep(50);
                worker.ReportProgress(i);
            }
        }

        private void Worker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            progressBar.Value = e.ProgressPercentage;
        }

        private void StartWithThread(object sender, EventArgs e)
        {
            progressBar.Value = 0;
            new Thread(() =>
            {
                for (int i = 1; i <= 100; i++)
                {
                    Thread.Sleep(50);
                    Invoke(new Action(() => progressBar.Value = i));
                }
            }).Start();
        }
    }
}
