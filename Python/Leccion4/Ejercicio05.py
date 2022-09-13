# Ejercicio 5 : Factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero positivo.

num = int(input("Ingrese el numero que desea calcular el factorial: "))
def factorial(num):
    if num < 0:
        print("El Factorial de un numero negativo no existe")
    elif num == 0:
        return 1
    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        return fact
print("Factorial del numero", num, "es", factorial(num))