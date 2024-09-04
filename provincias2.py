provincias={"Cordoba":"Cordoba","San miguel de tucuman":"San miguel de tucuman","Jujuy":"Jujuy","Mendoza":"Mendoza","salta":"salta","Santa fe":"Santa fe","Tierra del fuego":"Usuaia","Misiones":"Posadas","Chubut":"Rawson","Corrientes":"Corrientes","Chaco":"Resistencia","La pampa":"Santarosa","Santiago del estero":"Santiago del estero","Neuquen":"Neuquen","san luis":"San luis","La rioja":"La rioja","catamarca":"san fernando de el valle de catamarca"}


pciaBuscarValorCapital=input("Ingresar provincia a buscar capital: ")
#Buscamos el valor por clave, en este caso capital ingresando provincia
x = provincias[pciaBuscarValorCapital]
print("su capital es:",x)
print("_______________________")




for p, c in provincias.items():
    print(p, "-", c)
           
