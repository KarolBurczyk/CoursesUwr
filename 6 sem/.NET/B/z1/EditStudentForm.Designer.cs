namespace StudentRegistry
{
    partial class EditStudentForm
    {
        private TextBox textBoxFirstName;
        private TextBox textBoxLastName;
        private DateTimePicker dateTimePickerBirthDate;
        private Button btnSave;

        private ListView listViewAssignments;
        private Button btnAddAssignment;
        private Button btnRemoveAssignment;

        private void InitializeComponent()
        {
            this.textBoxFirstName = new TextBox();
            this.textBoxLastName = new TextBox();
            this.dateTimePickerBirthDate = new DateTimePicker();
            this.btnSave = new Button();
            this.btnSave.Height = 30;

            this.listViewAssignments = new ListView();
            this.btnAddAssignment = new Button();
            this.btnRemoveAssignment = new Button();

            this.SuspendLayout();

            // FirstName
            this.textBoxFirstName.Location = new System.Drawing.Point(12, 12);
            this.textBoxFirstName.PlaceholderText = "Imię";

            // LastName
            this.textBoxLastName.Location = new System.Drawing.Point(12, 42);
            this.textBoxLastName.PlaceholderText = "Nazwisko";

            // BirthDate
            this.dateTimePickerBirthDate.Location = new System.Drawing.Point(12, 72);

            // ListView Assignments
            this.listViewAssignments.Location = new System.Drawing.Point(12, 102);
            this.listViewAssignments.Size = new System.Drawing.Size(320, 120);
            this.listViewAssignments.View = View.Details;
            this.listViewAssignments.FullRowSelect = true;
            this.listViewAssignments.Columns.Add("Przedmiot", 180);
            this.listViewAssignments.Columns.Add("Rok akademicki", 130);

            // Add Assignment Button
            this.btnAddAssignment.Text = "Dodaj przedmiot";
            this.btnAddAssignment.Location = new System.Drawing.Point(340, 102);
            this.btnAddAssignment.Size = new System.Drawing.Size(120, 30);
            this.btnAddAssignment.Click += btnAddAssignment_Click;

            // Remove Assignment Button
            this.btnRemoveAssignment.Text = "Usuń przedmiot";
            this.btnRemoveAssignment.Location = new System.Drawing.Point(340, 142);
            this.btnRemoveAssignment.Size = new System.Drawing.Size(120, 30);
            this.btnRemoveAssignment.Click += btnRemoveAssignment_Click;

            // Save button
            this.btnSave.Text = "Zapisz";
            this.btnSave.Location = new System.Drawing.Point(12, 230);
            this.btnSave.Click += btnSave_Click;

            this.ClientSize = new System.Drawing.Size(480, 270);
            this.Controls.Add(this.textBoxFirstName);
            this.Controls.Add(this.textBoxLastName);
            this.Controls.Add(this.dateTimePickerBirthDate);
            this.Controls.Add(this.listViewAssignments);
            this.Controls.Add(this.btnAddAssignment);
            this.Controls.Add(this.btnRemoveAssignment);
            this.Controls.Add(this.btnSave);
            this.Text = "Edycja Studenta";

            this.ResumeLayout(false);
        }
    }
}
