# Ejercicio5 Sistema de calificaciones

nota = int(input("Ingrese su nota (0 - 10): "))
calificacion = None
if 0 <= nota < 6:
    calificacion = "F"
elif 6 <= nota < 7:
    calificacion = "D"
elif 7 <= nota < 8:
    calificacion = "C"
elif 8 <= nota < 9:
    calificacion = "B"
elif nota == 9 or 10:
    calificacion = "A"
else:
    print("El valor ingresado es incorrecto")
print(f"Su nota es : {nota} le corresponde una {calificacion}")
