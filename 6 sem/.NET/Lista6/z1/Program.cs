using System;
using System.Windows.Forms;

namespace UczelniaApp
{
    public class MainForm : Form
    {
        private TextBox txtNazwa;
        private TextBox txtAdres;
        private ComboBox cmbCykl;
        private CheckBox chkDzienne;
        private CheckBox chkUzupelniajace;
        private Button btnAkceptuj;
        private Button btnAnuluj;

        public MainForm()
        {
            this.Text = "Wybór uczelni";
            this.Width = 400;
            this.Height = 290;

            // Uczelnia
            GroupBox groupUczelnia = new GroupBox();
            groupUczelnia.Text = "Uczelnia";
            groupUczelnia.SetBounds(10, 10, 360, 80);

            Label lblNazwa = new Label { Text = "Nazwa:", Left = 10, Top = 20, Width = 50 };
            txtNazwa = new TextBox { Left = 70, Top = 18, Width = 270, Text = "Uniwersytet Wroc³awski" };

            Label lblAdres = new Label { Text = "Adres:", Left = 10, Top = 50, Width = 50 };
            txtAdres = new TextBox { Left = 70, Top = 48, Width = 270, Text = "pl. Uniwersytecki 1, 50-137 Wroc³aw" };

            groupUczelnia.Controls.AddRange(new Control[] { lblNazwa, txtNazwa, lblAdres, txtAdres });

            // Rodzaj studiów
            GroupBox groupStudia = new GroupBox();
            groupStudia.Text = "Rodzaj studiów";
            groupStudia.SetBounds(10, 100, 360, 90);

            Label lblCykl = new Label { Text = "Cykl nauki:", Left = 10, Top = 25 };
            cmbCykl = new ComboBox { Left = 120, Top = 22, Width = 200 };
            cmbCykl.Items.AddRange(new string[] { "3-letnie", "4-letnie", "5-letnie" });
            cmbCykl.SelectedIndex = 0;

            chkDzienne = new CheckBox { Text = "dzienne", Left = 120, Top = 55 };
            chkUzupelniajace = new CheckBox { Text = "uzupe³niaj¹ce", Left = 230, Top = 55 };

            groupStudia.Controls.AddRange(new Control[] { lblCykl, cmbCykl, chkDzienne, chkUzupelniajace });


            // Przyciski
            btnAkceptuj = new Button { Text = "Akceptuj", Left = 10, Top = 200 };
            btnAkceptuj.Click += BtnAkceptuj_Click;

            btnAnuluj = new Button { Text = "Anuluj", Left = 295, Top = 200 };
            btnAnuluj.Click += (s, e) => Application.Exit();

            this.Controls.AddRange(new Control[] { groupUczelnia, groupStudia, btnAkceptuj, btnAnuluj });
        }

        private void BtnAkceptuj_Click(object sender, EventArgs e)
        {
            string info = $"{txtNazwa.Text}\n{txtAdres.Text}\nStudia {cmbCykl.SelectedItem} ";

            if (chkDzienne.Checked)
                info += "dzienne\n";
            if (chkUzupelniajace.Checked)
                info += "uzupe³niaj¹ce";

            MessageBox.Show(info, "Uczelnia");
        }

        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new MainForm());
        }
    }
}
