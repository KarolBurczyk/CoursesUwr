namespace StudentRegistry
{
    partial class AddAssignmentForm
    {
        private ComboBox comboBoxCourses;
        private ComboBox comboBoxYears;
        private Button btnOK;
        private Button btnCancel;

        private void InitializeComponent()
        {
            this.comboBoxCourses = new ComboBox();
            this.comboBoxYears = new ComboBox();
            this.btnOK = new Button();
            this.btnOK.Height = 30;
            this.btnCancel = new Button();
            this.btnCancel.Height = 30;

            this.SuspendLayout();

            this.comboBoxCourses.Location = new System.Drawing.Point(12, 12);
            this.comboBoxCourses.Width = 250;

            this.comboBoxYears.Location = new System.Drawing.Point(12, 45);
            this.comboBoxYears.Width = 250;

            this.btnOK.Text = "OK";
            this.btnOK.Location = new System.Drawing.Point(12, 80);
            this.btnOK.Click += btnOK_Click;

            this.btnCancel.Text = "Anuluj";
            this.btnCancel.Location = new System.Drawing.Point(100, 80);
            this.btnCancel.Click += (s, e) => Close();

            this.ClientSize = new System.Drawing.Size(280, 120);
            this.Controls.Add(this.comboBoxCourses);
            this.Controls.Add(this.comboBoxYears);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.btnCancel);
            this.Text = "Dodaj Przedmiot";

            this.ResumeLayout(false);
        }
    }
}
