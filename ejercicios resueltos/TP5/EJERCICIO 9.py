#Ejercicio 9
N = int(input("Ingresa un numero positivo: "))
c = 1
t = 0
if N < 0:
    while N < 0:
        print("error")
        N = int(input("Ingresa un numero positivo: "))
if N%2 == 0:
    N = N - 1
    while c <= N:
        print(c)
        t = t + c
        c = c + 2
elif N%2 != 0:
    while c <= N:
        print(c)
        t = t + c
        c = c + 2
print("La suma de los numeros impares es ", t)