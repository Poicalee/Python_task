
def Loop(name):
    
    sum = 0
    
    for i in range(1,101):
        sum += i
       
    print(sum)
    
    i = 0
    power = 2
    while(power < 1000):
        i += 1
        power = 2**i
    
    print(i)

    liczby = [12, 5, 8, 21, 13, 7]
    najwieksza = 0
    
    for liczba in liczby:
        if liczba > najwieksza:
            najwieksza = liczba
    
    print(najwieksza)

if __name__ == "__main__":
    Loop("PyCharm")