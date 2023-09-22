# Leer los datos de entrada
sueldo_basico = float(input("Ingrese el sueldo básico: "))
antiguedad = int(input("Ingrese la antigüedad en años: "))
estado_civil = int(input("Ingrese el estado civil (1 para soltero, 2 para casado): "))

# Definir los porcentajes de incremento y descuento
porcentaje_incremento_soltero = 0.05
porcentaje_incremento_casado = 0.07
porcentaje_jubilacion = 0.11
porcentaje_obrasocial = 0.03
porcentaje_sindicato = 0.03

# Calcular el incremento del sueldo
if estado_civil == 1:  # Soltero
    incremento_sueldo = sueldo_basico * porcentaje_incremento_soltero * antiguedad
else:  # Casado
    incremento_sueldo = sueldo_basico * porcentaje_incremento_casado * antiguedad

# Calcular el sueldo bruto
sueldo_bruto = sueldo_basico + incremento_sueldo

# Calcular los descuentos
descuento_jubilacion = sueldo_bruto * porcentaje_jubilacion
descuento_obrasocial = sueldo_bruto * porcentaje_obrasocial
descuento_sindicato = sueldo_bruto * porcentaje_sindicato

# Calcular el sueldo neto
sueldo_neto = sueldo_bruto - (descuento_jubilacion + descuento_obrasocial + descuento_sindicato)

# Imprimir los resultados
print(f"Sueldo neto: ${sueldo_neto:.2f}")