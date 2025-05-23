SET STATISTICS TIME ON;
GO

SET SHOWPLAN_ALL ON;
GO

DROP PROCEDURE IF EXISTS ex1;
DROP PROCEDURE IF EXISTS ex2;
DROP PROCEDURE IF EXISTS ex3;
GO

CREATE PROCEDURE ex1
AS
BEGIN
    SELECT DISTINCT c.PESEL, c.Nazwisko
    FROM Egzemplarz e
    JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
    JOIN Wypozyczenie w ON e.Egzemplarz_ID = w.Egzemplarz_ID
    JOIN Czytelnik c ON c.Czytelnik_ID = w.Czytelnik_ID;
END;
GO

CREATE PROCEDURE ex2
AS
BEGIN
    SELECT c.PESEL, c.Nazwisko
    FROM Czytelnik c
    WHERE c.Czytelnik_ID IN (
        SELECT w.Czytelnik_ID
        FROM Wypozyczenie w
        JOIN Egzemplarz e ON e.Egzemplarz_ID = w.Egzemplarz_ID
        JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
    );
END;
GO

CREATE PROCEDURE ex3
AS
BEGIN
    SELECT DISTINCT c.PESEL, c.Nazwisko
    FROM Czytelnik c
    WHERE c.Czytelnik_ID IN (
        SELECT DISTINCT w.Czytelnik_ID
        FROM Wypozyczenie w
        WHERE w.Egzemplarz_ID IN (
            SELECT e.Egzemplarz_ID
            FROM Egzemplarz e
            JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
        )
    );
END;
GO

DELETE FROM Wypozyczenie;
DELETE FROM Egzemplarz;
DELETE FROM Ksiazka;
DELETE FROM Czytelnik;
GO

-------------------------------------------------------------------------------------------

SET IDENTITY_INSERT Ksiazka ON;
INSERT INTO Ksiazka (Ksiazka_ID, ISBN, Tytul, Autor, Rok_Wydania, Cena) VALUES
(1, '978-83-8125-011-0', 'Podstawy SQL', 'Jan Kowalski', 2018, 45),
(2, '978-83-8125-012-7', 'Zaawansowane SQL', 'Anna Nowak', 2020, 70),
(3, '978-83-8125-013-4', 'Projektowanie Baz Danych', 'Piotr Malinowski', 2019, 55),
(4, '978-83-8125-014-1', 'SQL dla początkujących', 'Magdalena Lis', 2021, 40),
(5, '978-83-8125-015-8', 'Administracja SQL', 'Tomasz Zięba', 2017, 65);
SET IDENTITY_INSERT Ksiazka OFF;
GO

SET IDENTITY_INSERT Egzemplarz ON;
INSERT INTO Egzemplarz (Egzemplarz_ID, Ksiazka_ID, Sygnatura) VALUES
(1, 1, 'E001'),
(2, 1, 'E002'),
(3, 2, 'E003'),
(4, 3, 'E004'),
(5, 4, 'E005'),
(6, 5, 'E006');
SET IDENTITY_INSERT Egzemplarz OFF;
GO

SET IDENTITY_INSERT Czytelnik ON;
INSERT INTO Czytelnik (Czytelnik_ID, PESEL, Nazwisko, Miasto, Data_Urodzenia) VALUES
(1, '90010112345', 'Kowalski', 'Warszawa', '1990-01-01'),
(2, '85050554321', 'Nowak', 'Kraków', '1985-05-05'),
(3, '80030387654', 'Lis', 'Poznań', '1980-03-03');
SET IDENTITY_INSERT Czytelnik OFF;
GO

SET IDENTITY_INSERT Wypozyczenie ON;
INSERT INTO Wypozyczenie (Wypozyczenie_ID, Czytelnik_ID, Egzemplarz_ID, Data, Liczba_Dni) VALUES
(1, 1, 1, '2023-01-01', 14),
(2, 1, 2, '2023-01-15', 7),
(3, 2, 3, '2023-02-01', 30),
(4, 3, 4, '2023-03-01', 21),
(5, 3, 5, '2023-04-01', 14),
(6, 2, 6, '2023-05-01', 10);
SET IDENTITY_INSERT Wypozyczenie OFF;
GO

------------------------------------------------------------------------------------------------

DECLARE @counter INT = 1;
WHILE @counter <= 100000
BEGIN
    INSERT INTO Czytelnik (PESEL, Nazwisko, Miasto, Data_Urodzenia)
    VALUES (FORMAT(@counter, '00000000000'), CONCAT('Nazwisko', @counter), 'Miasto', '2000-01-01');

    INSERT INTO Ksiazka (ISBN, Tytul, Autor, Rok_Wydania, Cena)
    VALUES (FORMAT(@counter, '978-83-8125-{000}'), 'TytulTestowy', 'AutorTestowy', 2022, 50);

    INSERT INTO Egzemplarz (Ksiazka_ID, Sygnatura)
    VALUES (1, FORMAT(@counter, 'E{000}'));

    INSERT INTO Wypozyczenie (Czytelnik_ID, Egzemplarz_ID, Data, Liczba_Dni)
    VALUES (1, 1, '2022-01-01', 7);

    SET @counter = @counter + 1;
END;
GO

ALTER TABLE Czytelnik CHECK CONSTRAINT ALL;
ALTER TABLE Ksiazka CHECK CONSTRAINT ALL;
ALTER TABLE Egzemplarz CHECK CONSTRAINT ALL;
ALTER TABLE Wypozyczenie CHECK CONSTRAINT ALL;
GO

DECLARE @StartTime1 DATETIME, @EndTime1 DATETIME;
DECLARE @StartTime2 DATETIME, @EndTime2 DATETIME;
DECLARE @StartTime3 DATETIME, @EndTime3 DATETIME;

SET @StartTime1 = GETDATE();
EXEC ex1;
SET @EndTime1 = GETDATE();

SET @StartTime2 = GETDATE();
EXEC ex2;
SET @EndTime2 = GETDATE();

SET @StartTime3 = GETDATE();
EXEC ex3;
SET @EndTime3 = GETDATE();

DECLARE @Runtime1 INT, @Runtime2 INT, @Runtime3 INT;
SET @Runtime1 = DATEDIFF(ms, @StartTime1, @EndTime1);
SET @Runtime2 = DATEDIFF(ms, @StartTime2, @EndTime2);
SET @Runtime3 = DATEDIFF(ms, @StartTime3, @EndTime3);

PRINT 'Runtime of ex1: ' + CAST(@Runtime1 AS VARCHAR) + ' ms';
PRINT 'Runtime of ex2: ' + CAST(@Runtime2 AS VARCHAR) + ' ms';
PRINT 'Runtime of ex3: ' + CAST(@Runtime3 AS VARCHAR) + ' ms';
GO

SET STATISTICS TIME OFF;
SET SHOWPLAN_ALL OFF;
GO