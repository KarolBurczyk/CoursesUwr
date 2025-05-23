using System;
using System.Linq;
using System.Windows.Forms;
using System.Xml.Linq;

namespace StudentRegistry
{
    public partial class MainForm : Form
    {
        string studentsFile = "students.xml";
        string coursesFile = "courses.xml";
        string yearsFile = "years.xml";
        string assignmentsFile = "assignments.xml";

        public MainForm()
        {
            InitializeComponent();
            LoadTree();
        }

        private void LoadTree()
        {
            treeView1.Nodes.Clear();

            var rootStudents = new TreeNode("Studenci") { Tag = "students" };
            var rootYears = new TreeNode("Lata Akademickie") { Tag = "years" };
            var rootCourses = new TreeNode("Zajęcia") { Tag = "courses" };

            treeView1.Nodes.Add(rootStudents);
            treeView1.Nodes.Add(rootYears);
            treeView1.Nodes.Add(rootCourses);
            treeView1.ExpandAll();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            listView1.Items.Clear();
            switch (e.Node.Tag)
            {
                case "students":
                    LoadStudents();
                    break;
                case "years":
                    LoadYears();
                    break;
                case "courses":
                    LoadCourses();
                    break;
            }
        }

        private void LoadStudents()
        {
            this.listView1.Columns[1].Text = "Imię";
            while (this.listView1.Columns.Count > 2)
            {
                this.listView1.Columns.RemoveAt(2);
            }
            this.listView1.Columns.Add("Nazwisko", 120);
            this.listView1.Columns.Add("Data urodzenia", 120);
            listView1.Items.Clear();
            var doc = XDocument.Load(studentsFile);
            foreach (var s in doc.Root.Elements("Student"))
            {
                var item = new ListViewItem(s.Attribute("Id")?.Value);
                item.SubItems.Add(s.Element("FirstName")?.Value);
                item.SubItems.Add(s.Element("LastName")?.Value);
                item.SubItems.Add(s.Element("BirthDate")?.Value);
                listView1.Items.Add(item);
            }
        }

        private void LoadYears()
        {
            this.listView1.Columns[1].Text = "Rok";
            while (this.listView1.Columns.Count > 2)
            {
                this.listView1.Columns.RemoveAt(2);
            }
            listView1.Items.Clear();
            var doc = XDocument.Load(yearsFile);
            foreach (var y in doc.Root.Elements("Year"))
            {
                var item = new ListViewItem(y.Attribute("Id")?.Value);
                item.SubItems.Add(y.Attribute("Name")?.Value);
                listView1.Items.Add(item);
            }
        }

        private void LoadCourses()
        {
            this.listView1.Columns[1].Text = "Przedmiot";
            while (this.listView1.Columns.Count > 2)
            {
                this.listView1.Columns.RemoveAt(2);
            }
            listView1.Items.Clear();
            var doc = XDocument.Load(coursesFile);
            foreach (var c in doc.Root.Elements("Course"))
            {
                var item = new ListViewItem(c.Attribute("Id")?.Value);
                item.SubItems.Add(c.Attribute("Name")?.Value);
                listView1.Items.Add(item);
            }
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            if (treeView1.SelectedNode?.Tag?.ToString() == "students")
            {
                var form = new EditStudentForm();
                if (form.ShowDialog() == DialogResult.OK)
                {
                    var doc = XDocument.Load(studentsFile);
                    doc.Root.Add(form.StudentElement);
                    doc.Save(studentsFile);
                    LoadStudents();
                }
            }
            if (treeView1.SelectedNode?.Tag?.ToString() == "years")
            {
                var form = new EditYearForm();
                if (form.ShowDialog() == DialogResult.OK)
                {
                    var doc = XDocument.Load(yearsFile);
                    doc.Root.Add(form.YearElement);
                    doc.Save(yearsFile);
                    LoadYears();
                }
            }
            if (treeView1.SelectedNode?.Tag?.ToString() == "courses")
            {
                var form = new EditCourseForm();
                if (form.ShowDialog() == DialogResult.OK)
                {
                    var doc = XDocument.Load(coursesFile);
                    doc.Root.Add(form.CourseElement);
                    doc.Save(coursesFile);
                    LoadCourses();
                }
            }
        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            if (treeView1.SelectedNode?.Tag?.ToString() == "students" && listView1.SelectedItems.Count > 0)
            {
                string selectedId = listView1.SelectedItems[0].Text;

                var doc = XDocument.Load(studentsFile);
                var studentElement = doc.Root.Elements("Student")
                    .FirstOrDefault(x => x.Attribute("Id")?.Value == selectedId);

                if (studentElement != null)
                {
                    var form = new EditStudentForm(studentElement);
                    if (form.ShowDialog() == DialogResult.OK)
                    {
                        studentElement.ReplaceWith(form.StudentElement);
                        doc.Save(studentsFile);
                        LoadStudents();
                    }
                }
            }
            if (treeView1.SelectedNode?.Tag?.ToString() == "years" && listView1.SelectedItems.Count > 0)
            {
                string selectedId = listView1.SelectedItems[0].Text;

                var doc = XDocument.Load(yearsFile);
                var yearElement = doc.Root.Elements("Year")
                    .FirstOrDefault(x => x.Attribute("Id")?.Value == selectedId);

                if (yearElement != null)
                {
                    var form = new EditYearForm(yearElement);
                    if (form.ShowDialog() == DialogResult.OK)
                    {
                        yearElement.ReplaceWith(form.YearElement);
                        doc.Save(yearsFile);
                        LoadYears();
                    }
                }
            }
            if (treeView1.SelectedNode?.Tag?.ToString() == "courses" && listView1.SelectedItems.Count > 0)
            {
                string selectedId = listView1.SelectedItems[0].Text;

                var doc = XDocument.Load(coursesFile);
                var courseElement = doc.Root.Elements("Course")
                    .FirstOrDefault(x => x.Attribute("Id")?.Value == selectedId);

                if (courseElement != null)
                {
                    var form = new EditCourseForm(courseElement);
                    if (form.ShowDialog() == DialogResult.OK)
                    {
                        courseElement.ReplaceWith(form.CourseElement);
                        doc.Save(coursesFile);
                        LoadCourses();
                    }
                }
            }
        }
    }
}
