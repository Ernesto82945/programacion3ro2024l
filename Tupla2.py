deportes=("Futbol","Tenis","Basquet")
buscar=input("Ingrese el elemento que desea buscar adentro de la lista: ")
if buscar in deportes:
    print("el elemento",buscar,"se encuentra dentro de la tupla:")
else:
    print("el elemento",buscar,"no se encuentra dentro de la tupla:")