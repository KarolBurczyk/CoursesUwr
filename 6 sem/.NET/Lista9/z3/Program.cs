using System;
using System.Net;
using System.Net.Http;
using System.Net.Mail;
using System.Net.Sockets;
using System.Threading.Tasks;

class Program {
    static async Task Main() {
        // HttpClient
        using var httpClient = new HttpClient();
        string result = await httpClient.GetStringAsync("http://example.com");
        Console.WriteLine("HttpClient async done");

        // HttpWebRequest
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create("http://example.com");
        using var response = (HttpWebResponse)await request.GetResponseAsync();
        Console.WriteLine("HttpWebRequest done");

        // TcpClient
        TcpClient tcpClient = new TcpClient();
        await tcpClient.ConnectAsync("example.com", 80);
        Console.WriteLine("TCP connected");

        // TcpListener
        TcpListener listener = new TcpListener(System.Net.IPAddress.Any, 12345);
        listener.Start();
        _ = listener.AcceptTcpClientAsync();

        // HttpListener
        HttpListener httpListener = new HttpListener();
        httpListener.Prefixes.Add("http://localhost:8080/");
        httpListener.Start();
        _ = httpListener.GetContextAsync();

    }
}
