#Ejercicio 4
NC = input("ingrese el numero de cliente: ")
tf = int(input("ingrese el total de la factura: "))
men = tf * 0.02
may = tf * 0.1 
if men < 200:
    men = 200
    
if may < 350:
    may = 350
men = tf - men
may = tf + may
print("El cliente", NC, "deberá abonar ", tf, "pagando en tiempo y forma", men, "pagando los primeros 10 dias y ", may, "pagando los ultimos dias")
