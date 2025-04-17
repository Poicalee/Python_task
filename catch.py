from idlelib.configdialog import is_int


class MojBlad(Exception):
    """Mój własny  błąd"""
    pass

def bezpieczne_dzielenie(a,b):
    try:
        c = int (a/b)
        return c
    except ZeroDivisionError:
        print(f"Nie można dzielic przez zero")    
    except TypeError:
        return "Niepoprawne typy danych - oczekiwano liczb"
    

def pobierz_liczbe():
    
    while True:
        
        x = input("Podaj liczbe całkowitą: ")
    
        try:
            if is_int(x):
                print(x)
                break
        except ValueError:
            print("Podaj liczbe int")

def ask_for_file():
    try:
        file_name = input("Podaj nazwę pliku: ")
        output_file = input("Podaj nazwę pliku do zapisu: ")
        with open(file_name,'r',encoding='utf8') as f:
            zawartosc = f.read().lower()
        with open(output_file,'w',encoding='utf8') as f:
            f.write(zawartosc)
            print(zawartosc)
    except FileNotFoundError:
        print(f"Plik nie istniej")
    except PermissionError:
        print("Brak uprawnien")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    

# bezpieczne_dzielenie(2,2)
# pobierz_liczbe()
ask_for_file()