from typing import Reversible


def pole_prostkata(dlugosc,szerokosc):
    print(dlugosc*szerokosc) 
    return dlugosc*szerokosc

def czy_palindrom(slowo):
    if slowo == slowo[::-1]:
        return True
    else:
        return False

def zlicz_slowa(tekst):
    tekst = tekst.lower()
    slowa = tekst.split()
    
    licznik = {}
    
    for slowo in slowa:
        slowo = slowo.strip(".,!?;:()[]{}\"'")
        if slowo:
            licznik[slowo] = licznik.get(slowo,0) + 1 
    return licznik

        

# Wywołanie funkcji
pole_prostkata(2,3)
pole_prostkata(5,10)
pole_prostkata(13,12)

print(czy_palindrom("kajak"))   # True
print(czy_palindrom("level"))   # True
print(czy_palindrom("python"))  # False
print(czy_palindrom("anna"))    # True
print(czy_palindrom("kot"))

tekst = "Ala ma kota. Ala ma psa! Psa ma też Ola."
wynik = zlicz_slowa(tekst)
print(wynik) 
