# This is a sample Python script.
from idlelib.colorizer import prog_group_name_to_tag


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def info(name):
    # Use a breakpoint in the code line below to debug your script.
    
    imie = "Karol"
    wiek = 22
    prog = True
    
    print(imie,type(imie))
    print(wiek,type(wiek))
    print("Lubie programować: ",prog,type(prog))
    
    a = 10
    b = 20
    
    c = float(a +b)
    
    print(c,type(c))
    
    temperatura_c = 25
    
    F = float((temperatura_c * 9/5) + 32)
    print(F,type(F))
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    info('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
