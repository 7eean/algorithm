#Ejercicio 1
i = 0
suma = 0
numeroIngresado = int(input("Ingrese un número: "))
while numeroIngresado <= 0:
    print("error")
    numeroIngresado = int(input("Ingrese un número: "))
else:
    while i < numeroIngresado:
        i = i + 1
        if numeroIngresado%i == 0 and i < numeroIngresado:
            suma = suma + i
if suma > numeroIngresado:
    print("Es un número excesivo")
else:
    print("No es un número excesivo")

#Ejercicio 2
nlegajo = int(input ("Ingrese un numero de legajo de cuatro digitos o -1 para finalizar "))
nota = 0
suma = 0
caplazados = 0
cdesaprobados = 0
caprobados = 0
cpromocionados = 0
paplazados = 0
pdesaprobados = 0
paprobados = 0
ppromocionados = 0

while nlegajo != -1 :
    if nlegajo > 999 and nlegajo < 10000 :
        nota = int(input("Ingrese la nota del alumno "))
        if nota >= 4 and nota < 7 :
            print ("El alumno aprobo con nota entre 4 y 6 ")
            caprobados = caprobados + 1
        elif nota >= 7 and nota <= 10 :
            print ("El alumno aprobo con nota entre 7 y 10 ")
            cpromocionados = cpromocionados + 1
        elif nota > 1 and nota < 4 :
            print ("El alumno desaprobo ")
            cdesaprobados = cdesaprobados + 1
        else:
            print ("El alumno fue aplazado ")
            caplazados = caplazados + 1
        nlegajo = int(input("Ingrese el numero de legajo del alumno de cuatro digitos o -1 para finalizar "))
    else:
        nlegajo = int(input("Ingrese el numero de legajo del alumno de cuatro digitos o -1 para finalizar "))
suma = caprobados + cpromocionados + cdesaprobados + caplazados
paplazados = caplazados * 100 / suma
pdesaprobados = cdesaprobados * 100 / suma
paprobados = caprobados * 100 / suma
ppromocionados = cpromocionados * 100 / suma

print ("La cantidad de alumnos aprobados con nota entre 4 y 7 es ", caprobados)
print ("El porcentaje de alumnos aprobados con nota entre 4 y 7 es ", paprobados)
print ("La cantidad de alumnos aprobados con nota entre 8 y 10 es ", cpromocionados)
print ("El porcentaje de alumnos aprobados con nota entre 8 y 10 es ", ppromocionados)
print ("La cantidad de alumnos aprobados con nota entre 2 y 3 es ", cdesaprobados)
print ("El porcentaje de alumnos aprobados con nota entre 2 y 3 es ", pdesaprobados)
print ("La cantidad de alumnos aprobados con nota 1 es ", caplazados)
print ("El porcentaje de alumnos aprobados con nota 1 es ", paplazados)