DECLARE @StartTime DATETIME = SYSDATETIME();

TRUNCATE TABLE SalesLT.CustomerBackup;

SET IDENTITY_INSERT SalesLT.CustomerBackup ON;

INSERT INTO SalesLT.CustomerBackup (CustomerID, NameStyle, Title, FirstName, MiddleName,
                                    LastName, Suffix, CompanyName, SalesPerson, EmailAddress, 
                                    Phone, PasswordHash, PasswordSalt, rowguid, ModifiedDate)
SELECT CustomerID, NameStyle, Title, FirstName, MiddleName, LastName, Suffix,
       CompanyName, SalesPerson, EmailAddress, Phone, PasswordHash, PasswordSalt, 
       rowguid, ModifiedDate
FROM SalesLT.Customer;

DECLARE @EndTime DATETIME = SYSDATETIME();

SELECT DATEDIFF(MILLISECOND, @StartTime, @EndTime) AS TotalExecutionTimeMS;
