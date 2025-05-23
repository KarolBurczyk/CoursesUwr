IF OBJECT_ID ('SalesLT.tr_LogProductCostPriceChanges', 'TR') IS NOT NULL
    DROP TRIGGER SalesLT.tr_LogProductCostPriceChanges;
GO

CREATE TRIGGER SalesLT.tr_LogProductCostPriceChanges
ON SalesLT.Product
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO SalesLT.ProductCostPriceHistory (ProductID, StandardCost, ListPrice, StartDate)
    SELECT 
        i.ProductID, 
        i.StandardCost, 
        i.ListPrice, 
        GETDATE() AS StartDate
    FROM 
        Inserted AS i
    INNER JOIN 
        Deleted AS d ON i.ProductID = d.ProductID
    WHERE 
        (i.StandardCost <> d.StandardCost OR i.ListPrice <> d.ListPrice);

    UPDATE SalesLT.ProductCostPriceHistory
    SET EndDate = GETDATE()
    FROM SalesLT.ProductCostPriceHistory AS h
    INNER JOIN Deleted AS d ON h.ProductID = d.ProductID
    WHERE 
        h.EndDate IS NULL
        AND (d.StandardCost <> h.StandardCost OR d.ListPrice <> h.ListPrice);
END;
GO
