# Ejercicio 1 : Llenar una lista
# Llenar una lista con los numeros del 1 al 50, luego mostrar
#la lista con el bucle for, los elementos deben mostrase
# de la siguiente forma:
#1-2-3-4-5... -50

lista = []
for i in range(51):
    lista.append(i)
    print(i, end="-")

