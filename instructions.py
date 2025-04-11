
def instructions(name):
    
    liczba = 7
    
    
    if(liczba % 2 == 0):
        print("Parzysta")
    else:
        print("Nieparzysta")

    a = 5
    b = 5
    c = 5
    
    if(a == b and b == c):
        print("Równoboczny")
    elif(a == b or c == b or a == c):
        print("Równoramienny")
    else:
        print("Różnoboczny")
    
    temperatura = 25
    
    if(temperatura < 0):
        print("Mróz")
    elif(temperatura >= 0 and temperatura < 10):
        print("Zimno")
    elif(temperatura >= 10 and temperatura < 20):
        print("Chłodno")
    elif(temperatura >= 20 and temperatura < 30):
        print("Ciepło")
    else:
        print("Gorąco")

if __name__ == '__main__':
    instructions('PyCharm')
    