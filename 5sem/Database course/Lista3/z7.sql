DROP TRIGGER IF EXISTS dbo.trg_LimitSpecimens
GO

CREATE TRIGGER trg_LimitSpecimens
ON dbo.Egzemplarz
INSTEAD OF INSERT
AS
BEGIN

    DECLARE @BookID INT;
    SELECT @BookID = Ksiazka_ID FROM inserted;

    IF ((SELECT COUNT(*) FROM Egzemplarz WHERE Ksiazka_ID = @BookID) >= 5)
    BEGIN
        RAISERROR ('Nie można dodać więcej niż 5 egzemplarzy dla jednej książki.', 16, 1);
        ROLLBACK TRANSACTION;
    END
    ELSE
    BEGIN
        INSERT INTO Egzemplarz (Sygnatura, Ksiazka_ID)
        SELECT Sygnatura, Ksiazka_ID FROM inserted;
    END
END;
GO

INSERT INTO Egzemplarz (Sygnatura, Ksiazka_ID) VALUES ('S0021', 4);
INSERT INTO Egzemplarz (Sygnatura, Ksiazka_ID) VALUES ('S0022', 4);
INSERT INTO Egzemplarz (Sygnatura, Ksiazka_ID) VALUES ('S0023', 4);
INSERT INTO Egzemplarz (Sygnatura, Ksiazka_ID) VALUES ('S0024', 4);
INSERT INTO Egzemplarz (Sygnatura, Ksiazka_ID) VALUES ('S0025', 4);

