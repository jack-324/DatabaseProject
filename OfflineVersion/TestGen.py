import datetime
now = datetime.datetime.now()
tablica = {}
tablica["1234"] = ['Wuda', '4', '', '1234', '1', now]
tablica["1235"] = ['Vodka', '2', '', '1235', '1', now]


with open("dane-do-exportu.csv", encoding="UTF-8", mode="w+") as f:
    string = ""
    for x in tablica.values():
        for y in x:
            string = string + str(y)+";"
            print(y)
        string = string +"\n"
    f.write(string)

