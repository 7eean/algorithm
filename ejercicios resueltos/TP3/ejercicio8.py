dia = int(input("Ingrese un numero de dia: "))
mes = int(input("Ingrese un numero de mes: "))
año = int(input("Ingrese un numero de año: "))

fechaValida = True
fechaInvalida = False

if (dia >= 1 and dia <= 30) or (mes >= 1 and mes <= 12) or (año >= 0 and año <= 2023):
    print(fechaValida)
else:
    print(fechaInvalida)

# Pude llegar hasta este paso pero sigo sin llegar al resultado