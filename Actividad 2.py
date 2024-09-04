numeroentero=[]
while True:

    numero=int(input("Ingrese nunero entero:              "))
    numeroentero.append(numero)
    if numero==0:
        print("Cerrando el programa ")
        break
    print("el valor mayor es:")
    print(max(numeroentero))