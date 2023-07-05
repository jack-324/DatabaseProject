import sqlite3
def ImportFileModule(plik=""):

    #connection = psycopg.connect(host = dane["host"],user = dane["user"],dbname = dane["dbname"],password = dane["passwd"],port = dane["port"])
    connection = sqlite3.connect('baza.db')
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
    c.execute("""CREATE TEMPORARY TABLE TempImport(Nazwa varchar(128),Ilosc int, opis varchar(512),kod_kreskowy varchar(16), ID_pracownika int FOREIGN_KEY, Data_pomiaru datetime);""")

    try:
        for x in data2:
            f = x.split(';')
            #print(f[0])
            #print(f[1])
            #print(f[2])
            #print(f[3])
            #print(f[4])
            #print(f[5])
            #print(x)
            #print('INSERT INTO TempImport VALUES("'+str(f[0])+'",' + str(f[1])+ ',"' + str(f[2]) + '","' + str(f[3]) + '",' + str(f[4])+ ',"'+str(f[5])+ '");')
            c.execute('INSERT INTO TempImport VALUES("'+str(f[0])+'",' + str(f[1])+ ',"' + str(f[2]) + '","' + str(f[3]) + '",' + str(f[4])+ ',"'+str(f[5])+ '");')
        #fa: 0 nazwa,1 ilosc,2 opis,3 kod_kreskowy,4 _numerek_pracownika_,5 data_pomiaru
    except:
        print("Nie udalo sie utworzyc tabeli pomocniczej")
        exit()
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
    except:
        print("Cos poszlo nie tak! Kod bledu:" +str(errorcode))
        c.execute("ROLLBACK")
        return

    c.execute("COMMIT")
    print("Import pomyslny!")
    c.close()
    connection.close()
    return

if __name__ == "__main__":
    ImportFileModule()
