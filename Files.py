#Zadanie 1
def files():
    with open('przyklady.txt','w',encoding='utf8') as f:
        f.write("To jest pierwsza linia\n")
        f.write("To jest druga linia\n")
        f.write("To jest trzecia linia")
    
    with open('przyklady.txt','r',encoding='utf8') as f:
         zawartosc = f.read()
         print(zawartosc)

#Zadanie 2
def copy_file():
    try:
     with open('przyklady.txt','r',encoding='utf8') as f:
        zawartosc = f.read()
        with open('przyklady2.txt','w',encoding='utf8') as f:
            f.write(zawartosc)
            print(zawartosc)
    except FileNotFoundError:
        print(f"Plik nie istniej")
        return 0

#Zadanie 3        
def ask_for_file():
    try:
        file_name = input("Podaj nazwę pliku: ")
        with open(file_name,'r',encoding='utf8') as f:
            zawartosc = f.read()
            slowa = zawartosc.split()
            print(zawartosc)
            print(len(slowa))
            return len(slowa)
    except FileNotFoundError:
        print(f"Plik nie istniej")
        
    
    
# files()
# copy_file()
ask_for_file()