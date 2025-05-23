using System;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;

public class MainForm : Form
{
    private Button asyncButton = new Button { Text = "Pobierz Asynchronicznie", Top = 10, Width = 200 };
    private Button syncButton = new Button { Text = "Pobierz Synchronicznie", Top = 50, Width = 200 };
    private Label statusLabel = new Label { Top = 100, Width = 400 };

    public MainForm()
    {
        Controls.Add(asyncButton);
        Controls.Add(syncButton);
        Controls.Add(statusLabel);

        asyncButton.Click += async (sender, e) => await FetchAsync();
        syncButton.Click += (sender, e) => FetchSync();
    }

    private async Task FetchAsync()
    {
        statusLabel.Text = "Trwa asynchroniczne pobieranie...";
        using HttpClient client = new HttpClient();
        string content = await client.GetStringAsync("https://example.com");
        statusLabel.Text = $"Pobrano {content.Length} znaków asynchronicznie.";
    }

    private void FetchSync()
    {
        statusLabel.Text = "Trwa synchroniczne pobieranie...";
        using WebClient client = new WebClient();
        string content = client.DownloadString("https://example.com");
        statusLabel.Text = $"Pobrano {content.Length} znaków synchronicznie.";
    }

    [STAThread]
    public static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Application.Run(new MainForm());
    }
}
