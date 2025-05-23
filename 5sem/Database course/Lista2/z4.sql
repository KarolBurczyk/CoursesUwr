IF OBJECT_ID('dbo.GetTotalBorrowedDaysByReaders', 'P') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.GetTotalBorrowedDaysByReaders;
END
GO

IF EXISTS (SELECT * FROM sys.types WHERE is_table_type = 1 AND name = 'IntTableType')
BEGIN
    DROP TYPE dbo.IntTableType;
END
GO

CREATE TYPE dbo.IntTableType AS TABLE
(
    ID INT
);
GO

CREATE PROCEDURE GetTotalBorrowedDaysByReaders
    @ReaderIDs dbo.IntTableType READONLY
AS
BEGIN
    SELECT 
        w.Czytelnik_ID AS ReaderID,
        SUM(w.Liczba_Dni) AS SumDays
    FROM 
        Wypozyczenie w
    INNER JOIN 
        @ReaderIDs r ON w.Czytelnik_ID = r.ID
    GROUP BY 
        w.Czytelnik_ID;
END;
GO

DECLARE @ReaderIDs dbo.IntTableType;

INSERT INTO @ReaderIDs (ID) VALUES (1), (2), (3);

EXEC GetTotalBorrowedDaysByReaders @ReaderIDs;