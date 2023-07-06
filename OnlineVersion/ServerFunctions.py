import sqlite3
import datetime
#try:
#    import psycopg
#except:
#    pass

#try:
#    with open("hasla.txt") as f:
#        dane = simplejson.loads(f.read())
#except:
#    pass

#connection = psycopg.connect(host = dane["host"],user = dane["user"],dbname = dane["dbname"],password = dane["passwd"],port = dane["port"])
#connection = sqlite3.connect('baza.db')
#c = connection.cursor()

import psycopg
import simplejson

with open("hasla.txt") as db_con_file:
   creds = simplejson.loads(db_con_file.read())






#Zarzadzanie produktem
def Zarzadz_produktem(c):
    while True:
        print("""Edycja produktow:
    1.Wypisz dane o produckcie o podanym kodzie kreskowym
    2.Wypisz dane o produckcie o podanym ID
    3.Usun produkt o podanym kodzie kreskowym
    4.Usun produkt o podanym ID
    5.Sprawdz jakie produkty nie posiadaja przypisanej nazwy
    6.Sprawdz jakie produkty nie posiadaja opisu
    7.Dodaj produkt
    8.Wypisz wszystkie produkty
    0.Powrot""")
        inp = input("Podaj wybor:")
        if inp == str(0):
            return
# Print Data
        elif inp == str(1):
            inp = input("Podaj kod:")
            try:
                c.execute("SELECT * FROM Produkty,Pracownicy WHERE kod_kreskowy = "+str(inp)+" AND Pracownicy.ID_pracownika = Produkty.ID_Pracownika;")
                x = list(c.fetchone())
                for a in range(len(x) - 1):
                    if x[a] == None:
                        x[a] = "Brak Danych."
                if len(x) < 1:
                    print("Nie odnaleziono produktu!")
                    raise Error("Nie odnaleziono podanych danych")
                print("=========================")
                print("ID produktu:" + str(x[0]))
                print("Nazwa prod.:" + str(x[1]))
                print("Ilosc prod.:" + str(x[2]))
                print("Opis prod.:" + str(x[3]))
                print("Kod kresk.:" + str(x[4]))
                print("Data wpisu:" + str(x[6]))
                print("Imie prac.:" + str(x[8]))
                print("Nazw prac.:" + str(x[9]))
                print("=========================")
                input("Wcisnij [ENTER] aby kontynuowac")
            except Exception as e:
                print(e)
                print("Wystapil blad w zapytaniu do bazy!")
                c.execute("ROLLBACK")
        elif inp == str(2):
            inp = input("Podaj kod:")
            try:
                c.execute("SELECT * FROM Produkty,Pracownicy WHERE ID_produktu = "+str(inp)+" AND Pracownicy.ID_pracownika = Produkty.ID_Pracownika;")

                x = list(c.fetchone())
                for a in range(len(x) - 1):
                    if x[a] == None:
                        x[a] = "Brak Danych."
                if len(x) < 1:
                    print("Nie odnaleziono produktu!")
                    raise Error("Nie odnaleziono podanych danych")
                print("=========================")
                print("ID produktu:" + str(x[0]))
                print("Nazwa prod.:" + str(x[1]))
                print("Ilosc prod.:" + str(x[2]))
                print("Opis prod.:" + str(x[3]))
                print("Kod kresk.:" + str(x[4]))
                print("Data wpisu:" + str(x[6]))
                print("Imie prac.:" + str(x[8]))
                print("Nazw prac.:" + str(x[9]))
                print("=========================")
                input("Wcisnij [ENTER] aby kontynuowac")
            except Exception as e:
                print(e)
                print("Wystapil blad w zapytaniu do bazy!")
# Delete Data
        elif inp == str(3):
            inp = input("Podaj kod:")
            try:
                c.execute("DELETE FROM Produkty WHERE kod_kreskowy = "+str(inp))
                if c.rowcount < 1:
                    print("Nie odnaleziono podanego produktu!")
                    raise Error("Nie odnaleziono podanych danych")
                print("Usunieto dane!")
                c.execute("COMMIT")
            except Exception as e:
                print(e)
                print("Wystapil blad przy usuwaniu danych!")
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(4):
            inp = input("Podaj kod:")
            try:
                c.execute("DELETE FROM Produkty WHERE ID_produktu = "+str(inp))
                if c.rowcount < 1:
                    print("Nie odnaleziono podanego produktu!")
                    raise Error("Nie odnaleziono podanych danych")
                print("Usunieto dane!")
                c.execute("COMMIT")
            except Exception as e:
                print(e)
                print("Wystapil blad przy usuwaniu danych!")
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(5):
            c.execute("SELECT ID_produktu, kod_kreskowy,Nazwa FROM Produkty WHERE Nazwa IS NULL")
            for x in c.fetchall():
                print("ID:"+str(x[0])+" Kod:"+str(x[1]))
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(6):
            c.execute("SELECT ID_produktu, kod_kreskowy,Opis FROM Produkty WHERE Opis IS NULL")
            for x in c.fetchall():
                print("ID:"+str(x[0])+" Kod:"+str(x[1]))
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(7):
            kod = input("Podaj kod kreskowy (zeskanuj)")
            ilosc = input("Podaj ilosc produktu:")
            nazwa = input("Podaj nazwe produktu:")
            opis = input("Podaj opis produktu (opcjonalnie):")
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            importdata = [(nazwa,ilosc,opis,kod,data)]
            try:
                c.executemany("INSERT INTO Produkty (Nazwa,ilosc,opis,kod_kreskowy,ID_pracownika,Data_pomiaru) VALUES(%s, %s, %s,%s,0,%s)",importdata)
                print("Dodano produkt!")
                c.execute("COMMIT")
            except Exception as e:
                pass
                if "duplicate key" in str(e):
                    importdata = [(nazwa,ilosc,opis,kod,data,kod)]
                    c.execute("ROLLBACK")
                    c.executemany("UPDATE Produkty SET Nazwa = %s,ilosc = %s, opis = %s, kod_kreskowy = %s, ID_pracownika = 0, Data_pomiaru = %s WHERE kod_kreskowy = %s",importdata)
                    print("Zaktualizowano produkt!")
                    c.execute("COMMIT")
                else:
                    print(e)
                    print("Blad dodania produktu!")
            input("Wcisnij [ENTER] aby kontynuowac")
            
                
            
            #c.execute("""INSERT INTO Produkty (Nazwa,ilosc,opis,kod_kreskowy,ID_pracownika,Data_pomiaru) VALUES("Woda gazowana Muszynianka",1,"","5901520000059",1,DateTime('now'));""")

        elif inp == str(8):
            try:
                c.execute("SELECT * FROM Produkty,Pracownicy WHERE Produkty.ID_Pracownika = Pracownicy.ID_Pracownika")
                for x in c.fetchall():
                    print(x)
            except Exception as e:
                print(e)
                print("Cos poszlo nie tak!")
            input("Wcisnij [ENTER] aby kontynuowac")
    


def Zarzadz_pracownikiem(c):
    while True:
        print("""Edycja pracowników:
    1.Wypisz dane o pracowniku o podanym ID
    2.Wypisz dane o wszystkich pracownikach
    3.Wypisz dane o pracowniku o podanym Nazwisku
    4.Zwolnij pracownika o podanym ID
    5.Wypisz dane o wszystkich obecnie zatrudnionych pracownikach
    6.Zatrudnij pracownika
    0.Powrot""")
        inp = input("Podaj wybor:")
        if inp == str(0):
            return
        elif inp == str(2):
            try:
                c.execute("SELECT * FROM Pracownicy")
                for x in c.fetchall():
                    print(x)
            except Exception as e:
                print(e)
                print("Cos poszlo nie tak!")
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(5):
            try:
                c.execute("SELECT * FROM Pracownicy WHERE Is_Zatrudniony = 1")
                for x in c.fetchall():
                    print(x)
            except Exception as e:
                print(e)
                print("Cos poszlo nie tak!")
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(1):
            inp = input("Podaj kod:")
            try:
                c.execute("SELECT * FROM Pracownicy WHERE ID_pracownika ="+str(inp)+";")

                x = list(c.fetchone())
                for a in range(len(x) - 1):
                    if x[a] == None:
                        x[a] = "Brak Danych."
                if len(x) < 1:
                    print("Nie odnaleziono pracownika!")
                    raise Error("Nie odnaleziono podanych danych")
                if str(x[4]) == "1":
                    x[4] = "TAK"
                else:
                    x[4] = "NIE"
                print("=========================")
                print("ID pracownika:" + str(x[0]))
                print("Imie pracown.:" + str(x[1]))
                print("Nazw. pracown:" + str(x[2]))
                print("Data zatrudn.:" + str(x[3]))
                print("Czy jest zatrudniony%s " + str(x[4]))
                print("=========================")
                input("Wcisnij [ENTER] aby kontynuowac")
            except Exception as e:
                print(e)
                print("Wystapil blad w zapytaniu do bazy!")
        elif inp == str(3):
            inp = input("Podaj nazwisko:")
            try:
                #print("SELECT * FROM Pracownicy WHERE Nazwisko = "+str(inp)+";")
                c.execute("SELECT * FROM Pracownicy WHERE nazwisko ='"+str(inp)+"';")

                x = list(c.fetchone())
                for a in range(len(x) - 1):
                    if x[a] == None:
                        x[a] = "Brak Danych."
                if len(x) < 1:
                    print("Nie odnaleziono pracownika!")
                    raise Error("Nie odnaleziono podanych danych")
                if str(x[4]) == "1":
                    x[4] = "TAK"
                else:
                    x[4] = "NIE"
                print("=========================")
                print("ID pracownika:" + str(x[0]))
                print("Imie pracown.:" + str(x[1]))
                print("Nazw. pracown:" + str(x[2]))
                print("Data zatrudn.:" + str(x[3]))
                print("Czy jest zatrudniony%s " + str(x[4]))
                print("=========================")
                input("Wcisnij [ENTER] aby kontynuowac")
            except Exception as e:
                print(e)
                print("Wystapil blad w zapytaniu do bazy!")
        elif inp == str(4):
            inp = input("Podaj kod:")
            if str(inp) == "0":
                print("Nie można usunąć systemowego pracownika!")
                raise Error("Proba usunieca pracownika SYSTEM")
            try:
                importdata = [tuple(inp)]
                c.executemany("UPDATE Pracownicy SET Is_zatrudniony = 0 WHERE ID_pracownika = %s;",importdata)
                if c.rowcount < 1:
                    print("Nie odnaleziono podanego pracownika!")
                    raise Error("Nie odnaleziono podanych danych")
                print("Usunieto dane!")
                c.execute("COMMIT")
            except Exception as e:
                print(e)
                print("Wystapil blad przy usuwaniu danych!")
            input("Wcisnij [ENTER] aby kontynuowac")
        elif inp == str(6):
            imie = input("Podaj imie pracownika")
            nazwisko = input("Podaj nazwisko pracownika")
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            importdata = [(imie,nazwisko,data)]
            try:
                c.executemany("INSERT INTO Pracownicy (Imie,Nazwisko,Data_zatrudnienia,Is_zatrudniony) VALUES(%s, %s, %s,1)",importdata)
                print("Dodano pracownika!")
                c.execute("COMMIT")
            except Exception as e:
                print(e)
                print("Blad dodania pracownika!")
            input("Wcisnij [ENTER] aby kontynuowac")




def ServerManagment():
    connection = psycopg.connect(
        host=creds['host'],
        user=creds['user'],
        dbname=creds['dbname'],
        password=creds['passwd'],
        port=creds['port'])
    c = connection.cursor()
    while True:
        print("""Menu wyboru:
        1.Pokaz wszystkie produkty (Tylko nazwa i ilosc)
        2.Zarzadzanie produktami
        3.Zarzadzanie pracownikami
        4.Drop_Table
        0.Wyjscie""")
        inp = input("Podaj wybor:")
        if inp == str(0):
            try:
                c.execute("COMMIT") #Tak dla pewnosci
            except:
                pass
            c.close()
            connection.close()
            print("Rozlaczono z baza!")
            return
        if inp == str(1):
            c.execute("SELECT Nazwa,Ilosc FROM Produkty;")
            for x in c.fetchall():
                print(x)
            
            input("Wcisnij [ENTER] aby kontynuowac")
        if inp == str(2):
            Zarzadz_produktem(c)
        if inp == str(3):
            Zarzadz_pracownikiem(c)
        if inp == str(4):
            Drop_Table(c)
        
def Drop_Table(c):
    while True:
        print("""Menu wyboru:
            1.Drop Table Pracownicy
            2.Drop Table Produkty
            0.Wyjscie""")
        inp = input("Podaj wybor:")
        if inp == str(0):
            return
        if inp == str(1):
            try:
                # Drop the "Pracownicy" table if it exists
                c.execute("DROP TABLE IF EXISTS Pracownicy")
                c.execute("COMMIT")
            except:
                pass
            print("Usunieto tabele Pracownicy")
            return
        if inp == str(2):
            try:
                # Drop the "Produkty" table if it exists
                c.execute("DROP TABLE IF EXISTS Produkty")
                c.execute("COMMIT")
            except:
                pass
            print("Usunieto tabele Produkty")
            return

if __name__ == "__main__":
    ServerManagment()
