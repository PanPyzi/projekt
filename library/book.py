## 3. moduł obsługi książek zawierający 1 funkcję:
## funkcja 1: dodanie nowej książki do bazy (book.csv)

import csv,time


def add(author,title,pages):
    """""
        funkcja do dodania ksiazki do bazy danych
    Args:
        author: autor ksiazki
        title: tytol ksiazki
        pages: ilosc stron
    """
    with open('database\\book.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # each line as dict
        for row in enumerate(csv_reader):
            idd=row[0]


    with open('database\\book.csv', 'a', newline='') as csvfile:
        fieldnames = ['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        created = time.strftime("%d/%b/%Y", time.gmtime())
        # writer.writeheader()
        writer.writerow({'ID': idd+102, 'AUTHOR': author, 'TITLE': title, 'PAGES': pages, 'CREATED': created, 'UPDATED': created})
