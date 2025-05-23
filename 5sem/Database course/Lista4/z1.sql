-- ACID to zbiór czterech zasad zapewniających niezawodność i integralność transakcji w bazach danych. Skrót ACID oznacza:

-- Atomicity (Atomowość) - Transakcja jest niepodzielna, czyli albo wykonuje się w całości, albo wcale. 
-- Gwarantuje to, że żadne częściowe dane nie pozostaną w bazie w przypadku przerwania transakcji.

-- Consistency (Spójność) - Po zakończeniu transakcji baza danych musi być w spójnym stanie, zgodnym z regułami i ograniczeniami danych.

-- Isolation (Izolacja) - Równocześnie wykonywane transakcje nie wpływają na siebie nawzajem. 
-- Każda transakcja działa jakby była wykonywana osobno, co zapobiega konflikom między nimi.

-- Durability (Trwałość) - Po zatwierdzeniu transakcji, jej efekty są trwałe i przetrwają ewentualne awarie systemu.

-- Zasady ACID zapewniają, że operacje na danych są niezawodne, chronią przed błędami, a baza pozostaje w stanie poprawnym niezależnie od sytuacji.