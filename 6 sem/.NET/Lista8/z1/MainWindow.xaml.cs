using System;
using System.Windows;
using System.Windows.Controls;

namespace UczelniaApp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnAkceptuj_Click(object sender, RoutedEventArgs e)
        {
            string info = $"{txtNazwa.Text}\n{txtAdres.Text}\nStudia {((ComboBoxItem)cmbCykl.SelectedItem).Content} ";

            if (chkDzienne.IsChecked == true)
                info += "dzienne\n";
            if (chkUzupelniajace.IsChecked == true)
                info += "uzupełniające";

            MessageBox.Show(info, "Uczelnia");
        }

        private void BtnAnuluj_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
    }
}
