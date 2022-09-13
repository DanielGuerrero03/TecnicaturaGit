# Ejercicio 2 : Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuacion.
# cree las siguientes listas (en las que no deben haber repeticion)

# creamos las listas
from typing import Set

lista1 = ["Daniel", "Matias", "Juan", "Juan", "Julian", "Amanda", "Julia", "Romina", "Daiana", "Amanda"]
lista2 = ["Laura", "Estela", "Pedro", "Marcos", "Julian", "Romina", "Juan"]

# 1 Listas de palabras que aparecen en las listas
lista3 = lista1 + lista2
print("Las palabras de las listas son : ", lista3)

# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = conjunto1 - conjunto2
print(list(conjunto3))

# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
conjunto3 = conjunto2 - conjunto1
print(list(conjunto3))

# 4 Lista de palabras que aparecen en ambas listas
conjunto3 = conjunto1 & conjunto2
print(list(conjunto3))
