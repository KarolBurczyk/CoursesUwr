import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import javax.swing.*;

public class FileNavigator {
    private JFrame frame;
    private JTextField currentPathField;
    private JList<String> fileList;
    private DefaultListModel<String> fileListModel;
    private JLabel fileInfoLabel;
    private ButtonGroup driveGroup;
    private File currentDirectory;

    public FileNavigator() {
        currentDirectory = new File(System.getProperty("user.dir"));

        frame = new JFrame("File Navigator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);
        frame.setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new BorderLayout());
        currentPathField = new JTextField(currentDirectory.getAbsolutePath());
        currentPathField.setEditable(false);
        topPanel.add(currentPathField, BorderLayout.CENTER);

        JButton backButton = new JButton("Cofnij");
        backButton.addActionListener(e -> navigateUp());
        topPanel.add(backButton, BorderLayout.WEST);

        frame.add(topPanel, BorderLayout.NORTH);

        fileListModel = new DefaultListModel<>();
        fileList = new JList<>(fileListModel);
        fileList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        fileList.setFont(new Font("Monospaced", Font.PLAIN, 12));
        JScrollPane scrollPane = new JScrollPane(fileList);
        frame.add(scrollPane, BorderLayout.CENTER);

        JPanel drivePanel = new JPanel();
        drivePanel.setLayout(new BoxLayout(drivePanel, BoxLayout.Y_AXIS));
        driveGroup = new ButtonGroup();

        for (File root : File.listRoots()) {
            JRadioButton driveButton = new JRadioButton(root.getAbsolutePath());
            driveButton.addActionListener(e -> changeDrive(root));
            driveGroup.add(driveButton);
            drivePanel.add(driveButton);
        }

        frame.add(drivePanel, BorderLayout.EAST);

        fileInfoLabel = new JLabel(" ");
        frame.add(fileInfoLabel, BorderLayout.SOUTH);

        fileList.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 2) {
                    navigateToSelectedDirectory();
                } else {
                    displaySelectedFileInfo();
                }
            }
        });

        loadDirectoryContents(currentDirectory);

        frame.setVisible(true);
    }

    private void loadDirectoryContents(File directory) {
        fileListModel.clear();
        File[] files = directory.listFiles();
        if (files == null) return;

        Arrays.sort(files, (f1, f2) -> {
            if (f1.isDirectory() && !f2.isDirectory()) return -1;
            if (!f1.isDirectory() && f2.isDirectory()) return 1;
            return f1.getName().compareToIgnoreCase(f2.getName());
        });

        for (File file : files) {
            if (file.isDirectory()) {
                fileListModel.addElement("[" + file.getName() + "]");
            } else {
                fileListModel.addElement(file.getName());
            }
        }

        currentPathField.setText(directory.getAbsolutePath());
        currentDirectory = directory;
    }

    private void navigateToSelectedDirectory() {
        String selectedValue = fileList.getSelectedValue();
        if (selectedValue != null && selectedValue.startsWith("[") && selectedValue.endsWith("]")) {
            String dirName = selectedValue.substring(1, selectedValue.length() - 1);
            File newDir = new File(currentDirectory, dirName);
            if (newDir.isDirectory()) {
                loadDirectoryContents(newDir);
            }
        }
    }

    private void displaySelectedFileInfo() {
        String selectedValue = fileList.getSelectedValue();
        if (selectedValue != null && !selectedValue.startsWith("[") && !selectedValue.endsWith("]")) {
            File selectedFile = new File(currentDirectory, selectedValue);
            if (selectedFile.isFile()) {
                long size = selectedFile.length();
                long lastModified = selectedFile.lastModified();
                String dateModified = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(lastModified);

                fileInfoLabel.setText("Nazwa: " + selectedFile.getName() + ", Rozmiar: " + size + " B, Ostatnia modyfikacja: " + dateModified);
            }
        } else {
            fileInfoLabel.setText(" ");
        }
    }

    private void navigateUp() {
        File parent = currentDirectory.getParentFile();
        if (parent != null) {
            loadDirectoryContents(parent);
        }
    }

    private void changeDrive(File drive) {
        loadDirectoryContents(drive);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(FileNavigator::new);
    }
}
