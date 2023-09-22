#TP4 Ejercicio11---------------------------------------------------

n = int(input ("Introduzca un numero positivo: (-1 para salir): "))
if n != -1:
    if (0 < n <= 2):
        print ("El numero es primo")
    else:
        cont = 2
        while n != -1:
            if n <= 0:
                print ("El numero ingresado es invalido, ingrese un numero mayor a 0")
                n = int(input ("Introduzca un numero: (-1 para salir): "))
            else:
                if (n % cont) == 0:
                    print ("El numero no es primo")
                    n= -1
                elif n < (cont ** 2):
                    print ("El numero es primo")
                    n= -1
                else:
                    cont = cont + 1