# Ejercicio 4 : Sumar numeros pares dentro de un rango
# Hacer un programa para sumar numeros pares dentro de un rango
#por ejemplo:
#              suma de numeros pares del 2 al 30
#               suma = 240

num1 = int(input("Ingrese Limite inferior del rango: "))
num2 = int(input("Ingrese Limite superior del rango: "))
suma = 0
for i in range (num1,num2+1):
    if i %2 == 0: # Esto es si el numero es par
        suma += i
    print(f"\nLa suma de los numeros pares en el rango es de : {suma} ")
