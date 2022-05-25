""""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
# Las literales se escriben x240, la variable y = x984, la variable z = x304
print(id(x))
print(id(y))
print(id(z))

# Tipos int (enteros) , float (flotante) , string (cadena), bool (booleano)
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)
# el simbolo + funciona como concatenacion
numero11 = "7"
numero22 = "8"
print(int(numero11) + int(numero22))  # aca al ponerle entero suma los valores

# Tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# procesar la entrada del usuario
# Funcion input
resultado = input("Digite un nuemro: ")  # regresa un dato string
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es:  ", resultado)

#Ejercicio1
print("Como estuvo tu dia?:")
dia = input()
print("Mi dia estuvo de: " + dia)

#Ejercicio2
print("Ingrese el titulo del libro: ")
titulo = input()
print("Ingrese el nombre del autor del libro: ")
autor = input()
print(titulo, "Fue escrito por", autor)
"""
"""
# Operadores aritmeticos
operandoa = 8
operandob = 5
suma = operandoa + operandob
# print("Resutaldo de la suma: ", suma)

print(f'El resutlado de la suma: {suma}')

resta = operandoa - operandob
print(f'El resutlado de la resta es: {resta}')

multiplicacion = operandoa * operandob
print(f'El resutlado de la multiplicacion es: {multiplicacion}')

divicion = operandoa / operandob
print(f'El resutlado de la divicion es: {divicion}')
divicion = operandoa // operandob
print(f'El resutlado de la divicion (int) es: {divicion}')

modulo = operandoa % operandob
print(f'El resutlado de la divicion o residuo (modulo) es: {modulo}')

exponente = operandoa ** operandob
print(f'El resutlado del exponente es: {exponente}')
"""
# Area y Perimetro de un rectangulo
"""
alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Ingrese el Ancho del rectangulo:"))
area = ancho * alto
print("El Area del rectangulo es: ", area)
perimetro = (alto + ancho) * 2
print("El Perimetro del rectangulo es: ", perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)
# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)
# se puede colocar lo de la linea 112 de esta manera igualmente
miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparación
d = 4
b = 2
resultado = d == b  # Comprobamos si son iguales
print(resultado)

# Operador diferente

resultado = d != b
print(resultado)

# Operador Mayor que
resultado = d > b
print(resultado)

# Operador Menor que
resultado = d < b
print(resultado)

# Operador Menor o Igual que
resultado = d <= b
print(resultado)

# Operador Mayor o Igual que
resultado = d >= b
print(resultado)

# Ejercicio3
valor = int(input("Ingrese un numero:"))
if valor %2 == 0:
        print("El numero es par")
else:
        print("El numero es impar")
"""
"""
# Ejercicio4
edad = int(input("Ingrese su edad:"))
if edad >= 18:
        print("Usted es mayor de Edad")
else:
        print("Usted es menor de Edad")
"""
"""
# Operadores Lógicos
# Operador and
a = True
b = True
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)

# Ejercicio valor dentro de un rango

valor = int(input("Ingrese un numero: "))
if valor >= 0 and valor <= 5:
        print(f"El numero {valor} esta dentro del rango: ")
else:
        print(f"El numero {valor} esta fuera del rango: ")
"""
"""
# Ejercicio Rango entre 20 y 30 años
edad = int(input("Ingrese su edad: "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)
if (edad >=20 and edad <30) or (edad >= 30 and edad < 40):
        print("Estas dentro del rango de los (20'0) a (30'0) años ")
else:
        print("No estas dentro del rango de los (20'0) a (30'0) años ")

# sintaxis simplificada del operador and
if (20 <= edad < 30) or (30 <=  edad < 40):
        print("Estas dentro del rango de los (20'0) a (30'0) años ")
else:
        print("No estas dentro del rango de los (20'0) a (30'0) años ")
"""
"""
# Ejercicio: El Mayor de dos numeros
numero1 = int(input("Ingrese un numero"))
numero2 = int(input("Ingrese otro numero"))
if (numero1 > numero2):
        print("El numero mayor es:",numero1)
else:
        print("El numero mayor es:", numero2)
"""
# Ejercicio: Tienda
print("Digite los siguientes datos del libro")
nombre = input("Escriba el nombre del libro: ")
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))
enviogratuito = input("Indique si el envio es gratuito o no, escriba (True/False):")
if enviogratuito == "True":
    enviogratuito = True
elif enviogratuito == "False":
    enviogratuito = False
else:
        enviogratuito = "El valor ingresado es incorrecto, debe escribir True/False"
print(f"""
        Nombre: {nombre}
        ID: {id}
        Precio: {precio}
        Envio Gratuito: {enviogratuito}""")