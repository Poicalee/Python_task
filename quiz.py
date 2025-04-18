# Usuń niepotrzebne importy
# from dataclasses import dataclass
# from instructions import instructions
import json
import random
import datetime

class Pytanie:
    def __init__(self, tresc, odpowiedzi, poprawna_odpowiedz, punkty=1):
        self.tresc = tresc
        self.odpowiedzi = odpowiedzi
        self.poprawna_odpowiedz = poprawna_odpowiedz  # To jest atrybut
        self.punkty = punkty

    def sprawdz_odpowiedz(self, odpowiedz_uzytkownika):  # Zmieniona nazwa metody
        return self.poprawna_odpowiedz == odpowiedz_uzytkownika

    def wyswietl(self):
        print(self.tresc)
        for i, odp in enumerate(self.odpowiedzi):
            print(f"({chr(97 + i)}) {odp}")

class Quiz:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.pytania = []
        self.wynik = 0

    def dodaj_pytanie(self, pytanie):
        self.pytania.append(pytanie)

    def wykonaj_quiz(self):
        print(f"Quiz: {self.nazwa}")
        print(f"Liczba pytan: {len(self.pytania)}")
        print("Start")

        for i, pytanie in enumerate(self.pytania):
            print(f"\nPytanie {i + 1} z {len(self.pytania)}")
            pytanie.wyswietl()

            odpowiedz = input("Twoja odpowiedz: (a, b, c, ...): ").lower()

            if 'a' <= odpowiedz <= 'z':
                indeks_odpowiedz = ord(odpowiedz) - ord('a')
                if pytanie.sprawdz_odpowiedz(indeks_odpowiedz):  # Prawidłowe wywołanie metody
                    print("Poprawna odpowiedź!")
                    self.wynik += pytanie.punkty
                else:
                    print(f"Niepoprawna odpowiedź. Prawidłowa odpowiedź to: {chr(97 + pytanie.poprawna_odpowiedz)}")
            else:
                print("Nieprawidłowy format odpowiedzi.")

        print(f"\nKoniec quizu! Twój wynik: {self.wynik}/{sum(p.punkty for p in self.pytania)}")

def wczytaj_pytania_z_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8-sig') as plik:
            dane = json.load(plik)

        pytania = []
        for p in dane["pytania"]:
            nowe_pytanie = Pytanie(
                p["tresc"],
                p["odpowiedzi"],  # Poprawiony klucz
                p["poprawna_odpowiedz"],
                p.get("punkty", 1)
            )
            pytania.append(nowe_pytanie)

        return pytania

    except FileNotFoundError:
        print(f"Nie znaleziono pliku {nazwa_pliku}")
        return []
    except json.decoder.JSONDecodeError as e:
        print(f"Błąd w formacie pliku {nazwa_pliku}: {e}")
    return []

def zapisz_wynik(nazwa_gracza, nazwa_quizu, wynik, max_wynik):
    try:
        with open("wyniki.txt", 'a', encoding='utf-8') as plik:
            data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            plik.write(f"{data} | {nazwa_gracza} | {nazwa_quizu} | {wynik}/{max_wynik}\n")  # Dodany znak nowej linii
        print("Wynik został zapisany")

    except Exception as e:  # Lepsza obsługa wyjątków
        print(f"Błąd podczas zapisywania wyniku: {e}")

def losuj_kol(quiz):
    random.shuffle(quiz.pytania)

def main():
    
    print("=== QUIZ TEKSTOWY ===")
    nazwa_gracza = input("Podaj swoje imię: ")

    # Tworzenie quizu
    moj_quiz = Quiz("Wiedza ogólna")

    # # Ręczne dodanie pytań
    # p1 = Pytanie(
    #     "Która planeta jest najbliżej Słońca?",
    #     ["Wenus", "Merkury", "Mars", "Ziemia"],
    #     1
    # )
    # moj_quiz.dodaj_pytanie(p1)
    # 
    # p2 = Pytanie(
    #     "Kto napisał 'Pan Tadeusz'?",
    #     ["Juliusz Słowacki", "Henryk Sienkiewicz", "Adam Mickiewicz", "Bolesław Prus"],
    #     2
    # )
    # moj_quiz.dodaj_pytanie(p2)

    # Można też wczytać pytania z pliku:
    pytania_z_pliku = wczytaj_pytania_z_pliku("pytania.json")
    for pyt in pytania_z_pliku:
        moj_quiz.dodaj_pytanie(pyt)

    # Losowanie kolejności pytań
    losuj_kol(moj_quiz)

    # Wykonanie quizu
    moj_quiz.wykonaj_quiz()

    # Zapisanie wyniku
    zapisz_wynik(nazwa_gracza, moj_quiz.nazwa, moj_quiz.wynik,
                 sum(p.punkty for p in moj_quiz.pytania))

if __name__ == "__main__":
    main()  # Dodany warunek uruchomienia funkcji main