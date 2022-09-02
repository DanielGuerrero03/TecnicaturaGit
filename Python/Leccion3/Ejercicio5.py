#Factorial de un numero 

num = int(input("Digite un Número para sacar el Factorial ! :"))
if num >= 0:
    i = 1
    factorial = 1
    while i <= num:
        factorial = factorial * i
        i += 1
    print("-------------------------------")
    print(f" El factorial es {factorial}")
    print("-------------------------------")
else:
   print("Digite un Número  valido para sacar el Factorial ! :")