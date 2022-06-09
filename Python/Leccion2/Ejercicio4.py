# Ejercicio4 Etapas de la vida

edad = int(input("Dijite su edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 29:
    mensaje = "Amor y comienza el trabajo"
elif 29 <= edad < 39:
    mensaje = "Continua el trabajo y comienzas una nueva familia"
elif 39 <= edad < 49:
    mensaje = "Trabajas y ves crecer a tus hijos"
elif 49 <= edad < 59:
    mensaje = "Una nueva etapa de tu/s hijo/s ha comenzado, sigue esfozandote"
elif 59 <= edad < 69:
    mensaje = "Estas en el tramo final de tu vida laboral, tus hijo/s ya ingresaron a la universidad "
elif 69 <= edad < 79:
    mensaje = "Ya estas retirado, ahora comienzas a disfrutar tus dias a tu manera, los nietos/as vendran a visitarte"
elif 79 <= edad < 89:
    mensaje = "El cuerpo duele, pero haces todo por tus hijos/as, nietos/as"
elif 89 <= edad < 99:
    mensaje = "Tienes una basta experiencia de vida, pero la misma esta por terminar, sonrie lo hiciste lo mejor que pudiste"
else:
    mensaje = "Felicitaciones has vivido mas años de lo esperado, ahora te invito a colocar bien tu edad"
print(f"Tienes: {edad} , {mensaje}")