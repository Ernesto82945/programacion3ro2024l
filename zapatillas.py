#1- Crear un programa que permita manipular y visualizar el stock de zapatillas donde cada una tenga las siguientes propiedades: Número, material, modelo y cantidad en stock.
codigo={"01":{"Talla":"48","Material":"cuero sintético","Cant de Stock":"20 pares","Modelo":"Nike"}},{"02":{"Talla":"39","Material":"cuero sintético","Cant de Stock":"26 pares","Modelo":"Adidas"}},{"03":{"Talla":"37","Material":"Plastico","Cant de Stock":"43 pares","Modelo":"Croc"}}
print(codigo)
print("_____________________________________________________________________________________________________________________________")

for c,v in codigo.item():
    print(c, ":", v )
    
    print("_________________________________________________________________________________________________________________________")