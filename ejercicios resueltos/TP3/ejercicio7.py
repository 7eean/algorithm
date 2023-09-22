año = int(input("Ingrese un numero correspondiente a un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(año, "es bisiesto")
else:
    print(año, "no es bisiesto")