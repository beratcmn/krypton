namespace Krypton_Editor
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.dosyaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.açToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.yeniProjeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.varsayılanToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.boşToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mainEditor = new FastColoredTextBoxNS.FastColoredTextBox();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.mainEditor)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(60)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.menuStrip1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.dosyaToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(800, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // dosyaToolStripMenuItem
            // 
            this.dosyaToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.açToolStripMenuItem,
            this.yeniProjeToolStripMenuItem});
            this.dosyaToolStripMenuItem.ForeColor = System.Drawing.Color.White;
            this.dosyaToolStripMenuItem.Name = "dosyaToolStripMenuItem";
            this.dosyaToolStripMenuItem.Size = new System.Drawing.Size(51, 20);
            this.dosyaToolStripMenuItem.Text = "Dosya";
            // 
            // açToolStripMenuItem
            // 
            this.açToolStripMenuItem.BackColor = System.Drawing.SystemColors.Window;
            this.açToolStripMenuItem.Name = "açToolStripMenuItem";
            this.açToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.açToolStripMenuItem.Text = "Proje Aç";
            // 
            // yeniProjeToolStripMenuItem
            // 
            this.yeniProjeToolStripMenuItem.BackColor = System.Drawing.SystemColors.Window;
            this.yeniProjeToolStripMenuItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.yeniProjeToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.varsayılanToolStripMenuItem,
            this.boşToolStripMenuItem});
            this.yeniProjeToolStripMenuItem.Name = "yeniProjeToolStripMenuItem";
            this.yeniProjeToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.yeniProjeToolStripMenuItem.Text = "Yeni Proje";
            this.yeniProjeToolStripMenuItem.ToolTipText = "Yeni bir proje oluştur";
            // 
            // varsayılanToolStripMenuItem
            // 
            this.varsayılanToolStripMenuItem.BackColor = System.Drawing.SystemColors.Window;
            this.varsayılanToolStripMenuItem.Name = "varsayılanToolStripMenuItem";
            this.varsayılanToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.varsayılanToolStripMenuItem.Size = new System.Drawing.Size(169, 22);
            this.varsayılanToolStripMenuItem.Text = "Varsayılan";
            this.varsayılanToolStripMenuItem.Click += new System.EventHandler(this.varsayılanToolStripMenuItem_Click_1);
            // 
            // boşToolStripMenuItem
            // 
            this.boşToolStripMenuItem.BackColor = System.Drawing.SystemColors.Window;
            this.boşToolStripMenuItem.Name = "boşToolStripMenuItem";
            this.boşToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)(((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Shift) 
            | System.Windows.Forms.Keys.N)));
            this.boşToolStripMenuItem.Size = new System.Drawing.Size(169, 22);
            this.boşToolStripMenuItem.Text = "Boş";
            // 
            // mainEditor
            // 
            this.mainEditor.AutoCompleteBracketsList = new char[] {
        '(',
        ')',
        '{',
        '}',
        '[',
        ']',
        '\"',
        '\"',
        '\'',
        '\''};
            this.mainEditor.AutoIndentCharsPatterns = "";
            this.mainEditor.AutoScrollMinSize = new System.Drawing.Size(335, 108);
            this.mainEditor.BackBrush = null;
            this.mainEditor.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(30)))), ((int)(((byte)(30)))), ((int)(((byte)(30)))));
            this.mainEditor.BookmarkColor = System.Drawing.Color.White;
            this.mainEditor.BracketsHighlightStrategy = FastColoredTextBoxNS.BracketsHighlightStrategy.Strategy2;
            this.mainEditor.CharHeight = 18;
            this.mainEditor.CharWidth = 9;
            this.mainEditor.CommentPrefix = null;
            this.mainEditor.CurrentPenSize = 3;
            this.mainEditor.DisabledColor = System.Drawing.Color.FromArgb(((int)(((byte)(100)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))), ((int)(((byte)(180)))));
            this.mainEditor.Dock = System.Windows.Forms.DockStyle.Fill;
            this.mainEditor.DocumentPath = null;
            this.mainEditor.Font = new System.Drawing.Font("Consolas", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.mainEditor.ForeColor = System.Drawing.Color.White;
            this.mainEditor.IndentBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(30)))), ((int)(((byte)(30)))), ((int)(((byte)(30)))));
            this.mainEditor.IsReplaceMode = false;
            this.mainEditor.LeftBracket = '<';
            this.mainEditor.LeftBracket2 = '(';
            this.mainEditor.Location = new System.Drawing.Point(0, 24);
            this.mainEditor.Name = "mainEditor";
            this.mainEditor.Paddings = new System.Windows.Forms.Padding(0);
            this.mainEditor.RightBracket = '>';
            this.mainEditor.RightBracket2 = ')';
            this.mainEditor.SelectionChangedDelayedEnabled = false;
            this.mainEditor.SelectionColor = System.Drawing.Color.FromArgb(((int)(((byte)(60)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(255)))));
            this.mainEditor.ServiceColors = ((FastColoredTextBoxNS.ServiceColors)(resources.GetObject("mainEditor.ServiceColors")));
            this.mainEditor.ServiceLinesColor = System.Drawing.Color.FromArgb(((int)(((byte)(30)))), ((int)(((byte)(30)))), ((int)(((byte)(30)))));
            this.mainEditor.Size = new System.Drawing.Size(800, 426);
            this.mainEditor.TabIndex = 1;
            this.mainEditor.Text = "sınıf Program{\r\n    // Programın buradan başlıyor\r\n    fonksiyon Giriş(){\r\n      " +
    "  yazdır(\"Merhaba, Dünya!\");\r\n    }\r\n}";
            this.mainEditor.Zoom = 100;
            this.mainEditor.TextChanged += new System.EventHandler<FastColoredTextBoxNS.TextChangedEventArgs>(this.mainEditor_TextChanged);
            this.mainEditor.Load += new System.EventHandler(this.mainEditor_Load);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(37)))), ((int)(((byte)(37)))), ((int)(((byte)(37)))));
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.mainEditor);
            this.Controls.Add(this.menuStrip1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Krypton Kod Editörü";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.mainEditor)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem dosyaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem yeniProjeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem varsayılanToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem boşToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem açToolStripMenuItem;
        private FastColoredTextBoxNS.FastColoredTextBox mainEditor;
    }
}
