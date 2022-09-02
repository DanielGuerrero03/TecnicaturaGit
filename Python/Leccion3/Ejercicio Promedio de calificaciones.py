#Ejercicio calificacion promedio
califProm = 0
califBaja = 10 # definmos que la escala de calificaciones de de 0 a 10
alumnos = 0
while  alumnos < 10:
    alumnos += 1
    cal= int(input(f" Ingrese la calificacion del Alumno #{alumnos} "))
    califProm = califProm + cal
    if califBaja > cal:
        califBaja = cal
        print("Cargue mas Calificaiones")
    else:
        print("Cargue mas Calificaiones")
califProm = califProm / 10
print("****************")
print(f"La Calificación Promedio es: {califProm} ")
print("****************")
print(f"La Calificación  mas Baja es: {califBaja} ")
print("****************")

print("copyright (c) 2022 BESTIAS BINARIAS")