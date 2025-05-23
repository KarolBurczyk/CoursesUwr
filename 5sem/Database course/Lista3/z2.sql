SET NOCOUNT ON;

DROP TABLE IF EXISTS Liczby;
GO

CREATE TABLE Liczby (Nr INT PRIMARY KEY, Liczba INT);
GO

DECLARE @A INT;
SET @A = 1;
WHILE (@A <= 60)
BEGIN
  INSERT INTO Liczby VALUES (@A, @A);
  SET @A = @A + 1;
END;
GO

DECLARE @X INT;
SET @X = 10;

-- Do wykonania 3 razy (każde z osobna, analizujemy wyniki: results i messages)
DECLARE C CURSOR KEYSET FOR SELECT Liczba FROM Liczby WHERE Liczba <= @X;
--DECLARE C CURSOR STATIC FOR SELECT Liczba FROM Liczby WHERE Liczba <= @X;
--DECLARE C CURSOR KEYSET FOR SELECT Liczba FROM Liczby WHERE Liczba <= @X;

SET @X = 20;

OPEN C;

DECLARE @Aux INT, @Licznik INT;
SET @Licznik = 2;

PRINT 'Kolejne liczby z kursora:';
FETCH NEXT FROM C INTO @Aux;
WHILE (@@FETCH_STATUS = 0)
BEGIN
  PRINT @Aux;
 PRINT 'Liczba: ' + CAST(@Aux AS VARCHAR);
 PRINT 'Licznik: ' + CAST(@Licznik AS VARCHAR);
  DELETE FROM Liczby WHERE Liczba = @Licznik;
  FETCH NEXT FROM C INTO @Aux;
  SET @Licznik = @Licznik + 2;
END;
PRINT 'Status ostatniej instrukcji FETCH: ' + CAST(@@FETCH_STATUS AS VARCHAR);

CLOSE C;
DEALLOCATE C;

SELECT * FROM Liczby WHERE Liczba <= 10;


