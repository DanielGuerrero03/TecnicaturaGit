#Ejercicio año bisiesto

bisiesto = int(input("Ingrese el Año"))
# sentencia if/else
if bisiesto % 4 == 0 and bisiesto % 100 != 0 or  bisiesto % 400 == 0:
    print(f"{bisiesto} ,Es un año Bisiesto ")
else:
    print(f"{bisiesto} ,no es un año Bisiesto ")