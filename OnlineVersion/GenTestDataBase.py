import sqlite3
import psycopg
import simplejson

with open("hasla.txt") as db_con_file:
   creds = simplejson.loads(db_con_file.read())

#connection = sqlite3.connect('student01.db')




def GenerateTestTables():
    connection = psycopg.connect(
             host=creds['host'],
             user=creds['user'],
             dbname=creds['dbname'],
             password=creds['passwd'],
             port=creds['port'])
    c = connection.cursor()
    c.execute("""CREATE TABLE Produkty(ID_produktu SERIAL PRIMARY KEY ,Nazwa varchar(128),Ilosc int, opis varchar(512),kod_kreskowy varchar(16) UNIQUE, ID_pracownika int FOREIGN_KEY, Data_pomiaru datetime);""")
    c.execute("""INSERT INTO Produkty (Nazwa,ilosc,opis,kod_kreskowy,ID_pracownika,Data_pomiaru) VALUES("Woda gazowana Muszynianka",1,"","5901520000059",1,DateTime('now'));""")
    c.execute("""CREATE TABLE Pracownicy(ID_pracownika INTEGER PRIMARY KEY AUTOINCREMENT, Imie varchar(64), Nazwisko varchar(64), Data_zatrudnienia datetime, Is_zatrudniony int);""")
    c.execute("""INSERT INTO Pracownicy (Imie,Nazwisko,Data_zatrudnienia,Is_zatrudniony) VALUES ("Janek", "Frankowski", DateTime('now'), 1);""")
    c.execute("""INSERT INTO Pracownicy VALUES (0,"System", "System", DateTime('now'), 1);""") #System
    c.execute("COMMIT")
    c.close()
    connection.close()
def FillTestData():
    connection = psycopg.connect(
             host=creds['host'],
             user=creds['user'],
             dbname=creds['dbname'],
             password=creds['passwd'],
             port=creds['port'])
    c = connection.cursor()
    c.execute("""INSERT INTO Produkty (Nazwa,ilosc,opis,kod_kreskowy,ID_pracownika,Data_pomiaru) VALUES('Woda gazowana Muszynianka',1,'','5901520000059',1,CURRENT_TIMESTAMP);""")
    c.execute("""INSERT INTO Pracownicy (Imie,Nazwisko,Data_zatrudnienia,Is_zatrudniony) VALUES ('Janek', 'Frankowski', CURRENT_TIMESTAMP, 1);""")
    c.execute("COMMIT")
    c.close()
    connection.close()
def GenerateStructure():
    connection = psycopg.connect(
             host=creds['host'],
             user=creds['user'],
             dbname=creds['dbname'],
             password=creds['passwd'],
             port=creds['port'])
    c = connection.cursor()
    c.execute("""CREATE TABLE Pracownicy(ID_pracownika SERIAL PRIMARY KEY, Imie varchar(64), Nazwisko varchar(64), Data_zatrudnienia TIMESTAMP, Is_zatrudniony int);""")
    c.execute("""CREATE TABLE Produkty(ID_produktu SERIAL PRIMARY KEY ,Nazwa varchar(128),Ilosc int, opis varchar(512),kod_kreskowy varchar(16) UNIQUE, ID_pracownika int REFERENCES Pracownicy(ID_pracownika), Data_pomiaru TIMESTAMP);""")
    c.execute("""INSERT INTO Pracownicy (Imie,Nazwisko,Data_zatrudnienia,Is_zatrudniony) VALUES ('System', 'System', CURRENT_TIMESTAMP, 1);""") #System
    c.execute("COMMIT")
    c.close()
    connection.close()
