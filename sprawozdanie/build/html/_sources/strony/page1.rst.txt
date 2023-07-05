=========================
Opis modułów i funkcji
=========================

-------------------------
Plik ServerFunctions.py
-------------------------

.. py:function:: ServerManagment()
	
	Pozwala na zarządzanie bazą baza.db z wykorzystaniem interfejsu
	
	w trybie tekstowym (CLI)


.. py:function:: Zarzadz_produktem(c)
	
	Argument c wskazuje na obiekt kursora

	Wywołuje interaktywny interfejs CLI modyfikowania produktów
	
	Możliwe funkcje:
	
    1.Wypisz dane o produckcie o podanym kodzie kreskowym
	
    2.Wypisz dane o produckcie o podanym ID
	
    3.Usun produkt o podanym kodzie kreskowym
	
    4.Usun produkt o podanym ID
	
    5.Sprawdz jakie produkty nie posiadaja przypisanej nazwy
	
    6.Sprawdz jakie produkty nie posiadaja opisu
	
    7.Dodaj produkt
	
    8.Wypisz wszystkie produkty
	

.. py:function:: Zarzadz_pracownikiem(c)

	Argument c wskazuje na obiekt kursora

	Wywołuje interaktywny interfejs CLI modyfikowania pracowników
	
	Możliwe funkcje:
	
    1.Wypisz dane o pracowniku o podanym ID
	
    2.Wypisz dane o wszystkich pracownikach
	
    3.Wypisz dane o pracowniku o nazwisku
	
    4.Zwolnij pracownika o podanym ID
	
    5.Wypisz dane o wszystkich zatrudnionych pracownikach
	
    6.Zatrudnij pracownika


-------------------------
Plik ClientModule.py
-------------------------

.. py:function:: ClientScanner()
	
	Pozwala na utworzenie pliku do importu danych
	
	o produktach w trybie tekstowym (CLI)


-------------------------
Plik ImportModule.py
-------------------------

.. py:function:: ImportFileModule(opcjonalnie[plik])
	
	Pozwala na dodanie danych z podanego pliku csv
	
	o produktach w trybie tekstowym (CLI)
	
	podanie ścieżki do pliku za pomocą opcjonalnego parametru  *plik*
	
	pominie zapytanie o nazwę pliku.
	
.. warning::
	
	Przy operacji importu należy upewnić się, czy nie jest uruchomiona funkcja
	
	*ServerManagment()*
	
-------------------------
Plik GenTestDataBase.py
-------------------------

.. py:function:: GenerateTestTables()
	
	Tworzy tabelę oraz wypełnia ją testowymi danymi

.. warning::
	
	Jeżeli baza jest wygenerowana, funkcja zwróci błąd
	

.. py:function:: FillTestData()
	
	Wypełnia tabelę testowymi danymi

.. py:function:: GenerateStructure()
	
	Tworzy tabelę oraz dodaje użytkownika o ID = 0
	
	Użytkownik jest ważny w przypadku dodawania danych za pomocą
	
	*ServerManagment()*
	
	Jeżeli baza jest wygenerowana, funkcja zwróci błąd
	
.. warning::

	Jeżeli baza jest wygenerowana, funkcja zwróci błąd
	
	Przy operacjach należy upewnić się, czy nie jest uruchomiona funkcja
	
	*ServerManagment()*