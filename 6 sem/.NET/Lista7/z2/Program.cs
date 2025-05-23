using System;
using System.Drawing;
using System.Windows.Forms;

namespace SmoothProgressBarApp
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new MainForm());
        }
    }

    public class MainForm : Form
    {
        private SmoothProgressBar smoothBar;
        private System.Windows.Forms.Timer timer;

        public MainForm()
        {
            Text = "SmoothProgressBar Demo";
            Size = new Size(400, 200);

            smoothBar = new SmoothProgressBar
            {
                Location = new Point(40, 50),
                Size = new Size(300, 30),
                Min = 0,
                Max = 100,
                Value = 0
            };

            Controls.Add(smoothBar);

            timer = new System.Windows.Forms.Timer { Interval = 50 };
            timer.Tick += (s, e) =>
            {
                smoothBar.Value = (smoothBar.Value + 1) % 101;
            };
            timer.Start();
        }
    }

    public class SmoothProgressBar : Control
    {
        private int min = 0;
        private int max = 100;
        private int value = 0;

        public int Min
        {
            get => min;
            set { min = value; Invalidate(); }
        }

        public int Max
        {
            get => max;
            set { max = value; Invalidate(); }
        }

        public int Value
        {
            get => this.value;
            set
            {
                this.value = Math.Max(min, Math.Min(max, value));
                Invalidate();
            }
        }

        public SmoothProgressBar()
        {
            DoubleBuffered = true;
            SetStyle(ControlStyles.ResizeRedraw | ControlStyles.UserPaint, true);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            e.Graphics.Clear(BackColor);

            float percent = (float)(Value - Min) / (Max - Min);
            int barWidth = (int)(percent * Width);

            using var bgBrush = new SolidBrush(Color.LightGray);
            using var fillBrush = new SolidBrush(Color.DodgerBlue);

            e.Graphics.FillRectangle(bgBrush, 0, 0, Width, Height);
            e.Graphics.FillRectangle(fillBrush, 0, 0, barWidth, Height);

            using var borderPen = new Pen(Color.Black);
            e.Graphics.DrawRectangle(borderPen, 0, 0, Width - 1, Height - 1);
        }
    }
}
