## 2. moduł obsługi klienta zawierający 4 funkcje
## funkcja 1: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## funkcja 2: usuwanie danych klienta względem ID lub NAME
## funkcja 3: rejestracja nowego klienta
## (klient podaje swoje dane, nadawany jest losowo numer ID (3 cyfry))
## w folderze DATABASE utworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego będą zapisywane dane wypożyczonej książki oraz
## data wypożyczenia a potem zwrotu książki

## 2. moduł obsługi klienta zawierający 4 funkcje
## funkcja 1: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv

import csv,random,time

def add(id,name,email,phone,street,city,country):

    with open('database\\customer.csv', 'a', newline='') as csvfile:
        fieldnames = ['ID','NAME','E-MAIL','PHONE','CREATED','UPDATED']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()#
        created = time.strftime("%d/%b/%Y", time.gmtime())
        writer.writerow({'ID': id, 'NAME': name, 'E-MAIL': email, 'PHONE': phone, 'CREATED': created, 'UPDATED': created})

    with open('database\\address.csv', 'a', newline='') as csvfile:
        fieldnames = ['ID','STREET','CITY','COUNTRY']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()#ID,STREET,CITY,COUNTRY
        writer.writerow({'ID': id, 'STREET': street, 'CITY': city, 'COUNTRY': country})

    ## funkcja 3: rejestracja nowego klienta

def register(function,name,email,phone,street,city,country):
    id=random.randint(100, 1000)
    function(id,name,email,phone,street,city,country)
    with open('database\\'+str(id)+'.csv', 'a', newline='') as csvfile:
        fieldnames = ['ID', 'AUTHOR', 'TITLE','OUT','BACK']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()


## funkcja 2: usuwanie danych klienta względem ID lub NAME

def remove(dane):
    write=dict()
    with open('database\\customer.csv', mode='r') as csvfile:
        read = csv.DictReader(csvfile)  # each line as dict
        for row in read:
            if (row['NAME']!=dane and row['ID']!=dane):
                #print(row)
                write[row['ID']]=row

    with open('database\\customer.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for line in write:
            #print(write[line]['ID'])
            writer.writerow(write[line])

    writeaddr = dict()
    with open('database\\address.csv', 'r', newline='') as csvfile:
        fieldnames = ['ID','STREET','CITY','COUNTRY']
        read = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in read:
            for line in write:
                if row['ID']==line:
                    writeaddr[row['ID']]=row

    with open('database\\address.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID','STREET','CITY','COUNTRY']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for line in writeaddr:
            #print(line)
            #print(writeaddr[line])
            writer.writerow(writeaddr[line])
