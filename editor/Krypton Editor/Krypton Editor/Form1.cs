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

namespace Krypton_Editor
{
    public partial class Form1 : Form
    {
        string lang = "CSharp (custom highlighter)";

        static Brush BlueColor = new SolidBrush(Color.FromArgb(255, 86, 156, 214));
        static Brush GreenColor = new SolidBrush(Color.FromArgb(255, 70, 201, 171));
        static Brush YellowColor = new SolidBrush(Color.FromArgb(255, 197, 172, 104));

        // Styles
        TextStyle BlueStyle = new TextStyle(BlueColor, null, FontStyle.Regular);
        TextStyle ClassStyle = new TextStyle(GreenColor, null, FontStyle.Underline);
        TextStyle YellowStyle = new TextStyle(GreenColor, null, FontStyle.Underline);
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

            //Keyword highlighting
            e.ChangedRange.SetStyle(BlueStyle, @"\b(sınıf|eğer)\b|#region\b|#endregion\b");

            //Func Invoke highlighting
            e.ChangedRange.SetStyle(YellowStyle, @"\b(yazdır)\b|#region\b|#endregion\b");
        }
    }
}
