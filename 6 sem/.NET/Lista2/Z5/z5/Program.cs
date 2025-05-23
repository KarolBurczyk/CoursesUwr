class Grid
{
    private int[,] _data;

    public int Rows { get; }
    public int Columns { get; }

    public Grid(int rows, int columns)
    {
        if (rows <= 0 || columns <= 0)
            throw new ArgumentException("Liczba wierszy i kolumn musi być większa niż 0");

        Rows = rows;
        Columns = columns;
        _data = new int[rows, columns];
    }

    public int this[int row, int col]
    {
        get
        {
            ValidateIndices(row, col);
            return _data[row, col];
        }
        set
        {
            ValidateIndices(row, col);
            _data[row, col] = value;
        }
    }

    public int[] this[int row]
    {
        get
        {
            if (row < 0 || row >= Rows)
                throw new IndexOutOfRangeException("Niepoprawny indeks wiersza");

            int[] rowData = new int[Columns];
            for (int col = 0; col < Columns; col++)
            {
                rowData[col] = _data[row, col];
            }
            return rowData;
        }
    }

    private void ValidateIndices(int row, int col)
    {
        if (row < 0 || row >= Rows || col < 0 || col >= Columns)
            throw new IndexOutOfRangeException("Indeksy poza zakresem");
    }

    public void Print()
    {
        for (int i = 0; i < Rows; i++)
        {
            for (int j = 0; j < Columns; j++)
            {
                Console.Write(_data[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }
}

// Tablice postrzępione to tablice tablic, nie muszą mieć identycznych rozmiarów
class Program
{
    static void Main()
    {
        Grid grid = new Grid(4, 4);

        grid[2, 2] = 5;
        grid[1, 3] = 7;

        int elem = grid[2, 2];
        Console.WriteLine($"Element w [2,2]: {elem}");

        int[] rowData = grid[1];
        Console.WriteLine("Zawartość wiersza 1: " + string.Join(", ", rowData));

        Console.WriteLine("Aktualna siatka:");
        grid.Print();
    }
}
