#Ejercicio 6
D = int(input("ingrese un numero: "))
cp = 9
cn = -cp
c = 0
N = D
if D > 0:
    while D > 0:    
        D = D - cp
        cp = cp + cp * 10
        c = c + 1
    print("El numero", N, "tiene", c, "digitos")
else:
    while D < 0:    
        D = D - cn
        cn = cn + cn * 10
        c = c + 1
    print("El numero", N, "tiene", c, "digitos")
        
    