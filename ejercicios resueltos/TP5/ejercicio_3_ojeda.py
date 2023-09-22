# Ejercicio 3: Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
# · Aplica el precio base a la primera docena de unidades.
# · Aplica un 10% de descuento a todas las unidades entre 13 y 100.
# · Aplica un 25% de descuento a todas las unidades por encima de las 10 [...]

qty_base_price = 0
qty_10_desc = 0
qty_25_desc = 0
qty_total_sale = 0
sale_total_value = 0
avg_price = 0

base_price = int(input("Ingrese el precio base del producto: "))
qty_requested = int(input("Ingrese la cantidad solicitada del producto: "))
counter = 1

while (qty_requested != -1):
    qty_total_sale += qty_requested
    qty_requested = int(input("Ingrese la cantidad solicitada del producto: "))

while counter <= 12:
    sale_total_value += base_price
    qty_base_price += 1
    counter += 1

while counter > 12 and counter <= 100:
    sale_total_value += (base_price * 0.9)
    qty_10_desc += 1
    counter += 1

while counter <= qty_total_sale:
    sale_total_value += (base_price * 0.75)
    qty_25_desc += 1
    counter += 1

avg_price = sale_total_value / qty_total_sale

# Print
print("Ventas con precio base: ", qty_base_price)
print("Ventas con 10% descuento: ", qty_10_desc)
print("Ventas con 25% descuento: ", qty_25_desc)
print("Ventas totales: ", qty_total_sale)
print("Valor total de venta: ", sale_total_value)
print("Precio promedio: ", avg_price)