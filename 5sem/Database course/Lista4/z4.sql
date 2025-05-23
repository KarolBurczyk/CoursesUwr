DROP TABLE IF EXISTS dbo.Liczby;
GO

CREATE TABLE dbo.Liczby (Liczba INT);
GO

INSERT INTO dbo.Liczby VALUES (10);
GO

-- -- 1 --
-- SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- BEGIN TRANSACTION;

-- -- Ustawiamy poziom izolacji transakcji na REPEATABLE READ, co oznacza, że podczas trwania transakcji 
-- -- dane odczytane przez transakcję są zablokowane tak, 
-- -- aby nie mogły zostać zmienione przez inne transakcje aż do zakończenia transakcji.

-- -- W drugim połączeniu wykonujemy update: UPDATE Liczby SET Liczba = 4
-- -- Sprawdzamy blokady: sp_lock

-- SELECT * FROM dbo.Liczby;

-- WAITFOR DELAY '00:00:15';


-- -- UPDATE dbo.Liczby SET Liczba = 4

-- -- Ponownie w drugim połączeniu wykonujemy update: UPDATE Liczby SET Liczba = 4
-- -- Sprawdzamy blokady: sp_lock

-- COMMIT;



-- 2 --
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

BEGIN TRANSACTION;

WAITFOR DELAY '00:00:15';

-- Ustawiamy poziom izolacji na SERIALIZABLE, który jest najsilniejszym poziomem izolacji. 
-- Zapewnia on, że transakcja widzi stabilny zestaw danych w trakcie swojego działania, 
-- zapobiegając phantom reads (odczytom fantomowym) i innym anomaliom.

-- W drugim połączeniu wykonujemy insert: INSERT INTO Liczby VALUES (151)
-- Sprawdzamy blokady: sp_lock

SELECT * FROM Liczby;

-- Ponownie w drugim połączeniu wykonujemy insert: INSERT INTO Liczby VALUES (151)
-- Sprawdzamy blokady: sp_lock

COMMIT;
