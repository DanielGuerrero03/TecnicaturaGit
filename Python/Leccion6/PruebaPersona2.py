from Persona2 import Persona2

print("creacion de objetos".center(50, "-"))
if __name__ == "__main__":
    persona5 = Persona2("Daniel", "Guerrero", 31)
    persona5.mostrar_detalles()

    print(__name__)

print("Eliminacion de objetos".center(50, "-"))
del persona5
