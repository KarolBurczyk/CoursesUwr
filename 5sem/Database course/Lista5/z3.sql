-- Włączenie śledzenia statystyk wykonania zapytań (czas wykonania)
SET STATISTICS TIME ON
GO

-- Włączenie generowania planów zapytań, aby móc je analizować
SET SHOWPLAN_ALL ON;
GO

-- Zapytanie pokazujące informacje o indeksach klastrowanych w tabelach
SELECT
    TableName = t.name, -- Nazwa tabeli
    ClusteredIndexName = i.name, -- Nazwa indeksu klastrowanego
    ColumnName = c.Name -- Nazwa kolumny, która jest częścią indeksu
FROM
    sys.tables t
INNER JOIN 
    sys.indexes i ON t.object_id = i.object_id -- Łączenie z tabelą indeksów
INNER JOIN 
    sys.index_columns ic ON i.index_id = ic.index_id AND i.object_id = ic.object_id -- Łączenie z kolumnami indeksów
INNER JOIN 
    sys.columns c ON ic.column_id = c.column_id AND ic.object_id = c.object_id -- Łączenie z kolumnami tabeli
WHERE
    i.index_id = 1  -- Sprawdzanie tylko indeksów klastrowanych (index_id = 1 oznacza indeks klastrowany)
    AND EXISTS (SELECT * 
                FROM sys.columns c2 
                WHERE ic.object_id = c2.object_id AND c2.is_identity = 1) -- Sprawdzanie, czy kolumna jest kolumną tożsamości (identyfikator)
GO

-- Usuwanie istniejącego indeksu klastrowanego na tabeli Ksiazka
DROP INDEX Ksiazka_PK ON Ksiazka;

-- Tworzenie nowego indeksu klastrowanego na tabeli Ksiazka
-- Indeks będzie obejmował kolumny Ksiazka_ID, Rok_Wydania (malejąco), Tytul (rosnąco)
CREATE CLUSTERED INDEX ClusteredIX_Ksiazka ON Ksiazka (Ksiazka_ID, Rok_Wydania DESC, Tytul ASC);

-- Wykonanie zapytania, aby sprawdzić, jak indeks klastrowany wpłynął na czas wykonania
SELECT TOP 10 Rok_Wydania, Tytul FROM Ksiazka;

-- Usuwanie wcześniej utworzonego indeksu klastrowanego na tabeli Ksiazka
DROP INDEX ClusteredIX_Ksiazka ON Ksiazka;
GO

-- Tworzenie indeksu nieklastrowanego na tabeli Egzemplarz
-- Indeks obejmuje kolumny Ksiazka_ID oraz Sygnatura
CREATE NONCLUSTERED INDEX NonClusteredIX_Egzemplarz ON Egzemplarz (Ksiazka_ID, Sygnatura);

-- Wykonanie zapytania, aby sprawdzić, jak indeks nieklastrowany wpłynął na czas wykonania
SELECT TOP 10 Sygnatura, Ksiazka_ID FROM Egzemplarz;

-- Usuwanie wcześniej utworzonego indeksu nieklastrowanego na tabeli Egzemplarz
DROP INDEX NonClusteredIX_Egzemplarz ON Egzemplarz;
GO

-- Indeks klastrowy: Zmienia fizyczną organizację danych w tabeli, sortując je według klucza indeksu. 
-- Może być tylko jeden na tabelę. Używany do szybszego wykonywania zapytań zakresowych, ale wstawianie, 
-- usuwanie i aktualizowanie danych jest wolniejsze.

-- Indeks nieklastrowy: Nie zmienia fizycznej organizacji danych. Może być więcej niż jeden na tabelę. 
-- Przechowuje osobną strukturę, która wskazuje na dane, poprawiając szybkość wyszukiwania, 
-- ale może być mniej wydajny przy zapytaniach zakresowych.

-- Tworzenie zoptymalizowanych indeksów nieklastrowanych dla zapytania JOIN
-- Pierwszy indeks nieklastrowany na kolumnie Ksiazka_ID w tabeli Egzemplarz
CREATE NONCLUSTERED INDEX IX_Egzemplarz_Ksiazka_ID ON Egzemplarz (Ksiazka_ID);

-- Drugi indeks nieklastrowany na kolumnie Ksiazka_ID w tabeli Ksiazka
CREATE NONCLUSTERED INDEX IX_Ksiazka_ID ON Ksiazka (Ksiazka_ID);

-- Przeprowadzenie zapytania łączącego tabele Ksiazka i Egzemplarz
-- Analiza planu zapytania pozwoli ocenić, jak optymalizacje wpływają na wydajność
SET SHOWPLAN_ALL ON;
SELECT TOP 10 * FROM Ksiazka JOIN Egzemplarz ON Ksiazka.Ksiazka_ID = Egzemplarz.Ksiazka_ID;
SET SHOWPLAN_ALL OFF;

-- Usuwanie indeksów, które zostały utworzone na tabelach Egzemplarz i Ksiazka
DROP INDEX IX_Egzemplarz_Ksiazka_ID ON Egzemplarz;
DROP INDEX IX_Ksiazka_ID ON Ksiazka;
GO

-- Wyłączenie śledzenia statystyk wykonania zapytań (czas wykonania)
SET STATISTICS TIME OFF
GO

-- Wyłączenie generowania planów zapytań
SET SHOWPLAN_ALL OFF;
GO
