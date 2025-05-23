namespace StudentRegistry
{
    partial class MainForm
    {
        private TreeView treeView1;
        private ListView listView1;
        private Button btnAdd;
        private Button btnEdit;

        private void InitializeComponent()
        {
            this.treeView1 = new TreeView();
            this.listView1 = new ListView();
            this.btnAdd = new Button();
            this.btnEdit = new Button();

            this.btnAdd.Height = 30;
            this.btnEdit.Height = 30;

            this.SuspendLayout();

            this.treeView1.Location = new System.Drawing.Point(12, 12);
            this.treeView1.Size = new System.Drawing.Size(200, 400);
            this.treeView1.AfterSelect += treeView1_AfterSelect;

            this.listView1.Location = new System.Drawing.Point(220, 12);
            this.listView1.Size = new System.Drawing.Size(500, 400);
            this.listView1.View = View.Details;
            this.listView1.Columns.Add("ID", 80);
            this.listView1.Columns.Add("Imię", 120);

            this.btnAdd.Text = "Dodaj";
            this.btnAdd.Location = new System.Drawing.Point(12, 420);
            this.btnAdd.Click += btnAdd_Click;

            this.btnEdit.Text = "Edytuj";
            this.btnEdit.Location = new System.Drawing.Point(100, 420);
            this.btnEdit.Click += btnEdit_Click;

            this.ClientSize = new System.Drawing.Size(740, 460);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.btnAdd);
            this.Controls.Add(this.btnEdit);
            this.Text = "Rejestr Studentów";

            this.ResumeLayout(false);
        }
    }
}
