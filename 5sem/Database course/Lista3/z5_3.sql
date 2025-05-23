IF OBJECT_ID ('SalesLT.tr_LogInitialProductCostPrice', 'TR') IS NOT NULL
    DROP TRIGGER SalesLT.tr_LogInitialProductCostPrice;
GO

CREATE TRIGGER SalesLT.tr_LogInitialProductCostPrice
ON SalesLT.Product
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO SalesLT.ProductCostPriceHistory (ProductID, StandardCost, ListPrice, StartDate)
    SELECT 
        i.ProductID, 
        i.StandardCost, 
        i.ListPrice, 
        GETDATE() AS StartDate
    FROM Inserted AS i;
END;
GO

-- INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate)
-- VALUES ('Test Product 2', 'TP-002', 100.00, 150.00, GETDATE());

UPDATE SalesLT.Product
SET StandardCost = 120.00, ListPrice = 170.00
WHERE Name = 'Test Product 2';

UPDATE SalesLT.Product
SET StandardCost = 130.00, ListPrice = 180.00
WHERE Name = 'Test Product 2';

SELECT * FROM SalesLT.ProductCostPriceHistory WHERE ProductID = (SELECT ProductID FROM SalesLT.Product WHERE Name = 'Test Product 2');
SELECT * FROM SalesLT.ProductCostPriceHistory WHERE ProductID = (SELECT ProductID FROM SalesLT.Product WHERE Name = 'Test Product');
