IF OBJECT_ID('SalesLT.ProductCostPriceHistory', 'U') IS NOT NULL
    DROP TABLE SalesLT.ProductCostPriceHistory;
GO

CREATE TABLE SalesLT.ProductCostPriceHistory (
    ProductID INT NOT NULL REFERENCES SalesLT.Product(ProductID),
    StandardCost DECIMAL(18, 2),
    ListPrice DECIMAL(18, 2),
    StartDate DATETIME NOT NULL DEFAULT GETDATE(),
    EndDate DATETIME NULL,
    CONSTRAINT PK_ProductCostPriceHistory PRIMARY KEY (ProductID, StartDate)
);
GO
