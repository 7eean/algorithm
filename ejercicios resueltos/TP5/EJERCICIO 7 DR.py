#Ejercicio 7 DR
n = int(input("Numero = "))
invertido = 0
if n < 0:
    n = -n

while n != 0:
    ultimodigito = n%10
    invertido = invertido*10 + ultimodigito
    n = n//10
print("El valor invertido es", invertido)
