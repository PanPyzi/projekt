## 4. moduł wypożyczalnia książek przez użytkownika 2 funkcje
## funkcja 1 (wielu zmiennych): wypożyczenie książki lub
## kilku książek równocześnie przez klienta
## funkcja 2: zwrot 1 książki przez klienta

## zablokowac mozliwosc wyporzyczenia tej samej ksiazki 2 razy
"""
Modul umozliwiajacy wypozyczenie i zwrocenie ksiazki
"""


import csv,time

def loan(id,*args):
    print(args)
    books = dict()
    h=0
    with open('database\\book.csv', 'r', newline='') as csvfile:
        fieldnames = ['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED']
        read = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in read:
            print(row)
            for a in args:
                if row['TITLE']==a:
                    h+=1
                    books[row['ID']] = row



    with open('database\\'+id+'.csv', 'a', newline='') as csvfile:
        fieldnames = ['ID', 'AUTHOR', 'TITLE','OUT','BACK']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for line in books:
            print(line)
            print(books[line])
            try:
                writer.writerow({'ID':books[line]['ID'],'AUTHOR':books[line]['AUTHOR'], 'TITLE':books[line]['TITLE'],'OUT':time.strftime("%d/%b/%Y",time.gmtime()),'BACK':'*'})
            except(ValueError):
                print("Blad zapisu do pliku")

def ret(id,title):
    h=0
    books = dict()
    with open('database\\'+id+'.csv', 'r', newline='') as csvfile:
        read = csv.DictReader(csvfile)
        a=0
        for row in read:
            a+=1
            if row['TITLE'] == title and row['BACK']=='*':
                h += 1
                books[a] = row
                books[a]['BACK']=time.strftime("%d/%b/%Y", time.gmtime())
            else:
                books[a] = row
        if h <1:
            print("Title or client not found")
            return 0

    with open('database\\'+id+'.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'AUTHOR', 'TITLE', 'OUT', 'BACK']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in books:
            print(line)
            print(books[line])
            try:
                writer.writerow(books[line])
            except(ValueError):
                print("Blad zapisu do pliku")


