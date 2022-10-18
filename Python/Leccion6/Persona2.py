class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  # Esta encapsulado
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  # decorador
    def nombre(self):  # Metodo Getter
        print("Estamos usando el metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print("Estamos utilizando el metodo ser")
        self._nombre = nombre
   @property  # decorador
    def apellido(self):  # Metodo Getter
        print("Estamos usando el metodo get")
        return self._apellido

    @apellido.setter
    def nombre(self, apellido):  # Metodo Setter
        print("Estamos utilizando el metodo ser")
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Metodo Getter
        print("Estamos usando el metodo get")
        return self._edad

    @edad.setter
    def nombre(self, edad):  # Metodo Setter
        print("Estamos utilizando el metodo ser")
        self._edad = edad



persona1 = Persona2("Daniel", "Guerrero", 31)
print(persona1.nombre)  # Llamamos al metodo getter
print(persona1.apellido)
print(persona1.edad)
persona1.nombre = "Juan Pedro"
print(persona1.nombre)
