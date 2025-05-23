SELECT DISTINCT c.PESEL, c.Nazwisko
FROM Egzemplarz e
JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
JOIN Wypozyczenie w ON e.Egzemplarz_ID = w.Egzemplarz_ID
JOIN Czytelnik c ON c.Czytelnik_ID = w.Czytelnik_ID;

Wykorzystuje łączenia tabel (JOIN) do uzyskania danych z czterech tabel: Ksiazka, Egzemplarz, Wypozyczenie i Czytelnik. 
Wynik jest filtrowany za pomocą DISTINCT na kolumnach PESEL i Nazwisko, aby unikać duplikatów.

SELECT c.PESEL, c.Nazwisko
FROM Czytelnik c
WHERE c.Czytelnik_ID IN (
  SELECT w.Czytelnik_ID
  FROM Wypozyczenie w
  JOIN Egzemplarz e ON e.Egzemplarz_ID = w.Egzemplarz_ID
  JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
);

Wykorzystuje podzapytanie w klauzuli WHERE, aby znaleźć czytelników, którzy występują w tabeli Wypozyczenie. Zamiast łączeń używa podejścia "IN":

SELECT DISTINCT c.PESEL, c.Nazwisko
FROM Czytelnik c
WHERE c.Czytelnik_ID IN (
    SELECT DISTINCT w.Czytelnik_ID
    FROM Wypozyczenie w
    WHERE w.Egzemplarz_ID IN (
        SELECT e.Egzemplarz_ID
        FROM Egzemplarz e
        JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
    )
);

Podobna do ex2, ale wykorzystuje dwa poziomy podzapytań (IN w zagnieżdżeniu) i dodatkowo stosuje DISTINCT w podzapycie: