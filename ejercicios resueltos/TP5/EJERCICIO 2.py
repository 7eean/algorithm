#Ejercicio 2
l = 0
cd = 0
ca = 0
cap = 0
while l != -1:
    l = int(input("ingrese el legajo del alumno: "))
    if l != -1:
        n = float(input("ingrese la nota del final: "))
    
        if n == 1:
            print("El alumno de legajo", l, "aplazo")
            ca = ca + 1
        elif n < 4 and n > 1:
            print("El alumno de legajo", l, "desaprobo")
            cd = cd + 1
        elif n <= 10 and n >=4:
            print("El alumno de legajo", l, "aprobo")
            cap = cap + 1
        else:
            print("error, ingrese los datos nuevamente")
cant = cap + ca + cd
prom = ca/cant * 100
print(cd, "alumnos desparobaron", cap, "alumnos aprobaron y ", prom, "% de los alumnos aplazaron")
        
