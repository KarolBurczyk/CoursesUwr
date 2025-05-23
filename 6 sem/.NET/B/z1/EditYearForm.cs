using System;
using System.Windows.Forms;
using System.Xml.Linq;

namespace StudentRegistry
{
    public partial class EditYearForm : Form
    {
        public XElement YearElement { get; private set; }

        public EditYearForm()
        {
            InitializeComponent();

            btnSave.Enabled = false;

            textBoxYear.TextChanged += TextBoxYear_TextChanged;
        }

        public EditYearForm(XElement yearElement) : this()
        {
            textBoxYear.Text = yearElement.Attribute("Name")?.Value;
            YearElement = new XElement(yearElement);

            UpdateSaveButtonState();
        }

        private void TextBoxYear_TextChanged(object sender, EventArgs e)
        {
            UpdateSaveButtonState();
        }

        private void UpdateSaveButtonState()
        {
            btnSave.Enabled = !string.IsNullOrWhiteSpace(textBoxYear.Text);
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            if (YearElement == null)
            {
                YearElement = new XElement("Year",
                    new XAttribute("Id", Guid.NewGuid().ToString())
                );
            }
            YearElement.SetAttributeValue("Name", textBoxYear.Text);
            DialogResult = DialogResult.OK;
        }
    }
}
