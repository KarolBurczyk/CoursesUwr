using System;
using System.Windows.Forms;

namespace ModalExample
{
    public partial class ModalForm : Form
    {
        public string Imie { get; private set; }

        private TextBox txtImie;
        private Button btnOK;

        public ModalForm(string imieZGlownego)
        {
            this.Text = "Okno modalne";
            this.Width = 400;
            this.Height = 200;

            Label lbl = new Label { Text = "Imiê:", Left = 10, Top = 20, Width = 30 };
            txtImie = new TextBox { Left = 70, Top = 18, Width = 200};
            txtImie.Text = imieZGlownego;

            btnOK = new Button { Text = "Otwórz okno G³ówne", Left = 60, Top = 60, Width = 150 };
            btnOK.Click += (s, e) => {
                Imie = txtImie.Text;
                this.DialogResult = DialogResult.OK;
                this.Close();
            };

            this.Controls.AddRange(new Control[] { lbl, txtImie, btnOK });
        }
    }

    public class MainForm : Form
    {
        private TextBox txtNazwa;
        private Button btnOtworzModalne;

        public MainForm()
        {
            this.Text = "G³ówne okno";
            this.Width = 400;
            this.Height = 200;

            Label lbl = new Label { Text = "Imiê:", Left = 10, Top = 20, Width = 30};
            txtNazwa = new TextBox { Left = 70, Top = 18, Width = 200, Text = "Jan" };

            btnOtworzModalne = new Button { Text = "Otwórz okno modalne", Left = 60, Top = 60 , Width = 150};
            btnOtworzModalne.Click += BtnOtworzModalne_Click;

            this.Controls.AddRange(new Control[] { lbl, txtNazwa, btnOtworzModalne });
        }

        private void BtnOtworzModalne_Click(object sender, EventArgs e)
        {
            ModalForm modal = new ModalForm(txtNazwa.Text);
            if (modal.ShowDialog() == DialogResult.OK)
            {
                txtNazwa.Text = modal.Imie;
            }
        }

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new MainForm());
        }
    }
}
