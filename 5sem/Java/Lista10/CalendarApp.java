import java.awt.*;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Locale;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class CalendarApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(CalendarFrame::new);
    }
}

// --- MODEL ---
class CalendarModel extends AbstractListModel<String> {
    private int year;
    private int month;

    public CalendarModel(int year, int month) {
        this.year = year;
        this.month = month;
    }

    public void setYearAndMonth(int year, int month) {
        this.year = year;
        this.month = month;
        fireContentsChanged(this, 0, getSize() - 1);
    }

    @Override
    public int getSize() {
        return getDaysInMonth(year, month);
    }

    @Override
    public String getElementAt(int index) {
        int day = index + 1;
        
        // Sprawdzamy, czy to październik 1582
        if (year == 1582 && month == Calendar.OCTOBER) {
            if (day >= 5 && day <= 14) {
                return null; // Te dni są pomijane
            }
            if (day >= 15) {
                day += 10; // Po 4 października następuje dzień 15
            }
        }
        
        Calendar calendar = new GregorianCalendar(year, month, day);
        String dayOfWeek = calendar.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.getDefault());
        return String.format("%d, %s", day, dayOfWeek); // Format: <dzień miesiąca>, <dzień tygodnia>
    }    

    private int getDaysInMonth(int year, int month) {
        if (year == 1582 && month == Calendar.OCTOBER) {
            return 21; // Październik 1582 miał tylko 21 dni (pomijamy 10 dni)
        }
        Calendar calendar = new GregorianCalendar(year, month, 1);
        return calendar.getActualMaximum(Calendar.DAY_OF_MONTH);
    }
}

// --- VIEW ---
class CalendarFrame extends JFrame {
    private final JLabel yearLabel;
    private final JLabel previousMonthLabel;
    private final JLabel currentMonthLabel;
    private final JLabel nextMonthLabel;
    private final JList<String> currentMonthList;
    private final JList<String> previousMonthList;
    private final JList<String> nextMonthList;
    private final CalendarModel currentMonthModel;
    private final CalendarModel previousMonthModel;
    private final CalendarModel nextMonthModel;

    private int currentYear;
    private int currentMonth;

    public CalendarFrame() {
        currentYear = Calendar.getInstance().get(Calendar.YEAR);
        currentMonth = Calendar.getInstance().get(Calendar.MONTH);
    
        // Main frame setup
        setTitle("Universal Calendar");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
    
        // Top label
        yearLabel = new JLabel(getYearLabel(), SwingConstants.CENTER);
        yearLabel.setFont(new Font("Arial", Font.BOLD, 16));
        yearLabel.setBorder(new EmptyBorder(10, 10, 10, 10));
        add(yearLabel, BorderLayout.NORTH);
    
        // Initialize month labels and lists
        previousMonthLabel = createMonthLabel(getMonthName(currentYear, getPreviousMonth(currentMonth)));
        currentMonthLabel = createMonthLabel(getMonthName(currentYear, currentMonth));
        nextMonthLabel = createMonthLabel(getMonthName(currentYear, getNextMonth(currentMonth)));

        previousMonthModel = new CalendarModel(currentYear, getPreviousMonth(currentMonth));
        currentMonthModel = new CalendarModel(currentYear, currentMonth);
        nextMonthModel = new CalendarModel(currentYear, getNextMonth(currentMonth));

        previousMonthList = new JList<>(previousMonthModel);
        currentMonthList = new JList<>(currentMonthModel);
        nextMonthList = new JList<>(nextMonthModel);
    
        setListRenderer(previousMonthList);
        setListRenderer(currentMonthList);
        setListRenderer(nextMonthList);
    
        // Center lists with labels
        JPanel centerPanel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        // Etykiety miesięcy (górny wiersz)
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.weightx = 1.0;
        gbc.weighty = 0.1; // Mała wysokość dla etykiet
        gbc.fill = GridBagConstraints.BOTH;
        centerPanel.add(previousMonthLabel, gbc);

        gbc.gridx = 1;
        centerPanel.add(currentMonthLabel, gbc);

        gbc.gridx = 2;
        centerPanel.add(nextMonthLabel, gbc);

        // Listy dni (dolny wiersz)
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.weighty = 0.9; // Większa wysokość dla list
        centerPanel.add(new JScrollPane(previousMonthList), gbc);

        gbc.gridx = 1;
        centerPanel.add(new JScrollPane(currentMonthList), gbc);

        gbc.gridx = 2;
        centerPanel.add(new JScrollPane(nextMonthList), gbc);

        add(centerPanel, BorderLayout.CENTER);

        // Bottom toolbar
        JToolBar toolBar = new JToolBar();
        toolBar.setFloatable(false);
        JButton prevMonthButton = new JButton("<");
        JButton nextMonthButton = new JButton(">");
        prevMonthButton.addActionListener(e -> changeMonth(-1));
        nextMonthButton.addActionListener(e -> changeMonth(1));
        toolBar.add(prevMonthButton);
        toolBar.add(nextMonthButton);
    
        JSpinner yearSpinner = new JSpinner(new SpinnerNumberModel(currentYear, 1, 3999, 1));
        yearSpinner.addChangeListener(e -> changeYear((int) yearSpinner.getValue()));
        toolBar.add(yearSpinner);
    
        add(toolBar, BorderLayout.SOUTH);
    
        pack();
        setSize(800, 600);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private JLabel createMonthLabel(String monthName) {
        JLabel label = new JLabel(monthName, SwingConstants.CENTER);
        label.setFont(new Font("Arial", Font.BOLD, 12)); // Mniejszy rozmiar czcionki
        label.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1)); // Ramka dla oddzielenia
        label.setPreferredSize(new Dimension(0, 0)); // Ustawienie mniejszej wysokości
        label.setOpaque(true);
        label.setBackground(Color.LIGHT_GRAY); // Opcjonalne tło dla lepszej widoczności
        return label;
    }    

    private void setListRenderer(JList<String> list) {
        list.setFixedCellHeight(30); // Zwiększona wysokość pola dla lepszej czytelności
        list.setCellRenderer(new ListCellRenderer<>() {
            @Override
            public Component getListCellRendererComponent(JList<? extends String> list, String value, int index, boolean isSelected, boolean cellHasFocus) {
                JLabel label = new JLabel(value);
                label.setOpaque(true);
                label.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1)); // Dodanie ramki
                label.setBackground(isSelected ? Color.LIGHT_GRAY : Color.WHITE);
    
                // Pobierz dzień tygodnia
                int dayOfWeek = (index + 1) % 7; // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    
                // Ustaw kolor czcionki na czerwony, jeśli to niedziela (DayOfWeek == 1)
                if (dayOfWeek == Calendar.SUNDAY) {
                    label.setForeground(Color.RED);
                } else {
                    label.setForeground(Color.BLACK);
                }
    
                return label;
            }
        });
    }
      
    private String getYearLabel() {
        String calendarType = (currentYear < 1582 || (currentYear == 1582 && currentMonth < Calendar.OCTOBER)) ? "Julian" : "Gregorian";
        return String.format("%d (%s Calendar)", currentYear, calendarType);
    }

    private void changeMonth(int delta) {
        currentMonth += delta;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        } else if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        updateModels();
    }

    private void changeYear(int year) {
        currentYear = year;
        updateModels();
    }

    private void updateModels() {
        yearLabel.setText(getYearLabel());
        currentMonthModel.setYearAndMonth(currentYear, currentMonth);
        previousMonthModel.setYearAndMonth(currentYear, getPreviousMonth(currentMonth));
        nextMonthModel.setYearAndMonth(currentYear, getNextMonth(currentMonth));

        previousMonthLabel.setText(getMonthName(currentYear, getPreviousMonth(currentMonth)));
        currentMonthLabel.setText(getMonthName(currentYear, currentMonth));
        nextMonthLabel.setText(getMonthName(currentYear, getNextMonth(currentMonth)));
    }

    private String getMonthName(int year, int month) {
        Calendar calendar = new GregorianCalendar(year, month, 1);
        return calendar.getDisplayName(Calendar.MONTH, Calendar.LONG, Locale.getDefault());
    }

    private int getPreviousMonth(int month) {
        return (month == 0) ? 11 : month - 1;
    }

    private int getNextMonth(int month) {
        return (month == 11) ? 0 : month + 1;
    }
}
