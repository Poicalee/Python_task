from xml.etree.ElementTree import XMLParser


def operators(name):
    a = 10
    h = 5
    
    area = 0.5 * h * a
    print(area)

    x = 15
    y = 4
    
    print(x//y)
    print(x%y)
    print(x**y)

    wiek = 19
    warunek = (wiek >= 18) and (wiek < 65)
    
    print(warunek) 

if __name__ == '__main__':
    operators('PyCharm')