using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Xml.Linq;

namespace StudentRegistry
{
    public partial class EditStudentForm : Form
    {
        public XElement StudentElement { get; private set; }

        private XElement assignmentsRoot;
        private XElement coursesRoot;
        private XElement yearsRoot;

        private List<XElement> studentAssignments = new List<XElement>();

        public EditStudentForm()
        {
            InitializeComponent();

            btnSave.Enabled = false;

            textBoxFirstName.TextChanged += TextBoxes_TextChanged;
            textBoxLastName.TextChanged += TextBoxes_TextChanged;

            LoadXmlFiles();

            StudentElement = new XElement("Student",
                new XAttribute("Id", Guid.NewGuid().ToString()));

            LoadAssignments();
        }


        public EditStudentForm(XElement studentElement) : this()
        {
            StudentElement = new XElement(studentElement);

            textBoxFirstName.Text = studentElement.Element("FirstName")?.Value;
            textBoxLastName.Text = studentElement.Element("LastName")?.Value;

            if (DateTime.TryParse(studentElement.Element("BirthDate")?.Value, out DateTime birthDate))
            {
                dateTimePickerBirthDate.Value = birthDate;
            }

            LoadAssignments();

            UpdateSaveButtonState();
        }

        private void LoadXmlFiles()
        {
            assignmentsRoot = XElement.Load("assignments.xml");
            coursesRoot = XElement.Load("courses.xml");
            yearsRoot = XElement.Load("years.xml");
        }


        private void TextBoxes_TextChanged(object sender, EventArgs e)
        {
            UpdateSaveButtonState();
        }

        private void UpdateSaveButtonState()
        {
            btnSave.Enabled =
                !string.IsNullOrWhiteSpace(textBoxFirstName.Text) &&
                !string.IsNullOrWhiteSpace(textBoxLastName.Text);
        }

        private void LoadAssignments()
        {
            listViewAssignments.Items.Clear();
            studentAssignments.Clear();

            string studentId = StudentElement.Attribute("Id")?.Value;

            if (string.IsNullOrEmpty(studentId))
                return;

            studentAssignments = assignmentsRoot.Elements("Assignment")
                .Where(a => a.Attribute("StudentId")?.Value == studentId)
                .ToList();

            foreach (var assign in studentAssignments)
            {
                string courseId = assign.Attribute("CourseId")?.Value;
                string yearId = assign.Attribute("YearId")?.Value;

                string courseName = coursesRoot.Elements("Course")
                    .FirstOrDefault(c => c.Attribute("Id")?.Value == courseId)?
                    .Attribute("Name")?.Value ?? "(Nieznany kurs)";

                string yearName = yearsRoot.Elements("Year")
                    .FirstOrDefault(y => y.Attribute("Id")?.Value == yearId)?
                    .Attribute("Name")?.Value ?? "(Nieznany rok)";

                var lvi = new ListViewItem(new[] { courseName, yearName });
                lvi.Tag = assign;
                listViewAssignments.Items.Add(lvi);
            }
        }

        private void btnAddAssignment_Click(object sender, EventArgs e)
        {
            using (var dlg = new AddAssignmentForm(coursesRoot, yearsRoot))
            {
                if (dlg.ShowDialog() == DialogResult.OK)
                {
                    string studentId = StudentElement.Attribute("Id")?.Value;

                    XElement newAssign = new XElement("Assignment",
                        new XAttribute("StudentId", studentId),
                        new XAttribute("CourseId", dlg.SelectedCourseId),
                        new XAttribute("YearId", dlg.SelectedYearId));

                    assignmentsRoot.Add(newAssign);
                    studentAssignments.Add(newAssign);

                    LoadAssignments();
                }
            }
        }

        private void btnRemoveAssignment_Click(object sender, EventArgs e)
        {
            if (listViewAssignments.SelectedItems.Count == 0)
                return;

            var lvi = listViewAssignments.SelectedItems[0];
            var assign = lvi.Tag as XElement;

            if (assign != null)
            {
                assignmentsRoot.Elements("Assignment").Where(a => a == assign).Remove();
                studentAssignments.Remove(assign);
                LoadAssignments();
            }
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            StudentElement.SetElementValue("FirstName", textBoxFirstName.Text);
            StudentElement.SetElementValue("LastName", textBoxLastName.Text);
            StudentElement.SetElementValue("BirthDate", dateTimePickerBirthDate.Value.ToString("yyyy-MM-dd"));

            assignmentsRoot.Save("assignments.xml");

            DialogResult = DialogResult.OK;
        }

    }
}
