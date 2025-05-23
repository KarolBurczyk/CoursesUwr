CREATE FUNCTION dbo.GetReadersWithSpecimensHeldForDays
(
    @MinDays INT
)
RETURNS @ResultTable TABLE
(
    PESEL NVARCHAR(11),
    SpecimenCount INT
)
AS
BEGIN
    INSERT INTO @ResultTable (PESEL, SpecimenCount)
    SELECT
        C.PESEL,
        COUNT(W.Egzemplarz_ID) AS SpecimenCount
    FROM
        Wypozyczenie W
    INNER JOIN Czytelnik C ON W.Czytelnik_ID = C.Czytelnik_ID
    WHERE
        DATEDIFF(DAY, W.Data, GETDATE()) - W.Liczba_Dni >= @MinDays
    GROUP BY
        C.PESEL
    HAVING
        COUNT(W.Egzemplarz_ID) > 0

    RETURN;
END

-- SELECT * FROM dbo.GetReadersWithSpecimensHeldForDays(30);
