namespace StudentRegistry
{
    partial class EditYearForm
    {
        private TextBox textBoxYear;
        private Button btnSave;

        private void InitializeComponent()
        {
            this.textBoxYear = new TextBox();
            this.btnSave = new Button();
            this.btnSave.Height = 30;

            this.SuspendLayout();

            this.textBoxYear.Location = new System.Drawing.Point(12, 12);
            this.textBoxYear.PlaceholderText = "Rok akademicki";

            this.btnSave.Text = "Zapisz";
            this.btnSave.Location = new System.Drawing.Point(12, 102);
            this.btnSave.Click += btnSave_Click;
            this.btnSave.Focus();

            this.ClientSize = new System.Drawing.Size(250, 150);
            this.Controls.Add(btnSave);
            this.Controls.Add(textBoxYear);
            this.Text = "Edycja Roku";

            this.ResumeLayout(false);
        }
    }
}
