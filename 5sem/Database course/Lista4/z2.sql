-- Savepoint w systemach zarządzania bazami danych to punkt kontrolny utworzony wewnątrz transakcji, 
-- do którego można cofnąć się w razie potrzeby, aby anulować część działań, ale nie całą transakcję. 
-- Jest to przydatne w sytuacjach, gdy podczas przetwarzania części danych wystąpi błąd, 
-- ale chcemy zachować wcześniej dokonane zmiany, lub gdy musimy anulować tylko wybrane działania w transakcji.

DROP PROCEDURE IF EXISTS DeleteCustomerOrder;
GO

CREATE PROCEDURE DeleteCustomerOrder
    @OrderID INT
AS
    DECLARE @TranCounter INT;
    SET @TranCounter = @@TRANCOUNT;

    IF @TranCounter > 0
        SAVE TRANSACTION OrderSave;
    ELSE
        BEGIN TRANSACTION;

    BEGIN TRY
        DELETE FROM SalesLT.SalesOrderHeader WHERE SalesOrderID = @OrderID;

        SAVE TRANSACTION DetailSave;

        DELETE FROM SalesLT.SalesOrderDetail WHERE SalesOrderID = @OrderID;

        IF @TranCounter = 0
            COMMIT TRANSACTION;

    END TRY
    BEGIN CATCH
        IF @TranCounter = 0
            ROLLBACK TRANSACTION;
        ELSE
            IF XACT_STATE() <> -1
                ROLLBACK TRANSACTION DetailSave;

        DECLARE @ErrorMessage NVARCHAR(4000);
        DECLARE @ErrorSeverity INT;
        DECLARE @ErrorState INT;

        SELECT @ErrorMessage = ERROR_MESSAGE();
        SELECT @ErrorSeverity = ERROR_SEVERITY();
        SELECT @ErrorState = ERROR_STATE();

        RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH
GO

EXEC DeleteCustomerOrder @OrderID = 71774;