from turtledemo.sorting_animate import Block


def dicitionary(name):
    #Zadanie 1
    filmy = ["Harry Potter","Szklana pułapka","Efekt motyla","Transformers","Jak Wytresować Smoka"]
    filmy.append("Avatar")
    filmy.pop(1)
    filmy.insert(1,"Transformers 2")

    for film in filmy:
        print(film)
        
    #Zadanie 2
    kraje = {
        "Francja" : "Paryż",
        "Polska" : "Warszawa",
        "Niemcy" : "Berlin"
    }
    
    print(kraje["Francja"])
    
    kraje["Czechy"] = "Praga"
    
    if "Czechy" in kraje:
        print(kraje["Czechy"])
        
    for kraj,stolica in kraje.items():
        print(f"{kraj}: {stolica}")
    
    #Zadanie 3
    A = {1,2,3,4,5}
    B = {4,5,6,7,8}
    
    print(A.union(B))
    print(A.intersection(B))
    print(A.difference(B))
    print(B.difference(A))

if __name__ == "__main__":
    dicitionary("PyCharm")