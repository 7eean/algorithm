#Ejercicio 1
E = 0
pcm = 0
pcM = 0
cm = 0
cM = 0
while E != -1:
    E = int(input("Ingrese la edad(1-100): "))
    if E <= 18 and E >= 0:
        cm = cm + 1
        pcm = pcm + E
    elif E <= 100 and E > 18:
        cM = cM + 1
        pcM = pcM + E
    else:
        print("error, ingrese otro numero")
prom = pcm/cm
proM = pcM/cM
print("Hay", cm, "menores y ", cM, "mayores. El promedio de edad de menores y mayores es ", prom, proM, "respectivamente")