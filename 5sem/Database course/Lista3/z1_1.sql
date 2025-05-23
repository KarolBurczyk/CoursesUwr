IF OBJECT_ID('SalesLT.CustomerBackup', 'U') IS NOT NULL
    DROP TABLE SalesLT.CustomerBackup;

SELECT *
INTO SalesLT.CustomerBackup
FROM SalesLT.Customer
WHERE 1 = 0;
