# lista = Ariel , Liliana, Natalia, Osvaldo

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
