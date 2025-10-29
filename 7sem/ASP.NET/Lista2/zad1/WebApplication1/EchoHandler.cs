using System;
using System.IO;
using System.Text;
using System.Web;

public class EchoHandler : IHttpHandler
{
    public void ProcessRequest(HttpContext context)
    {
        var req = context.Request;
        var res = context.Response;

        res.ContentType = "text/html; charset=utf-8";

        var sb = new StringBuilder();
        sb.Append("<!DOCTYPE html><html><head><meta charset='utf-8'><title>Echo</title>");
        sb.Append("<style>body{font-family:sans-serif;margin:20px}pre{white-space:pre-wrap;word-break:break-word}</style>");
        sb.Append("</head><body>");
        sb.Append("<h2>Echo ¿¹dania</h2>");

        // Pe³ny adres i metoda
        sb.AppendFormat("<p><strong>URL:</strong> {0}</p>",
            HttpUtility.HtmlEncode(req.Url.ToString()));
        sb.AppendFormat("<p><strong>Method:</strong> {0}</p>",
            HttpUtility.HtmlEncode(req.HttpMethod));

        // Nag³ówki
        sb.Append("<h3>Nag³ówki</h3><ul>");
        foreach (var key in req.Headers.AllKeys)
        {
            sb.AppendFormat("<li>{0}: {1}</li>",
                HttpUtility.HtmlEncode(key),
                HttpUtility.HtmlEncode(req.Headers[key]));
        }
        sb.Append("</ul>");

        // Body tylko dla POST/PUT/PATCH itp., jeœli jest zawartoœæ
        if (!string.IsNullOrEmpty(req.HttpMethod) &&
            (string.Equals(req.HttpMethod, "POST", StringComparison.OrdinalIgnoreCase) ||
             string.Equals(req.HttpMethod, "PUT", StringComparison.OrdinalIgnoreCase) ||
             string.Equals(req.HttpMethod, "PATCH", StringComparison.OrdinalIgnoreCase)))
        {
            if (req.ContentLength > 0 && req.InputStream != null)
            {
                try
                {
                    // Przewiñ wstecz na wszelki wypadek
                    if (req.InputStream.CanSeek) req.InputStream.Position = 0;

                    using (var reader = new StreamReader(req.InputStream, req.ContentEncoding ?? Encoding.UTF8, true, 1024, true))
                    {
                        var body = reader.ReadToEnd();
                        if (!string.IsNullOrEmpty(body))
                        {
                            sb.Append("<h3>Body</h3>");
                            sb.AppendFormat("<pre>{0}</pre>", HttpUtility.HtmlEncode(body));
                        }
                        else
                        {
                            sb.Append("<h3>Body</h3><p>(puste)</p>");
                        }
                    }
                }
                catch (Exception ex)
                {
                    sb.AppendFormat("<h3>Body</h3><p>B³¹d odczytu: {0}</p>",
                        HttpUtility.HtmlEncode(ex.Message));
                }
            }
            else
            {
                sb.Append("<h3>Body</h3><p>(brak treœci)</p>");
            }
        }

        sb.Append("</body></html>");
        res.Write(sb.ToString());
    }

    public bool IsReusable => false;
}
