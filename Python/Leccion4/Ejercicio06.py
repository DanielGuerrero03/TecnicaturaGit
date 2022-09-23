#Ejercicio 6: Tabla de multiplicar
# hacer un programa que pida un numero por teclado y guarde en una lista
# su tabla de multiplicar hasta el 10. Por ejemplo:
# si digita el 5 la lista tendrá :5,10,15,20,25,30,35,40,45,50.

numero = int(input("Digite un numero: "))
lista = [] # Creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)

print(f'\nTabla de multiplicar del {numero}: \n {lista}')

for indice,i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}') # Este ciclo es para ver el formato de una tabla de multiplicar