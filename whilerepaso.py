prod=[]
rta="si"
while rta=="Si" or rta=="si" or rta=="SI":
opcion=input("1. Agregar un producto a la lista\n2. Mostrar productos de la lista\n3.Salir")
if opcion=="1":
    productoAgregar=input("Ingrese el producto a Agregar:")
    prod.append(productoAgregar)
elif opcion=="2":
    for p in prod:
        print("los productos en la lista son:",p)
elif opcion=="3":
    rta=input("Esta seguro de salir del sistema:(si/no)") 
    if rta=="no" or rta=="No" or rta=="NO":
     break
else:
    print("opcion invalida")  




