# Ejercicio 3 : Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos.
#Nombre : Aragon
#Clase : Guerrero
#Raza : Dunadan del norte

#Nombre : Gandalf
#Clase : Mago
#Raza : Istar

#Nombre : Legolas
#Clase : Elfo
#Raza : Elfo Sindar

#creamos una lista vacia
personajes = []
# Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero','Raza': 'Dunadan del Norte'}
personajes.append(P) #agregamos a la lista un personaje
P = {'Nombre': 'Gandalf', 'Clase': 'Mago','Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Elfo','Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Frodo Bolson', 'Clase': 'Espadachin','Raza': 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Boromir', 'Clase': 'Guerrero','Raza': 'Dunadan del Sur'}
personajes.append(P)
P = {'Nombre': 'Elrond', 'Clase': 'Señor de Rivendel','Raza': 'Peredhil'}
personajes.append(P)
print(personajes)