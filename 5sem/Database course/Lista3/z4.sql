ALTER DATABASE course  
   SET RECURSIVE_TRIGGERS OFF;  
GO  

DROP TRIGGER IF EXISTS SalesLT.tr_UpdateCustomerModifiedDate;
GO

CREATE TRIGGER SalesLT.tr_UpdateCustomerModifiedDate
ON SalesLT.Customer
AFTER UPDATE
AS
BEGIN
    UPDATE SalesLT.Customer
    SET ModifiedDate = GETDATE()
    FROM SalesLT.Customer AS c
    INNER JOIN Inserted AS i ON c.CustomerID = i.CustomerID;
END;
GO

UPDATE SalesLT.Customer
SET CompanyName = 'MediaExpert'
WHERE CustomerID = 5;

SELECT CustomerID, CompanyName, ModifiedDate
FROM SalesLT.Customer
WHERE CustomerID = 5;
