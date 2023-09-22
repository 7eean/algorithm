n = int(input ("Introduzca un numero: (-1 para salir): "))
if n != -1:
    flag = 1
    while n != -1:
        if flag == 1:
            flag = 0
        elif flag == 0:
            flag = 1
        n = int(input ("Introduzca otro numero (-1 para finalizar la carga):"))
    if flag == 0:
        print ("La cantidad de elementos es impar")
    elif flag == 1:
        print ("La cantidad de elementos es par")
else:
    print ("Saliendo...")  