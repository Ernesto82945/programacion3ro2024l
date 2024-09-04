#2- Un cliente te solicita la creación de un Programa que permita poder buscar sus socios dentro de una lista y que el programa le informe si existen o no en su listado de socios-
#Ayuda:- crear lista y asignar nombres de socios.
#usar la estructura de control de programación adecuada a la situación a resolver para satisfacer lo solicitado por el cliente.
Lista_De_Socios= ["Pepe","Pepe2","Pepe3","Pepe4"]
BuscarNombre= input("Ingrese el nombre de algun socio que este en la lista:")
if BuscarNombre in Lista_De_Socios:
    print ("El si se encuentra en la lista de socios")
else:
    print ("El no forma parte de la lista de socios")
    