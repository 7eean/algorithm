#Ejercicio 5
D = int(input("ingrese el dia: "))
M = int(input("ingrese el mes: "))
A = int(input("ingrese el año: "))

N = int(input("ingrese cantidad de dias a sumar: "))
c = 0

while c < N:
    D = D + 1
    if D > 31 and ((M <= 7 and M%2 != 0) or (M >= 7 and M%2 == 0)):
        D = 1
        M = M + 1
    elif D > 30 and ((M >= 7 and M%2 != 0) or (M <= 7 and M%2 == 0) and M != 2):
        M = M + 1
        D = 1
    elif D > 29 and M == 2 and ((A%4 == 0 and A%100 != 0) or (A%400 == 0)):
        D = 1
        M = M + 1
    elif D > 28 and M == 2 and ((A%4 != 0) or (A%100 == 0)):
        D = 1
        M = M + 1
        
    if M == 13:
        M = 1
        A = A + 1
    c = c + 1
    
print("la nueva fecha es", D, "/", M, "/", A)
    