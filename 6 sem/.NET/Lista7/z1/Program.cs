using System;
using System.Drawing;
using System.Windows.Forms;

public class AnalogClockForm : Form
{
    System.Windows.Forms.Timer timer;


    public AnalogClockForm()
    {
        this.Text = "Analog Clock";
        this.DoubleBuffered = true;
        this.timer = new System.Windows.Forms.Timer { Interval = 1000 };
        this.timer.Tick += (s, e) => this.Invalidate();
        this.timer.Start();
        this.Resize += (s, e) => this.Invalidate();
    }

    protected override void OnPaint(PaintEventArgs e)
    {
        base.OnPaint(e);
        var g = e.Graphics;
        g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

        int size = Math.Min(ClientSize.Width, ClientSize.Height);
        Point center = new(ClientSize.Width / 2, ClientSize.Height / 2);
        int radius = size / 2 - 10;

        g.DrawEllipse(Pens.Black, center.X - radius, center.Y - radius, radius * 2, radius * 2);

        DateTime now = DateTime.Now;
        DrawHand(g, center, radius * 0.5f, now.Hour % 12 * 30 + now.Minute / 2, 6, Brushes.Black);
        DrawHand(g, center, radius * 0.7f, now.Minute * 6, 4, Brushes.Blue);
        DrawHand(g, center, radius * 0.9f, now.Second * 6, 2, Brushes.Red);
    }

    private void DrawHand(Graphics g, Point center, float length, float angleDeg, int thickness, Brush brush)
    {
        double angleRad = Math.PI * angleDeg / 180.0;
        Point end = new(
            center.X + (int)(length * Math.Sin(angleRad)),
            center.Y - (int)(length * Math.Cos(angleRad))
        );
        using Pen pen = new(brush, thickness);
        g.DrawLine(pen, center, end);
    }

    [STAThread]
    public static void Main() => Application.Run(new AnalogClockForm());
}
