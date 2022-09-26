# Comenzamos con Funciones

# mi_funcion() _ No se puede llamar antes de definir una función

# Definimos una Función
def mi_funcion(): # Para identificar a la función utilizamos paréntesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion() # Estamos llamando a la función
mi_funcion() # Se puede llamar a una función N cantidad de veces
mi_funcion()

# Desempaquetado de listas o list Unpacking
def show(name, lastname):
    print(name+" "+lastname)
person = ["Daniel", "Guerrero"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función.
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Ariel", "Betancud") # desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastname": "Lucero", "name": "Natalia"} # Diccionario
show(**person3)

# Repaso For / Else

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se terminó")

# List comprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP =[p for p in names if p[0] == "P"] # Esto regresa una nueva lista
print(alongP)
# Utiliza mos esto cuando queremos ver lo que contiene una lista / diccionario sin cambiar nada de ellas/os
bottleC = [{"name": "Quilmes", "country" : "Arg"},
           {"name": "Corona", "country" : "Mx"},
           {"name": "Stella Artois", "country" : "Belgium"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastname):
    print("Saludos a todos los que ven a travez del canal de Youtube")
    print(f"Nombre: {name}, Apellido: {lastname}")
mi_funcion2("Jorge", "Luecero")
mi_funcion2("Daniel", "Guerrero")
mi_funcion2("Nahuel", "Tapia")

# La palabra return en Funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f"El resultado de la suma es : {resultado}")
print(f'El resultado es : {sumar(55, 45)}')

# Valores por default en funciones
def sumar2(a: int = 0, b: int = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22,66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza : *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres("Daniel", "Ariel", "Pepe","Raul","Mirta")
listarNombres("Nahuel", "Gabriel", "Rosa", "Carlos")

