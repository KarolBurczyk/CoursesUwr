using System;
using System.Linq;
using System.Windows.Forms;
using System.Xml.Linq;

namespace StudentRegistry
{
    public partial class AddAssignmentForm : Form
    {
        public string SelectedCourseId { get; private set; }
        public string SelectedYearId { get; private set; }

        public AddAssignmentForm(XElement coursesRoot, XElement yearsRoot)
        {
            InitializeComponent();

            foreach (var course in coursesRoot.Elements("Course"))
            {
                comboBoxCourses.Items.Add(new ComboboxItem(course.Attribute("Name")?.Value, course.Attribute("Id")?.Value));
            }

            foreach (var year in yearsRoot.Elements("Year"))
            {
                comboBoxYears.Items.Add(new ComboboxItem(year.Attribute("Name")?.Value, year.Attribute("Id")?.Value));
            }

            if (comboBoxCourses.Items.Count > 0)
                comboBoxCourses.SelectedIndex = 0;
            if (comboBoxYears.Items.Count > 0)
                comboBoxYears.SelectedIndex = 0;
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            if (comboBoxCourses.SelectedItem is ComboboxItem course &&
                comboBoxYears.SelectedItem is ComboboxItem year)
            {
                SelectedCourseId = course.Value;
                SelectedYearId = year.Value;

                DialogResult = DialogResult.OK;
                Close();
            }
            else
            {
                MessageBox.Show("Proszę wybrać kurs i rok akademicki.");
            }
        }
    }

    public class ComboboxItem
    {
        public string Text { get; set; }
        public string Value { get; set; }
        public ComboboxItem(string text, string value)
        {
            Text = text;
            Value = value;
        }
        public override string ToString() => Text;
    }
}
