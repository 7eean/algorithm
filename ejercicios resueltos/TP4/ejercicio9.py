"""TP4:9. Se desea analizar cuántos autos circulan con patente con numeración par y 
cuántos con numeración impar en un día. Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe 
cuántos vehículos pasaron con numeración par y cuántos con numeración impar"""

patente = int(input("escribir la numeración final de la patente: "))

patente_par = 0
patente_impar = 0

while patente != -1:
    if (patente >= 0) and (patente <= 9):
        if (patente % 2) == 0:
            patente_par = patente_par + 1
        else:
            patente_impar = patente_impar + 1
    else:
        print("re-escribir la numeración final de la patente (entre 0 y 9)")
    patente = int(input("escribir la numeración final de la patente: "))
    
print("la cantidad de patentes pares son: ", patente_par)
print("la cantidad de patentes impares son: ", patente_impar)