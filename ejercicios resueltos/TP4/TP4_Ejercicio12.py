#TP4 Ejercicio12------------------------------------------

n = int(input ("Introduzca un numero: (-1 para salir): "))
if n != -1:
    cont = 0
    num3 = 0
    acum = 0
    while cont != n:
        if cont == 0:
            num0 = 0
            print (num0,end="")
        elif cont == 1:
            num1 = 1
            acum = 0 + num1
            print (num1,end="")
        elif cont > 1:
            num3 = num0 + num1
            num0 = num1
            num1 = num3
            acum = acum + num3
            print (num3,end="")
        cont = cont + 1
        if cont != n:
            print (", ",end="")

print ("\nLa suma final es ", acum)