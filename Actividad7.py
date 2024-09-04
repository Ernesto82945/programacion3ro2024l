montos = []
monto = float(input("Ingrese el monto de la compra (o 0 para finalizar): "))

while monto != 0:
    montos.append(monto)
    monto = float(input("Ingrese el monto de la compra (o 0 para finalizar): "))

print(f"\nMontos ingresados: {montos}")
print(f"Total de compras: {sum(montos):.2f}")