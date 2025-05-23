-- Dirty read: 

-- W brudnym odczycie transakcja odczytuje dane zmienione przez inną, niezakończoną jeszcze transakcję. 
-- Jeśli tamta transakcja zostanie wycofana, odczytane dane stają się nieprawdziwe.

-- TRANSACTION A:
BEGIN TRANSACTION;
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 1;

-- TRANSACTION B (in the same time):
SELECT Balance FROM Accounts WHERE AccountID = 1;

-- TRANSACTION A:
ROLLBACK TRANSACTION;

-- Conclusion:
-- Transakcja B odczytała zmiany, które w rzeczywistości nie zostały zapisane, 
-- co może prowadzić do nieprawidłowych wyników w jej dalszym przetwarzaniu.

-- Non-Repeatable-read:

-- W niepowtarzalnym odczycie transakcja odczytuje wartość pewnego rekordu, 
-- ale po chwili wartość ta zostaje zmieniona przez inną transakcję, przez co ponowny odczyt daje inny wynik.

-- TRANSACTION A:
BEGIN TRANSACTION;
SELECT Price FROM Products WHERE ProductID = 1; -- Zakładając, że cena wynosi 200

-- TRANSACTION B (in the same time):
BEGIN TRANSACTION;
UPDATE Products SET Price = 250 WHERE ProductID = 1;
COMMIT TRANSACTION;

-- TRANSACTION A:
SELECT Price FROM Products WHERE ProductID = 1; -- Ponowny odczyt, ale dający inny wynik

-- Conclusion:
-- Transakcja A odczytuje różne wartości dla tego samego rekordu podczas jednej operacji, 
-- co może prowadzić do niespójności, szczególnie w analizach i raportach.

-- Phantom Read

-- W odczycie fantomowym transakcja odczytuje pewien zestaw rekordów, 
-- a następnie inna transakcja dodaje lub usuwa rekordy pasujące do warunków zapytania, 
-- przez co pierwszy odczyt zwraca inny zestaw wyników niż kolejny.

-- TRANSACTION A:
BEGIN TRANSACTION;
SELECT COUNT(*) FROM Orders WHERE Amount > 1000; -- Zakładając, że wynik to 5 zamówień

-- TRANSACTION B (in the same time):BEGIN TRANSACTION;
INSERT INTO Orders (OrderID, Amount) VALUES (101, 1500);
COMMIT TRANSACTION;

-- TRANSACTION A:
SELECT COUNT(*) FROM Orders WHERE Amount > 1000; -- Ponowny odczyt, ale dający inny wynik

-- Conclusion:
-- W trakcie trwania jednej transakcji zmienił się zbiór danych, który transakcja odczytuje. 
-- Takie „fantomowe” zmiany mogą powodować problemy w aplikacjach, które wymagają stabilnego widoku danych na czas trwania operacji.
