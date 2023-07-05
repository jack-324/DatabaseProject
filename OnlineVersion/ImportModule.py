import sqlite3
import psycopg
import datetime
import simplejson

with open("hasla.txt") as db_con_file:
   creds = simplejson.loads(db_con_file.read())



def ImportFileModule(plik=""):

    connection = psycopg.connect(
             host=creds['host'],
             user=creds['user'],
             dbname=creds['dbname'],
             password=creds['passwd'],
             port=creds['port'])
    c = connection.cursor()

    if plik == "":
        plik = input("Podaj nazwe pliku do importu:")
    try:
        with open(plik) as f:
            data = f.read()
    except:
        print("Podano niepoprawny plik!")
        return 
    data2 = data.split("\n")
    del data2[-1] # Delete ostatni EMPTY srednik
    c.execute("""CREATE TEMPORARY TABLE TempImport(Nazwa varchar(128),Ilosc int, opis varchar(512),kod_kreskowy varchar(16), ID_pracownika int, 
    Data_pomiaru TIMESTAMP);""")
    
    try:
        for x in data2:
            f = x.split(';')
            importdata = [(f[0],f[1],f[2],f[3],f[4],f[5])]
            insert_query = """
                INSERT INTO TempImport (Nazwa, Ilosc, opis, kod_kreskowy, ID_pracownika, Data_pomiaru)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            insert_query = insert_query.replace("''", "NULL")  # Replace empty string ('') with NULL
            #print(insert_query, importdata)
            c.executemany(insert_query, importdata)
    except Exception as e:
        print("Failed to create the temporary table:", str(e))
        return


    try:
        errorcode="Utworzenie tranzakcji (czy cos innego dodaje w tym samym momencie?"
        #c.execute("BEGIN TRANSACTION")
        #Najpierw apdejt wszystkich obecnych produktów (tylko kodzik + ilość + pracownik + data) WHERE data_update newer or equal data_system
        errorcode="Update istniejacych produktow (Ilosc+Data+Pracownik)"
        c.execute("""UPDATE Produkty
            SET ID_pracownika = (
                SELECT ID_pracownika FROM TempImport
                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                    AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                ),
                kod_kreskowy = (
                SELECT kod_kreskowy FROM TempImport
                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                    AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                ),
                Ilosc = (
                SELECT Ilosc FROM TempImport
                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                    AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                ),
                Data_pomiaru = (
                SELECT Data_pomiaru FROM TempImport
                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                    AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                )
            WHERE EXISTS (
                SELECT 1 FROM TempImport
                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                    AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
            )""")

        #Potem Insert nowych produktów(Kodzik,Ilość,Pracownik,Data), może insert wszystkiego ? to co sie zimportuje to zimportuje
        errorcode="Dodanie nowych produktow)"
        c.execute("""    INSERT INTO Produkty (Nazwa, ilosc, opis, kod_kreskowy, ID_pracownika, Data_pomiaru)
            SELECT t.Nazwa, t.ilosc, t.opis, t.kod_kreskowy, t.ID_pracownika, t.Data_pomiaru
            FROM TempImport t
            WHERE NOT EXISTS (
                SELECT 1 FROM Produkty p
                WHERE p.kod_kreskowy = t.kod_kreskowy
            )""")


        #Potem update Nazwy produktu dla wszystkich, jeżeli Nazwa_produktu_new len > 2 and data newer OR equal
        #Potem update Opis produktu jezeli Opis_produktu_new len > 2 and data newer OR equal
        errorcode="Aktualizacja nazw"


        c.execute("""UPDATE Produkty
                SET nazwa = (
                        SELECT nazwa FROM TempImport
                        WHERE LENGTH(TempImport.nazwa) >= 2
                        AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                        AND TempImport.Data_pomiaru >= Produkty.Data_pomiaru)
                WHERE EXISTS (
                                SELECT 1 FROM TempImport
                                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                                        AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                                        )""")
        errorcode="Aktualizacja opisow"
        c.execute("""UPDATE Produkty
                SET opis = (
                        SELECT opis FROM TempImport
                        WHERE LENGTH(TempImport.opis) >= 2
                        AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                        AND TempImport.Data_pomiaru >= Produkty.Data_pomiaru)
                WHERE EXISTS (
                                SELECT 1 FROM TempImport
                                WHERE TempImport.Data_pomiaru >= Produkty.Data_pomiaru
                                        AND TempImport.kod_kreskowy = Produkty.kod_kreskowy
                                        )""")
    except Exception as e:
        print("Cos poszlo nie tak! Kod bledu:" +str(errorcode) + str(e))
        c.execute("ROLLBACK")
        return

    c.execute("COMMIT")
    print("Import pomyslny!")
    c.close()
    connection.close()
    return

if __name__ == "__main__":
    ImportFileModule()