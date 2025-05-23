
DROP TABLE IF EXISTS Prices;
DROP TABLE IF EXISTS Rates;
DROP TABLE IF EXISTS Products;
GO

CREATE TABLE Products (
    ID INT PRIMARY KEY,
    ProductName NVARCHAR(50)
);

CREATE TABLE Rates (
    Currency NVARCHAR(10) PRIMARY KEY,
    PricePLN DECIMAL(18, 2)
);

CREATE TABLE Prices (
    ProductID INT,
    Currency NVARCHAR(10),
    Price DECIMAL(18, 2)
);

INSERT INTO Products (ID, ProductName) VALUES (1, 'Produkt A'), (2, 'Produkt B');

INSERT INTO Rates (Currency, PricePLN) VALUES ('USD', 3.8), ('EUR', 4.5), ('GBP', 5.2);

INSERT INTO Prices (ProductID, Currency, Price) VALUES 
    (1, 'USD', 3.8), 
    (1, 'EUR', 4.5), 
    (1, 'GBP', 5.2), 
    (2, 'USD', 3.8), 
    (2, 'EUR', 4.5), 
    (2, 'YEN', 0.03);

DECLARE C CURSOR FOR
    SELECT ProductID, Currency, Price
    FROM Prices;

DECLARE @ProductID INT;
DECLARE @Currency NVARCHAR(10);
DECLARE @Price DECIMAL(18, 2);

OPEN C;

FETCH NEXT FROM C INTO @ProductID, @Currency, @Price;

WHILE @@FETCH_STATUS = 0
BEGIN
    IF EXISTS (SELECT 1 FROM Rates WHERE Currency = @Currency)
    BEGIN
        DECLARE @PricePLN DECIMAL(18, 2);
        SELECT @PricePLN = PricePLN FROM Rates WHERE Currency = @Currency;

        UPDATE Prices
        SET Price = @PricePLN
        WHERE ProductID = @ProductID AND Currency = @Currency;
    END
    ELSE
    BEGIN
        DELETE FROM Prices
        WHERE ProductID = @ProductID AND Currency = @Currency;
    END

    FETCH NEXT FROM C INTO @ProductID, @Currency, @Price;
END

CLOSE C;
DEALLOCATE C;

SELECT * FROM Prices;
