IF EXISTS (SELECT * FROM sys.types WHERE is_table_type = 1 AND name = 'ProductIDTableType')
BEGIN
    DROP TYPE dbo.ProductIDTableType;
END
GO

IF OBJECT_ID('dbo.SetDiscontinuedDateForProducts', 'P') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.SetDiscontinuedDateForProducts;
END
GO

CREATE TYPE dbo.ProductIDTableType AS TABLE
(
    ProductID INT
);
GO

CREATE PROCEDURE dbo.SetDiscontinuedDateForProducts
    @ProductIDs dbo.ProductIDTableType READONLY,
    @DiscontinueDate DATE
AS
BEGIN
    SELECT 
        p.ProductID,
        'ProductID ' + CAST(p.ProductID AS VARCHAR) + ' already has a DiscontinuedDate.' AS Message
    FROM 
        SalesLT.Product p
    INNER JOIN 
        @ProductIDs pid ON p.ProductID = pid.ProductID
    WHERE 
        p.DiscontinuedDate IS NOT NULL;

    UPDATE p
    SET p.DiscontinuedDate = @DiscontinueDate
    FROM SalesLT.Product p
    INNER JOIN @ProductIDs pid ON p.ProductID = pid.ProductID
    WHERE p.DiscontinuedDate IS NULL;
END;
GO

DECLARE @ProductIDs dbo.ProductIDTableType;
INSERT INTO @ProductIDs (ProductID) VALUES (680), (709), (710), (742), (741);

EXEC dbo.SetDiscontinuedDateForProducts @ProductIDs, '2024-10-23';
