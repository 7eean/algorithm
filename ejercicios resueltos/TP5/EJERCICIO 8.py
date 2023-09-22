#Ejercicio 8
N = 0
c1 = 0
C3 = 0
M = 0
S = 0
R = 0
c = 0
st1 = 0
st2 = 0
st3 = 0
D = 0
while N != -1:
    N = int(input("Ingrese el legajo: "))
    if N != -1:
        S = int(input("Ingrese el salario: "))
        if S >= 200000:
            c1 = c1 + 1
            print("El empleado", N, "gana", S, "y es de categoria 1")
            st1 = st1 + N
        elif S < 50000:
            C3 = C3 + 1
            st3 = st3 + N
            print("El empleado", N, "gana", S, "y es de categoria 3")
        else:
            st2 = st2 + N
            print("El empleado", N, "gana", S, "y es de categoria 2")
        if c == 0:
            D = S
        elif c != 0 and D >= S:
            D = S
        elif M <= S:
            M = S
            sma = N
        c = c + 1
        R = R + S
prom = R/c
print("El importe total de salarios es: ", R)
print(c1, "empleados ganan mas de 200000")
print(C3, "empleados ganan menos de 50000")
print("El empleado de legajo", sma, "es el que mas gana")
print("El sueldo mas bajo es", D)
print("Se paga un total de", st1, st2, st3, "para la categoria 1 2 y 3 respectivamente")
print("El salario promedio por empleado es: ", prom)
