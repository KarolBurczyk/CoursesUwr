using System.Net;
using System.Net.Mail;

public class SmtpFacade
{
    public void Send(string from, string to, string subject, string body, Stream attachment, string attachmentMimeType)
    {
        var message = new MailMessage(from, to, subject, body);

        if (attachment != null)
        {
            var attachmentData = new Attachment(attachment, "attachment", attachmentMimeType);
            message.Attachments.Add(attachmentData);
        }

        using (var smtp = new SmtpClient("smtp.example.com"))
        {
            smtp.Credentials = new NetworkCredential("user", "password");
            smtp.Send(message);
        }
    }
}