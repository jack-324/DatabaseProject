def ClientScanner():
    import datetime
    numerek = input("Podaj swoj numer pracownika: ")
    slownik = {}
    while (True):
        print("""Menu wyboru:
        1.Dodaj/edytuj
        2.Usun
        3.Zakoncz
        0.Proste dodanie (sam kod + ilosc)""")
        kb = input("Wybierz numer:")
        if kb==str(0):
            kod = input("Podaj kod kreskowy (zeskanuj)")
            ilosc = input("Podaj ilosc produktu:")
            slownik[kod] = ['',ilosc,'',kod,numerek,data]
        if kb==str(1):
            kod = input("Podaj kod kreskowy (zeskanuj)")
            ilosc = input("Podaj ilosc produktu:")
            nazwa = input("Podaj nazwe produktu:")
            opis = input("Podaj opis produktu (opcjonalnie):")
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            slownik[kod] = [nazwa,ilosc,opis,kod,numerek,data]
            print("Dodano: "+ str(slownik[kod]))
        if kb==str(2):
            kod = input("Podaj kod kreskowy (zeskanuj)")
            try:
                del slownik[kod]
            except:
                print("Nie odnaleziono lokalnie produktow")
        if kb==str(3):
            with open("dane-do-exportu"+str(numerek)+ ".csv", encoding="UTF-8", mode="a+") as f:
                string = ""
                for x in slownik.values():
                    for y in x:
                        string = string + str(y)+";"
                        #print(y)
                    string = string +"\n"
                f.write(string)

            return string

if __name__ == "__main__":
    ClientScanner()
