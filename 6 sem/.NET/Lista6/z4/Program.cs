Button btnOpen = new Button { Text = "OpenFileDialog", Top = 10, Left = 10 };
btnOpen.Click += (s, e) => {
    OpenFileDialog ofd = new OpenFileDialog();
    if (ofd.ShowDialog() == DialogResult.OK)
        MessageBox.Show("Wybrano plik: " + ofd.FileName);
};

Button btnSave = new Button { Text = "SaveFileDialog", Top = 40, Left = 10 };
btnSave.Click += (s, e) => {
    SaveFileDialog sfd = new SaveFileDialog();
    if (sfd.ShowDialog() == DialogResult.OK)
        MessageBox.Show("Zapisano do: " + sfd.FileName);
};

Button btnFolder = new Button { Text = "FolderBrowserDialog", Top = 70, Left = 10 };
btnFolder.Click += (s, e) => {
    FolderBrowserDialog fbd = new FolderBrowserDialog();
    if (fbd.ShowDialog() == DialogResult.OK)
        MessageBox.Show("Wybrano folder: " + fbd.SelectedPath);
};

// Dodaj je np. do FlowLayoutPanel z Punktu 3
flow.Controls.AddRange(new Control[] { btnOpen, btnSave, btnFolder });
