# Ejercicio 1 iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
print(f"Los numeros divisibles por 3 son: ")
for i in range(0, 10):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimirlos.
print("El rango de 2 a 6 esta conformado por :")
for i in range(2, 7):
    print(i)

# Ejercicio 3 : Crear un rango de 3 a 10 pero con incrementos de 2 en 2
print("El rango con valores de inicio en 3 y fin en 10, con incremento de 2 en 2")
for i in range(3, 11 , 2):
    print(i)