#Ejercicio 7

i = 1
suma = 0
prom = 0
while i <= 5:
    horas = int(input("Dijite la cantidad de horas trabajadas: "))
    tarifa = int(input("Dijite la tarifa por hora: "))
    salario = horas * tarifa
    print("=======================================")
    print(f"Salario del Trabajador es : {salario} ")
    suma = suma + salario
    i += 1
    print("=======================================")
    print(f"La suma de los salarios es : {suma}")
    print("=======================================")
