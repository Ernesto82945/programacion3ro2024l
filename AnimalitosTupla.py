Animales=("Conejo","Mono","Cocodrilo")
buscar=input("Ingrese el animal que desea buscar adentro de la lista: ")
if buscar in Animales:
    print("el animal",buscar,"se encuentra dentro de la tupla")
else:
    print("el animal",buscar,"no se encuentra dentro de la tupla")