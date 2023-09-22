kmRecorrido = float(input("Ingrese la cantidad de kilometros recorridos: "))
viajeMinimo = 250
viajeMedio = 30 * kmRecorrido
viajeLargo = 20 * kmRecorrido

if kmRecorrido > 0 and kmRecorrido < 10:
    print("Usted debera abonar ", viajeMedio)
elif kmRecorrido > 10:
    print("Usted debera abonar ", viajeLargo)
else:
    print("Usted debera abonar ", viajeMinimo)