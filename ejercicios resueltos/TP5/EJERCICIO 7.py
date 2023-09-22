#Ejercicio 7
D = int(input("ingrese un numero: "))
cp = 9
cn = -cp
c = 0
N = D
ni = 0
if D > 0:
    while D > 0:    
        D = D - cp
        cp = cp + cp * 10
        c = c + 1
else:
    while D < 0:    
        D = D - cn
        cn = cn + cn * 10
        c = c + 1
p = c        
while c >= 0:
    F = N//(10**(c-1))
    N = N - F * (10**(c-1))
    R = F%(10**(c-1))
    if R != 0:
        ni = ni + R*(10**-c)
    else:
        ni = ni + F*(10**-c)
    c = c - 1
N = ni * (10**p)
print(N)
    
    