# lista = Ariel , Liliana, Natalia, Osvaldo
# Colecciones en Python

# Las listas se conocen en otros lenguajes como arreglos o vectores
# Una lista puede tener diferentes tipos de datos
nombres = ["Naty" , "Osvaldo" , "Lily" , "Ariel"]
print(nombres)
# De esta manera podemos ver un nombre de la lista en especifico
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

# ver como recuperamos un rango de la lista
print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
# ir al inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # indices a mostrar 0 , 1 , 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
# Iterar nuestra lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Alberto") # Primero insertamos un entero (posicion del indice), luego un string (objeto)
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminamos un indice especifico
del nombres[2] # del significa delete (Eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) # Aqui no mostrara nada sino que va a mostrar un error porque no hay lista que mostrar


# Tuplas (Los elementos en ella no se pueden eliminar o modificar)

# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
# Ver cantidad de elementos
print(len(cocina))
# Acceder a un elemento, para ello utilizamos los corchetes no parentesis
print(cocina[0])
# Mostrar de la manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ("Papa",) # Una Tupla necesita aunque sea de un elemento: la coma
# De lo contrario solo seria un tipo string cadena

# Recorremos los elementos de una tupla
for cocinar in cocina:
    print(cocinar, end=" ") # Print esta usando \n para saltos de linea, si agregamos el end = " ", elimina los saltos de linea

# Se puede modificar una tupla, pasandola a lista y luego pasandola a tupla, pero no se considera buenas practicas
cocinalista = list(cocina)
cocinalista[0] = "Plato"
cocina = tuple(cocinalista)
print("\n", cocina)

# En las tuplas no se pueden utilizar append, remove, del

# del cocina esto es para eliminar una tupla.
# Tipo set
planetas ={"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas)) #Usamos la funcion len = length significa largo

# Revisar si un elemento existe dentro de set
print("Marte" in planetas)

#Agregar un elemento
planetas.add("Tierra") #add es una función.
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe.
planetas.remove("Jupiter") # Esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("Tierra") #Esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra un error

# "Maradona": 10 Un diccionario esta compuesto por dos elementos
# Una Llave y Un Valor
# dict(key,value)
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sistema de Administracion de Base de Datos"
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

#Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

# Otras maneras de acceder a un Diccionario
for termino in diccionario.keys(): #estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la exitencia de algun elemento
print("IDE" in diccionario) # Devuelve un booleano, si queremos consultar sino esta colocamos el not in diccionario

# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

#No se puede agregar llaves duplicadas!

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del    diccionario # El diccionario se borro
# ----------------------------------------------------------------------------------
# Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2 # Concatenamos
print(lista3)

lista3.extend([7,8,9,1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta en el valor ingresado
#print(lista3.index(0)) esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner nuestra lista al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = lista3 * 2
print(lista)

# Mètodos de ordenamiento, en python es una funcion

lista.sort() # Ordena los elementos en forma ascendente
print(lista)
lista.sort(reverse=True) # Ordena descendentemente
print(lista)

#Repaso Tuplas
# Tuplas son lista inmutables (no se pueden modificar) y pueden tener diferentes tipos de datos

tupla =(4, "Hola", 6.78, [1,2,78], 4, "Hola")
print(tupla)

# Buscar un elemento
print(4 in tupla) # Accion Booleana, su respuesta es de tipo booleana

# Lo que podemos usar dentro de tuplas son : index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla


#Repaso de set o cunjunto
#Para definir un conjunto
conjunto2 = set() # Con set podemos inicializar el conjunto
conjunto1 = {"bye"} #Con las llaves solas no se puede inicializas vacio con las llaves
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el numero 3 no esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuleve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un sub conjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como sabes si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {"Azul" : "Blue", "Rojo" : "Red", "Verde": "Green", "Amarillo" : "Yellow" }
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Ariel": {"Edad" : 40, "Altura": 1.83}, "Osvaldo": [45, 1.85], "Natalia" :[35, 167]}
print(diccionario2)

seleccionArgentina={
    10: {"Nombre": "Lionel Messi", "Edad" : 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad" : 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    21: {"Nombre": "Paulo Dybala", "Edad" : 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19: {"Nombre": "Nicolas Otamendi", "Edad" : 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad" : 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Portero"},
    23: {"Nombre": "Emiliano Martinez", "Edad" : 30, "Altura": 1.95, "Precio": "28 Millones", "Posicion": "Portero"},
    17: {"Nombre": "Papu Gòmez", "Edad" : 34, "Altura": 1.67, "Precio": "6 Millones", "Posicion": "Mediocentro Ofensivo"},
    22: {"Nombre": "Lautaro Martínez", "Edad" : 25, "Altura": 1.74, "Precio": "75 Millones", "Posicion": "Delantero Centro"},
    20: {"Nombre": "Giovani Lo Celso", "Edad" : 26, "Altura": 1.77, "Precio": "22 Millones", "Posicion": "Mediocentro"}
}
for llave,valor in seleccionArgentina.items():
    print(llave,valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end= "")
print(len(seleccionArgentina))

# Metodo PILAS usando Listas
pila = [1, 2, 3]

# Agregar elemento a la pila por el final (siempre se trabaja con el ultimo elemento)
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora quedo asi: {pila}")

# Colas con listas
# Estructura de datos de tipo fifo (Firts input / first output)

cola = ["Ariel", 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}' )
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}' )
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}' )
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}' )
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}' )
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for

for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")

