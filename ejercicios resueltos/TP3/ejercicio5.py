costoLibro = 500
costoPorPagina = 3.20
encuadernacionTela = 200
procedimientoEspecial = 336
cantPaginas = int(input("Ingrese la cantidad de páginas de su libro: "))
costoTotal = costoLibro + (costoPorPagina * cantPaginas)

if cantPaginas > 300:
    costoTotal += encuadernacionTela
elif cantPaginas > 600:
    costoTotal += procedimientoEspecial

print("El costo del libro es ", costoTotal)