-- Locking hints (podpowiedzi dotyczące blokad) w SQL Server umożliwiają programistom jawne określenie rodzaju 
-- blokady lub jej braku podczas wykonywania zapytania, niezależnie od bieżącego poziomu izolacji transakcji. 
-- Dzięki temu można precyzyjnie kontrolować zachowanie współbieżności i wydajności.

-- NOLOCK:
-- Oznacza, że zapytanie nie nakłada blokad współdzielonych (shared locks) ani nie respektuje blokad ekskluzywnych (exclusive locks).
-- Pozwala na odczyt danych niezatwierdzonych (dirty reads), co może prowadzić do niespójności.

DROP TABLE IF EXISTS Produkty;

CREATE TABLE Produkty (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(50),
    Price DECIMAL(10, 2)
);

INSERT INTO Produkty VALUES (1, 'Laptop', 1000.00), (2, 'Tablet', 500.00);

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

BEGIN TRANSACTION;


-- Zapytanie bez NOLOCK
SELECT * FROM Produkty WHERE Price > 400;

-- Symulacja trzymania blokady poprzez brak zatwierdzenia
-- COMMIT TRANSACTION;

-- -- Podczas działania poprzedniej transakcji wykonujemy:
SELECT * FROM Produkty WITH (NOLOCK) WHERE Price > 400;

COMMIT TRANSACTION
