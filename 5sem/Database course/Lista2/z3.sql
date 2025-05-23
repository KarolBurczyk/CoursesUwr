IF OBJECT_ID('dbo.AddNewReader', 'P') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.AddNewReader;
END
GO

CREATE PROCEDURE AddNewReader
    @PESEL CHAR(11),
    @Nazwisko VARCHAR(30),
    @Miasto VARCHAR(30),
    @Data_Urodzenia DATE
AS
BEGIN
    IF LEN(@PESEL) != 11 OR @PESEL LIKE '%[^0-9]%'
    BEGIN
        RAISERROR('PESEL must consist of exactly 11 digits.', 16, 1);
        RETURN;
    END

    IF LEN(@Nazwisko) < 2
    BEGIN
        RAISERROR('Last name must be at least 2 characters long.', 16, 1);
        RETURN;
    END

    IF LEFT(@Nazwisko, 1) COLLATE Latin1_General_BIN NOT LIKE '[A-Z]'
    BEGIN
        RAISERROR('LAst name must start with a capital letter.', 16, 1);
        RETURN;
    END

    IF TRY_CONVERT(DATE, @Data_Urodzenia) IS NULL
    BEGIN
        RAISERROR('Birth date must be in the format DD-MM-YYYY.', 16, 1);
        RETURN;
    END

    INSERT INTO Czytelnik (PESEL, Nazwisko, Miasto, Data_Urodzenia)
    VALUES (@PESEL, @Nazwisko, @Miasto, @Data_Urodzenia);

    PRINT 'New reader added successfully.';
END;
GO

EXEC AddNewReader '89000134002', 'Świerk', 'Warszawa', '01.01.2023';
