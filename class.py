#Zadanie 1
class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole(self):
        return self.dlugosc * self.szerokosc

    def obwod(self):
            return 2 * (self.dlugosc + self.szerokosc)

    def czy_kwadrat(self):
        if self.dlugosc == self.szerokosc:
            return True


prost = Prostokat(10,10)
print(prost.pole())
print(prost.obwod())
print(prost.czy_kwadrat())

#Zadanie 2
class Konto:
    def __init__(self, numer, wlasciciel, saldo):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        saldo = 0
        
    def wplac(self, kwota):
        self.saldo += kwota
        return self.saldo
    
    def wyplac(self, kwota):
        
        if self.saldo > kwota:
            self.saldo -= kwota
            return self.saldo
        else:
            print("Brak środków")
            return self.saldo
    
    def info(self):
        print(self.numer, self.wlasciciel, self.saldo)
        
konto = Konto(123, "Karol", 10000)
konto.info()
konto.wplac(10000)
konto.wyplac(5000)
konto.info()


#Zadanie 3

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.wypozyczona = False

    def __str__(self):
        return f"'{self.tytul}' by {self.autor} ({self.rok_wydania})"


class Czytelnik:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wypozyczone_ksiazki = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Biblioteka:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.ksiazki = []

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def wypozycz(self, ksiazka, czytelnik):
        if ksiazka in self.ksiazki and not ksiazka.wypozyczona:
            ksiazka.wypozyczona = True
            czytelnik.wypozyczone_ksiazki.append(ksiazka)
            print(f"Książka {ksiazka} została wypożyczona przez {czytelnik}.")
        else:
            print(f"Książka {ksiazka} jest niedostępna.")

    def zwroc(self, ksiazka, czytelnik):
        if ksiazka in czytelnik.wypozyczone_ksiazki:
            ksiazka.wypozyczona = False
            czytelnik.wypozyczone_ksiazki.remove(ksiazka)
            print(f"Książka {ksiazka} została zwrócona przez {czytelnik}.")
        else:
            print(f"{czytelnik} nie posiada książki {ksiazka}.")


biblioteka = Biblioteka("Biblioteka Miejska",)
ks1 = Ksiazka("Lalka", "Bolesław Prus", 1890)
ks2 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)
czytelnik1 = Czytelnik("Jan", "Kowalski")

# Dodanie książek do biblioteki
biblioteka.dodaj_ksiazke(ks1)
biblioteka.dodaj_ksiazke(ks2)

# Wypożyczenie i zwrot
biblioteka.wypozycz(ks1, czytelnik1)
biblioteka.zwroc(ks1, czytelnik1)