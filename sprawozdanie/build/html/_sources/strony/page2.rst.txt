==========================
Struktura bazy danych
==========================

Tabele
=============

----------------------
Tabela ``Produkty``
----------------------

Tablica jest podzielona na:

	* ID_produktu liczbowy 🔑 🔢
	* Nazwa varchar(128)
	* Ilosc liczbowy
	* opis varchar(512)
	* kod_kreskowy varchar(16) ∉
	* ID_pracownika liczbowy ⚿
	* Data_pomiaru datetime

------------------------
Tabela ``Pracownicy``
------------------------

Tablica jest podzielona na:

	* ID_pracownika liczbowy 🔑
	* Imie varchar(64)
	* Nazwisko varchar(64)
	* Data_zatrudnienia datetime
	* Is_zatrudniony int

.. note::
	Spis symboli:
	
		∉ >> unikatowy
		
		⚿ >> klucz obcy
		
		🔑 >> klucz główny
		
		🔢 >> wartość rosnąca (autoincrement)

----------------------------------------------------
Relacje między tabelą ``Produkty`` a ``Pracownicy``
----------------------------------------------------


+-----------------+----------+-----------------+
| Produkty        |          | Pracownicy      |
+=================+==========+=================+
|  ID_Produktu    |          |                 |
|                 |          |                 |
+-----------------+----------+-----------------+
|  ID_pracownika  |    ⇔     |  ID_pracownika  |
+-----------------+----------+-----------------+