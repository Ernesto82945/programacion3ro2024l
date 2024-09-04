numeroentero=[]
suma = 0
n= 1
while n != 0:
    n=int(input("ingrese un positivo entero, si ingresa el numero 0 suma todos los numeros:            "))
    suma += n
print (f"la suma de los numeros es: {suma}")    
digitos_pares = []
for digito in num:
    digito_int = int(digito)
    sdd += digito_int
    if digito_int % 2 == 0:
        digitos_pares.append(digito_int)
print (f"estos son los digitos del numero sumados: {sdd}")
print (f"estos son los numeros pares que pusiste: {digito_int}")
