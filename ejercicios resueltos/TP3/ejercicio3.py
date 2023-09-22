# Ejercicio 3: Desarrollar un programa que solicite un número
# de mes y escriba el nombre del mes en letras. Verificar que el
# mes sea válido y mostrar un mensaje de error en caso de que no
# lo sea.

numMes = int(input("Ingrese un numero de mes: "))

if numMes == 1:
    print("Enero")
elif numMes == 2:
    print("Febrero")
elif numMes == 3:
    print("Marzo")
elif numMes == 4:
    print("Abril")
elif numMes == 5:
    print("Mayo")
elif numMes == 6:
    print("Junio")
elif numMes == 7:
    print("Julio")
elif numMes == 8:
    print("Agosto")
elif numMes == 9:
    print("Septiembre")
elif numMes == 10:
    print("Octubre")
elif numMes == 11:
    print("Noviembre")
elif numMes == 12:
    print("Diciembre")
else:
    numMes < 1 and numMes > 12
    print("Numero de mes invalido. Por favor, ingrese un numero valido.")