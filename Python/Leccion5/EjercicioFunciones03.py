# Ejercicio 3 : Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendiente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el,
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# en caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# si se ingresan numero negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:  # caso base
        print(numero)
        imprimir_numeros_recursivos(numero - 1)  # caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("El Valor ingresado es incorrecto ...")


numero = int(input("Ingrese un numero: "))
print(imprimir_numeros_recursivos(numero))
