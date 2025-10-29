using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class _default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string path = @"C:\Users\burcz\Desktop\test_server.txt";
            try
            {
                string result;
                using (var sr = new System.IO.StreamReader(path))
                {
                    result = sr.ReadToEnd();
                }
                Response.Write($"Plik odczytany: {result}");
            }
            catch (Exception ex)
            {
                Response.Write($"Błąd: {ex.Message}");
            }
        }
    }
}