#Ejercicio 3
cu = 0
c = 0
c10 = 0
cpb = 0
cu = int(input("Ingrese cantidad solicitada: "))
while cu != -1:
    pb = int(input("ingrese el precio base: "))
    if cu != -1:
        if cu < 13:
            vt = cu * 100
            cpb = cpb + 1
            print("El valor total de las ventas es = ", vt, "el promedio por unidad es", pb)
        elif cu <= 100 and cu >=13:
            vt = 12 * pb + (cu - 12) * (pb * 0.9)
            prom = vt / cu
            c10 = c10 + 1
            print("El valor total de las ventas es = ", vt, "el promedio por unidad es", prom)
        elif cu > 100:
            vt = 12 * pb + 88 * (pb * 0.9) + (cu - 100) * (pb * 0.75)
            prom = vt / cu
            print("El valor total de las ventas es = ", vt, "el promedio por unidad es", prom)
        cu = int(input("Ingrese cantidad solicitada: "))
        c = c + 1
    
print("Hubo", c, "ventas totales.", cpb, "de las ventas fueron con precio base y ", c10, "con 10% de descuento")