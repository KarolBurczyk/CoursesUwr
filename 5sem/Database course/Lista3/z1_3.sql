DECLARE @StartTime DATETIME = SYSDATETIME();

TRUNCATE TABLE SalesLT.CustomerBackup;

SET IDENTITY_INSERT SalesLT.CustomerBackup ON;

DECLARE @CustomerID INT,
        @NameStyle BIT,
        @Title NVARCHAR(8),
        @FirstName NVARCHAR(50),
        @MiddleName NVARCHAR(50),
        @LastName NVARCHAR(50),
        @Suffix NVARCHAR(10),
        @CompanyName NVARCHAR(128),
        @SalesPerson NVARCHAR(256),
        @EmailAddress NVARCHAR(50),
        @Phone NVARCHAR(25),
        @PasswordHash NVARCHAR(128),
        @PasswordSalt NVARCHAR(10),
        @rowguid UNIQUEIDENTIFIER,
        @ModifiedDate DATETIME;

DECLARE customer_cursor CURSOR FOR
SELECT CustomerID, NameStyle, Title, FirstName, MiddleName, LastName, Suffix,
       CompanyName, SalesPerson, EmailAddress, Phone, PasswordHash, PasswordSalt, 
       rowguid, ModifiedDate
FROM SalesLT.Customer;

OPEN customer_cursor;
FETCH NEXT FROM customer_cursor INTO @CustomerID, @NameStyle, @Title, @FirstName, 
                                     @MiddleName, @LastName, @Suffix, @CompanyName, 
                                     @SalesPerson, @EmailAddress, @Phone, @PasswordHash, 
                                     @PasswordSalt, @rowguid, @ModifiedDate;

WHILE @@FETCH_STATUS = 0
BEGIN
    INSERT INTO SalesLT.CustomerBackup (CustomerID, NameStyle, Title, FirstName, MiddleName,
                                        LastName, Suffix, CompanyName, SalesPerson, EmailAddress, 
                                        Phone, PasswordHash, PasswordSalt, rowguid, ModifiedDate)
    VALUES (@CustomerID, @NameStyle, @Title, @FirstName, @MiddleName, @LastName, @Suffix, 
            @CompanyName, @SalesPerson, @EmailAddress, @Phone, @PasswordHash, 
            @PasswordSalt, @rowguid, @ModifiedDate);

    FETCH NEXT FROM customer_cursor INTO @CustomerID, @NameStyle, @Title, @FirstName, 
                                         @MiddleName, @LastName, @Suffix, @CompanyName, 
                                         @SalesPerson, @EmailAddress, @Phone, @PasswordHash, 
                                         @PasswordSalt, @rowguid, @ModifiedDate;
END;

CLOSE customer_cursor;
DEALLOCATE customer_cursor;

DECLARE @EndTime DATETIME = SYSDATETIME();

SELECT DATEDIFF(MILLISECOND, @StartTime, @EndTime) AS TotalExecutionTimeMS;
