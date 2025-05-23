Dwie transakcje (T1 i T2) próbują edytować ten sam rekord w tabeli Products.

ProductID	ProductName	    Price
1	        Laptop	        1000.00


Pesymistyczna kontrola współbieżności:
T1 rozpoczyna transakcję i nakłada blokadę na rekord ProductID = 1.
T1 aktualizuje cenę Price na 900.00, ale jeszcze nie zatwierdza transakcji.
T2 próbuje edytować ten sam rekord, ale jest blokowana, dopóki T1 nie zakończy transakcji.
T1 zatwierdza zmiany i zwalnia blokadę.
T2 uzyskuje dostęp do rekordu i może kontynuować.


Optymistyczna kontrola współbieżności:
T1 odczytuje rekord ProductID = 1 i planuje zmienić cenę na 900.00.
T2 równocześnie odczytuje ten sam rekord i planuje zmienić cenę na 800.00.
T1 próbuje zatwierdzić zmiany, a system waliduje, czy rekord nie został zmieniony przez inną transakcję (nie został).
T1 zatwierdza zmiany.
T2 próbuje zatwierdzić zmiany, ale system wykrywa konflikt (rekord został zmieniony przez T1) i wycofuje T2.
T2 musi odczytać nowe dane i powtórzyć transakcję.