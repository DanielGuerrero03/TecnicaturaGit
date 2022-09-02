# Cantidad de Números Positivos y Negativos
numPos = 0
numNeg = 0
numNeu = 0
cant = 0
while  cant < 10:
    cant += 1
    num = int(input(f" Ingrese un Número #{cant} "))
    if num > 0:
        numPos += 1
    elif num < 0:
        numNeg += 1
    else:
        numNeu += 1
print("****************")
print(f"La cantidad de Números positivos es: {numPos} ")
print("****************")
print("****************")
print(f"La cantidad de Números Negativos es: {numNeg} ")
print("****************")
print("****************")
print(f"La cantidad de Números Neutros es: {numNeu} ")
print("****************")
print("copyright (c) 2022 BESTIAS BINARIAS")