using System;
using System.Windows.Forms;
using System.Xml.Linq;

namespace StudentRegistry
{
    public partial class EditCourseForm : Form
    {
        public XElement CourseElement { get; private set; }

        public EditCourseForm()
        {
            InitializeComponent();
            btnSave.Enabled = false;
            textBoxCourse.TextChanged += TextBoxCourse_TextChanged;
        }

        public EditCourseForm(XElement courseElement) : this()
        {
            textBoxCourse.Text = courseElement.Attribute("Name")?.Value;
            CourseElement = new XElement(courseElement);
            UpdateSaveButtonState();
        }

        private void TextBoxCourse_TextChanged(object sender, EventArgs e)
        {
            UpdateSaveButtonState();
        }

        private void UpdateSaveButtonState()
        {
            btnSave.Enabled = !string.IsNullOrWhiteSpace(textBoxCourse.Text);
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            if (CourseElement == null)
            {
                CourseElement = new XElement("Course",
                    new XAttribute("Id", Guid.NewGuid().ToString())
                );
            }
            CourseElement.SetAttributeValue("Name", textBoxCourse.Text);
            DialogResult = DialogResult.OK;
        }
    }
}
