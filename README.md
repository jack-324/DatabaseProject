# Projekt bazy danych

-------------------------------------------------
Te repozytorium zawiera dwie wersje aplikacji:
-------------------------------------------------

  1.Wersje z bazą danych online (łączenie za pomocą psycopg)

  2.Wersję z bazą danych offline (plik baza.db)

W przypadku wyboru wersji online, należy w pliku hasla.txt wprowadzic odpowiednie dane do połączenia z bazą.

W przypadku wersji offline, domyślnie jest utworzona baza danych przykładowa (baza.db)

=========================
Korzystanie z aplikacji
=========================

	
	Możliwe jest wykorzystanie programu bez konieczności załączania modułów
	
	Wystarczy uruchomić odpowiednią bibliotekę poleceniem
	
	.. code-block::
	
		python modul.py


Pierwsze użycie
-------------------------

Na samym początku potrzebujemy utworzyć bazę danych.
Wywołujemy funkcję *GenerateStructure()* aby utworzył nam szkielet bazy
	
   import GenTestDataBase
   GenTestDataBase.GenerateStructure()

	
	Jeżeli chcemy zobaczyć bazę z testowymi danymi możemy użyć funkcji
	
	*GenerateTestTables()* zamiast *GenerateStructure()*

Zbieranie danych
-------------------------

Aby zbierać dane i je zapisać w formacie, który pozwoli nam łatwo je dodać do bazy danych


należy skorzystać z *ClientScanner()*

.. code-block:: python
   :linenos:
   
   import ClientModule
   ClientModule.ClientScanner()

Dzięki tej opcji możemy interaktywnie dodawać dane z wykorzystaniem interfejsu tekstowego

Wybranie opcji zakończ utworzy nam plik o nazwie *dane-do-exportuNR_PRACOWNIKA.csv*

Przykładowo, jeżeli podamy nr pracownika = 3, to plik będzie nazwany *dane-do-exportu3.csv*

.. note::

	Możliwe jest dodawanie częściowych danych. Najważniejszy jest kod kreskowy produktu oraz ilość.
	
	Jeżeli wiemy, że produkt jest już w bazie danych (bądź mamy takie podejrzenie) możemy dodać kod oraz ilość.
	
	Nazwa produktu oraz opis produktu nie jest wymagany, nawet jeżeli zaznaczymy opcje dodania nazwy i opisu

-----------------------------------
Dodawanie danych do bazy danych
-----------------------------------

Możemy dodać dane do bazy w dwa różne sposoby:

	1. Import pliku
	
	2. Ręcznie dodawanie za pomocą funkcji *ServerManagment()*
	
Aby dodać dane z pliku należy:

	1. Zaimportować *ImportModule*
	
	2. Wywołać funkcję *ImportFileModule(plik)*
	
		Jeżeli nie podamy ścieżki do pliku w parametrze ``plik`` to funkcja nas zapyta o nazwę pliku.
		
		Jeżeli podamy, ale nazwa będzie błędna, funkcja zwróci błąd.

.. code-block:: python
	:linenos:
	
	import ImportModule
	plik = "dane-do-exportu1.csv"
	ImportModule.ImportFileModule(plik)

.. note::

	Dołączanie danych jest wrażliwe na datę. Co oznacza że w przypadku importu kilku różnych plików
	
	z takimi samymi produktami, najważniejsze będzie godzina WYKONANIA POMIARU, a nie godzina utworzonego pliku
	
	co oznacza, że nowsze dane będą nadpisywać starsze, a stare dane nie będą nadpisywać nowych

.. warning::
	
	Jeżeli nie jest stworzony pracownik na serwerze, import danych się nie powiedzie.
	


-------------------------------------------------
Zarządzanie danymi za pomocą ServerManagment()
-------------------------------------------------

Aby zobaczyć dane, bądź je zmodyfikować możemy użyć funkcji *ServerManagment()*

Aby to było możliwe należy:

	1. Zaimportować *ServerFunctions*
	
	2. Wywołać funkcję *ServerManagment()*

.. code-block:: python
	:linenos:
	
	import ServerFunctions
	ServerFunctions.ServerManagment()


.. note::

	Podczas edytowania danych dane będą aktualizowane natychmiastowo
	
	Jeżeli się pomylimy przy usuwaniu musimy dodać na nowo informacje
