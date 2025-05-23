using System;
using System.Drawing;
using System.Windows.Forms;

namespace Punkt3Demo
{
    public class MainForm : Form
    {
        private MenuStrip menuStrip;
        private ToolStrip toolStrip;
        private TabControl tabControl;
        private ToolTip toolTip;
        private ContextMenuStrip contextMenu;

        public MainForm()
        {
            this.Text = "Z3";
            this.Width = 700;
            this.Height = 500;

            InitMenuStrip();
            InitToolStrip();
            InitContextMenu();
            InitTabControl();
            InitToolTip();
        }

        private void InitMenuStrip()
        {
            menuStrip = new MenuStrip();
            var plik = new ToolStripMenuItem("Plik");
            plik.DropDownItems.Add("Nowy");
            plik.DropDownItems.Add("Zamknij", null, (s, e) => this.Close());
            menuStrip.Items.Add(plik);
            this.MainMenuStrip = menuStrip;
            this.Controls.Add(menuStrip);
        }

        private void InitContextMenu()
        {
            contextMenu = new ContextMenuStrip();
            contextMenu.Items.Add("Opcja kontekstowa 1");
            contextMenu.Items.Add("Opcja kontekstowa 2");
        }

        private void InitToolStrip()
        {
            toolStrip = new ToolStrip();
            toolStrip.Items.Add("Opcja 1");
            toolStrip.Items.Add("Opcja 2");
            toolStrip.Top = menuStrip.Bottom;
            this.Controls.Add(toolStrip);
        }

        private void InitToolTip()
        {
            toolTip = new ToolTip();
            toolTip.SetToolTip(tabControl, "Zak³adki z ró¿nymi kontrolkami");
            toolTip.SetToolTip(menuStrip, "Menu g³ówne");
            toolTip.SetToolTip(toolStrip, "Pasek narzêdzi");
        }

        private void InitTabControl()
        {
            tabControl = new TabControl();
            tabControl.SetBounds(10, 60, 660, 380);

            var tab1 = new TabPage("FlowLayout");
            FlowLayoutPanel flow = new FlowLayoutPanel();
            flow.Dock = DockStyle.Fill;
            for (int i = 1; i <= 5; i++)
                flow.Controls.Add(new Button { Text = $"Przycisk {i}", Width = 100 });
            tab1.Controls.Add(flow);

            var tab2 = new TabPage("SplitContainer");
            SplitContainer split = new SplitContainer { Dock = DockStyle.Fill, Orientation = Orientation.Horizontal };
            split.Panel1.Controls.Add(new Label { Text = "Panel 1", Dock = DockStyle.Fill });
            split.Panel2.Controls.Add(new Label { Text = "Panel 2", Dock = DockStyle.Fill });
            tab2.Controls.Add(split);

            var tab3 = new TabPage("Panel");

            Panel panel = new Panel
            {
                Dock = DockStyle.Fill,
                BorderStyle = BorderStyle.FixedSingle,
                BackColor = Color.LightYellow
            };

            Label lblInfo = new Label
            {
                Text = "To jest zwyk³y Panel",
                Location = new Point(20, 20),
                AutoSize = true
            };

            TextBox txt = new TextBox
            {
                Location = new Point(20, 50),
                Width = 200
            };

            Button btn = new Button
            {
                Text = "Kliknij",
                Location = new Point(20, 80)
            };
            btn.Click += (s, e) => MessageBox.Show("Klikniêto w panelu!");

            panel.Controls.Add(lblInfo);
            panel.Controls.Add(txt);
            panel.Controls.Add(btn);

            tab3.Controls.Add(panel);

            tabControl.TabPages.AddRange(new TabPage[] { tab1, tab2, tab3 });

            tabControl.ContextMenuStrip = contextMenu;

            this.Controls.Add(tabControl);
        }


        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new MainForm());
        }
    }
}
