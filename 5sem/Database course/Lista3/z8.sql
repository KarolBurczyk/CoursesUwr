ALTER DATABASE course  
   SET RECURSIVE_TRIGGERS ON;  
GO  

SELECT name AS 'dbo', is_recursive_triggers_on AS 'Recursive Triggers Enabled'
FROM sys.databases

DROP TABLE IF EXISTS dbo.Account;

CREATE TABLE dbo.Account (
    AccountID INT PRIMARY KEY,
    Balance DECIMAL(10, 2),
    TransferAccountID INT,
    FOREIGN KEY (TransferAccountID) REFERENCES dbo.Account(AccountID)
);

INSERT INTO dbo.Account (AccountID, Balance, TransferAccountID)
VALUES
(1, 300.00, 2),  -- Konto 1 odnosi się do konta 2
(2, 500.00, NULL), -- Konto 2 nie ma konta transferowego
(3, 1200.00, 1);   -- Konto 3 odnosi się do konta 1
GO

-- Usuwamy istniejący trigger
DROP TRIGGER IF EXISTS trg_TransferExcess;
GO

-- Tworzymy nowy trigger
CREATE TRIGGER trg_TransferExcess
ON dbo.Account
AFTER UPDATE
AS
BEGIN
    IF (TRIGGER_NESTLEVEL() > 1)
    BEGIN
        RETURN;
    END;

    DECLARE @AccountID INT, @Balance DECIMAL(10, 2), @TransferAccountID INT, @ExcessAmount DECIMAL(10, 2);

    DECLARE account_cursor CURSOR FOR
    SELECT AccountID, Balance, TransferAccountID
    FROM inserted;

    OPEN account_cursor;

    FETCH NEXT FROM account_cursor INTO @AccountID, @Balance, @TransferAccountID;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        IF @Balance > 1000
        BEGIN
            SET @ExcessAmount = @Balance - 1000;

            UPDATE dbo.Account
            SET Balance = Balance - @ExcessAmount
            WHERE AccountID = @AccountID;

            IF @TransferAccountID IS NOT NULL
            BEGIN
                UPDATE dbo.Account
                SET Balance = Balance + @ExcessAmount
                WHERE AccountID = @TransferAccountID;
            END
        END

        FETCH NEXT FROM account_cursor INTO @AccountID, @Balance, @TransferAccountID;
    END;

    CLOSE account_cursor;
    DEALLOCATE account_cursor;
END;
GO

SELECT * FROM dbo.Account;

UPDATE dbo.Account
SET Balance = Balance + 1000
WHERE AccountID = 3;

SELECT * FROM dbo.Account;

UPDATE dbo.Account
SET Balance = Balance + 1000
WHERE AccountID = 1;

SELECT * FROM dbo.Account;
