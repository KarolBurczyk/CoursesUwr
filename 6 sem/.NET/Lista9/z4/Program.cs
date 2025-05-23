using System;
using System.Globalization;
using System.Threading;
using System.Windows.Forms;

class Program
{
    [STAThread]
    static void Main()
    {
        string[] cultures = { "en-US", "de-DE", "fr-FR", "ru-RU", "ar-SA", "cs-CZ", "pl-PL" };
        string output = "";

        foreach (var c in cultures)
        {
            CultureInfo ci = new CultureInfo(c);
            output += $"[{ci.DisplayName}]\n";
            output += "Months: " + string.Join(", ", ci.DateTimeFormat.MonthNames[..12]) + "\n";
            output += "Days: " + string.Join(", ", ci.DateTimeFormat.DayNames) + "\n";
            output += "Now: " + DateTime.Now.ToString(ci) + "\n\n";
        }

        MessageBox.Show(output);
    }
}
