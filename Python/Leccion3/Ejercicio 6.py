#Numeros pares de la lista y promedio de numeros impares

cant = int(input("Ingrese un la cantidad de Numeros a utilizar: "))
pares = 0
impares = 0
suma = 0
prom = 0
acum = 0
i = 1
while i <= cant:
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        suma = suma + num
        pares += 1
    else:
        acum = acum + num
        impares +=1
        prom = acum / impares
    i +=1

print("-------------------------------------------------")
print(f" La cantidad de Números Pares es: {pares} ")
print("-------------------------------------------------")
print(f" La suma de Números pares es {suma}")
print("-------------------------------------------------")
print(f" El promedio de los Números impares es {prom}")