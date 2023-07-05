import sqlite3
def GenerateTestTables():
    connection = sqlite3.connect('baza.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE Produkty(ID_produktu INTEGER PRIMARY KEY AUTOINCREMENT ,Nazwa varchar(128),Ilosc int, opis varchar(512),kod_kreskowy varchar(16) UNIQUE, ID_pracownika int FOREIGN_KEY, Data_pomiaru datetime);""")
    c.execute("""INSERT INTO Produkty (Nazwa,ilosc,opis,kod_kreskowy,ID_pracownika,Data_pomiaru) VALUES("Woda gazowana Muszynianka",1,"","5901520000059",1,DateTime('now'));""")
    c.execute("""CREATE TABLE Pracownicy(ID_pracownika INTEGER PRIMARY KEY AUTOINCREMENT, Imie varchar(64), Nazwisko varchar(64), Data_zatrudnienia datetime, Is_zatrudniony int);""")
    c.execute("""INSERT INTO Pracownicy (Imie,Nazwisko,Data_zatrudnienia,Is_zatrudniony) VALUES ("Janek", "Frankowski", DateTime('now'), 1);""")
    c.execute("""INSERT INTO Pracownicy VALUES (0,"System", "System", DateTime('now'), 1);""") #System
    c.execute("COMMIT")
    c.close()
    connection.close()
def FillTestData():
    connection = sqlite3.connect('baza.db')
    c = connection.cursor()
    c.execute("""INSERT INTO Produkty (Nazwa,ilosc,opis,kod_kreskowy,ID_pracownika,Data_pomiaru) VALUES("Woda gazowana Muszynianka",1,"","5901520000059",1,DateTime('now'));""")
    c.execute("""INSERT INTO Pracownicy (Imie,Nazwisko,Data_zatrudnienia,Is_zatrudniony) VALUES ("Janek", "Frankowski", DateTime('now'), 1);""")
    c.execute("COMMIT")
    c.close()
    connection.close()
def GenerateStructure():
    connection = sqlite3.connect('baza.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE Produkty(ID_produktu INTEGER PRIMARY KEY AUTOINCREMENT ,Nazwa varchar(128),Ilosc int, opis varchar(512),kod_kreskowy varchar(16) UNIQUE, ID_pracownika int FOREIGN_KEY, Data_pomiaru datetime);""")
    c.execute("""CREATE TABLE Pracownicy(ID_pracownika INTEGER PRIMARY KEY AUTOINCREMENT, Imie varchar(64), Nazwisko varchar(64), Data_zatrudnienia datetime, Is_zatrudniony int);""")
    c.execute("""INSERT INTO Pracownicy VALUES (0,"System", "System", DateTime('now'), 1);""") #System
    c.execute("COMMIT")
    c.close()
    connection.close()
if __name__ == "__main__":
    GenerateStucture()
