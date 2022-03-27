using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using FastColoredTextBoxNS;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;

namespace Krypton_Editor
{
    public partial class Form1 : Form
    {

        public const int WM_NCLBUTTONDOWN = 0xA1;
        public const int HT_CAPTION = 0x2;

        [DllImportAttribute("user32.dll")]
        public static extern int SendMessage(IntPtr hWnd,
                         int Msg, int wParam, int lParam);
        [DllImportAttribute("user32.dll")]
        public static extern bool ReleaseCapture();



        static Brush BlueColor = new SolidBrush(Color.FromArgb(255, 86, 156, 214));
        static Brush GreenColor = new SolidBrush(Color.FromArgb(255, 70, 201, 171));
        static Brush YellowColor = new SolidBrush(Color.FromArgb(255, 197, 172, 104));

        // Styles
        TextStyle BlueStyle = new TextStyle(BlueColor, null, FontStyle.Regular);
        TextStyle ClassStyle = new TextStyle(GreenColor, null, FontStyle.Underline);
        TextStyle YellowStyle = new TextStyle(YellowColor, null, FontStyle.Regular);
        TextStyle GrayStyle = new TextStyle(Brushes.Gray, null, FontStyle.Regular);
        TextStyle MagentaStyle = new TextStyle(Brushes.Magenta, null, FontStyle.Regular);
        TextStyle GreenStyle = new TextStyle(Brushes.Green, null, FontStyle.Italic);
        TextStyle BrownStyle = new TextStyle(Brushes.Brown, null, FontStyle.Italic);
        TextStyle MaroonStyle = new TextStyle(Brushes.Maroon, null, FontStyle.Regular);

        MarkerStyle SameWordsStyle = new MarkerStyle(new SolidBrush(Color.FromArgb(40, Color.Gray)));

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mainEditor.AddStyle(SameWordsStyle);
        }


        private void varsayılanToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            MessageBox.Show("Varsayılan Yeni Proje");
        }

        private void mainEditor_Load(object sender, EventArgs e)
        {

        }

        void mainEditor_TextChanged(object sender, TextChangedEventArgs e)
        {

            mainEditor.LeftBracket = '(';
            mainEditor.RightBracket = ')';
            mainEditor.LeftBracket2 = '\x0';
            mainEditor.RightBracket2 = '\x0';

            //Clear style of changed range
            e.ChangedRange.ClearStyle(BlueStyle, ClassStyle, YellowStyle, GrayStyle, MagentaStyle, GreenStyle, BrownStyle);

            //Comments
            e.ChangedRange.SetStyle(GreenStyle, @"//.*$", RegexOptions.Multiline);
            e.ChangedRange.SetStyle(GreenStyle, @"(/\*.*?\*/)|(/\*.*)", RegexOptions.Singleline);
            e.ChangedRange.SetStyle(GreenStyle, @"(/\*.*?\*/)|(.*\*/)", RegexOptions.Singleline | RegexOptions.RightToLeft);

            //Number highlighting
            e.ChangedRange.SetStyle(MagentaStyle, @"\b\d+[\.]?\d*([eE]\-?\d+)?[lLdDfF]?\b|\b0x[a-fA-F\d]+\b");

            //Attribute highlighting
            e.ChangedRange.SetStyle(GrayStyle, @"^\s*(?<range>\[.+?\])\s*$", RegexOptions.Multiline);

            //Class name highlighting
            e.ChangedRange.SetStyle(ClassStyle, @"\b(sınıf)\s+(?<range>\w+?)\b");

            //Function name highlighting
            // e.ChangedRange.SetStyle(YellowStyle, @"\b(fonksiyon)\s+(?<range>\w+?)\b"); //? Useless for now

            //Keyword highlighting
            e.ChangedRange.SetStyle(BlueStyle, @"\b(sınıf|fonksiyon)\b|#region\b|#endregion\b");

            //Func Invoke highlighting
            e.ChangedRange.SetStyle(YellowStyle, @"\b([a-zA-Zığüşöç])*\s*(?=\()");
            // e.ChangedRange.SetStyle(YellowStyle, @"");

            //string highlighting
            e.ChangedRange.SetStyle(BrownStyle, @"""""|@""""|''|@"".*?""|(?<!@)(?<range>"".*?[^\\]"")|'.*?[^\\]'");

            //clear folding markers
            e.ChangedRange.ClearFoldingMarkers();

            //set folding markers
            e.ChangedRange.SetFoldingMarkers("{", "}");//allow to collapse brackets block
            e.ChangedRange.SetFoldingMarkers(@"#region\b", @"#endregion\b");//allow to collapse #region blocks
            e.ChangedRange.SetFoldingMarkers(@"/\*", @"\*/");//allow to collapse comment block
        }

        private void closeButton_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }

        private void maximizeButton_Click(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Maximized)
            {
                this.WindowState = FormWindowState.Normal;
            }
            else if (this.WindowState == FormWindowState.Normal)
            {
                this.WindowState = FormWindowState.Maximized;
            }
        }

        private void minimizeButton_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void titleBar_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                ReleaseCapture();
                SendMessage(Handle, WM_NCLBUTTONDOWN, HT_CAPTION, 0);
            }
        }

        private void titleBar_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (this.WindowState == FormWindowState.Maximized)
            {
                this.WindowState = FormWindowState.Normal;
            }
            else if (this.WindowState == FormWindowState.Normal)
            {
                this.WindowState = FormWindowState.Maximized;
            }
        }

        private void menuStrip1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //ReleaseCapture();
                SendMessage(Handle, WM_NCLBUTTONDOWN, HT_CAPTION, 0);
            }
        }

        private void menuStrip1_DoubleClick(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Maximized)
            {
                this.WindowState = FormWindowState.Normal;
            }
            else if (this.WindowState == FormWindowState.Normal)
            {
                this.WindowState = FormWindowState.Maximized;
            }
        }
    }
}
