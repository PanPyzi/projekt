################# Task
## Folder Library zawiera 3 pliki zawierające następujące dane:
## book.csv - dane książek
## address.csv - adres klientów
## customer.csv - dane osobowe klientów

## Twoim zadaniem jest utworzenie pakietu obsługi klienta w wypożyczalni
## Utwórz następujące moduły:
## 1. moduł main - moduł główny (administracja zasobami wypożyczalni)



## 2. moduł obsługi klienta zawierający 4 funkcje
## funkcja 1: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## funkcja 2: usuwanie danych klienta względem ID lub NAME
## funkcja 3: rejestracja nowego klienta
## (klient podaje swoje dane, nadawany jest losowo numer ID (3 cyfry))
## w folderze DATABASE utworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego będą zapisywane dane wypożyczonej książki oraz
## data wypożyczenia a potem zwrotu książki



## 3. moduł obsługi książek zawierający 1 funkcję:
## funkcja 1: dodanie nowej książki do bazy (book.csv)

## 4. moduł wypożyczalnia książek przez użytkownika 2 funkcje
## funkcja 1 (wielu zmiennych): wypożyczenie książki lub
## kilku książek równocześnie przez klienta
## funkcja 2: zwrot 1 książki przez klienta

## WYMAGANIA:
## - możesz programować wyłącznie w paradygmacie funkcyjnym
## - utwórz conajmniej 1 funkcję wyższego rzędu
## - wykonaj dokumentację dla conajmniej 1 funkcji i 1 modułu
## - conajmniej 2 razy wykonaj obsługę wyjątku

## WSKAZANIA:
## - możesz zwiększyć liczbę modułów
## - dla zapisu/odczytu daty wykorzystaj odpowiedni pakiet time
from library import book,klient,wyp
import random


while True:
    print("                   BIBLIOTEKA \n 1.Dodanie klienta\n 2.Rejestracja klienta\n"
          " 3.Usuwanie danych klienta\n 4.Dodanie nowej ksiazki\n "
          "5.Wyporzyczenie \n 6.zwrot")
    choice=input("Podaj numer:")
    match choice:
        case "1":
            name = input("Imie: ")
            email = input("Email: ")
            phone = input("Telefon: ")
            street = input("Ulica: ")
            city = input("Miasto: ")
            country = input("Panstwo: ")
            klient.add(random.randint(100, 1000),name,email,phone,street,city,country)

        case "2":
            name = input("Imie: ")
            email = input("Email: ")
            phone = input("Telefon: ")
            street = input("Ulica: ")
            city = input("Miasto: ")
            country = input("Panstwo: ")
            klient.register(klient.add,name, email, phone, street, city, country)

        case "3":
            data = input("Imie/ID: ")
            klient.remove(data)

        case "4":
            autor = input("Autor: ")
            title = input("Tytol: ")
            pages = input("Strony: ")
            book.add(autor,title,pages)

        case "5":
            id= input("Podaj id klienta: ")
            tytul = input("W przypadku kilku ksiazek: tytul,tytul2,tytul3 \nTytuly: ")
            wyp.loan(id,tytul.split(","))

        case "6":
            id = input("Podaj id klienta: ")
            tytul = input("Tytul: ")
            wyp.ret(id,tytul)




















