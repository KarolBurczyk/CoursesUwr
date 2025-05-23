namespace StudentRegistry
{
    partial class EditCourseForm
    {
        private TextBox textBoxCourse;
        private Button btnSave;

        private void InitializeComponent()
        {
            this.textBoxCourse = new TextBox();
            this.btnSave = new Button();
            this.btnSave.Height = 30;

            this.SuspendLayout();

            this.textBoxCourse.Location = new System.Drawing.Point(12, 12);
            this.textBoxCourse.PlaceholderText = "Przedmiot";

            this.btnSave.Text = "Zapisz";
            this.btnSave.Location = new System.Drawing.Point(12, 102);
            this.btnSave.Click += btnSave_Click;

            this.ClientSize = new System.Drawing.Size(250, 150);
            this.Controls.Add(btnSave);
            this.Controls.Add(textBoxCourse);
            this.Text = "Edycja Przedmiotu";

            this.ResumeLayout(false);
        }
    }
}
