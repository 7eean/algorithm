#Clase 04 ///// Ejercicio 2 
num = int(input("Introduzca un numero: "))
flag = 1
while num != 1:
        if flag == 1:
            flag = 0
        elif flag == 0:
            flag = 1
        num = int(input ("Introduzca otro numero: "))
if flag == 0:
    print ("La cantidad de elementos es impar")
if flag == 1:
    print ("La cantidad de elementos es par")


#Clase 04 ///// Ejercicio 4 
suma = 0
inicio = 43 

while inicio < 176:
    suma += inicio
    inicio = inicio + 2 
print("La suma de los numeros impares entre 42 y 176 es: " , suma)

#Clase 04 //// Ejercicio 5 
#Desarrollar un programa que imprima la suma de los numeros
#impares comprendidos entre 1 y N. El valor de N se ingresa.
n = int(input("Ingrese un numero: "))
i = 1 

while i <= n:
    print(i)

#Clase 04 //// Ejercico 6
#Mostrar la tabla de multiplicar (entre 1 y 12) del numero 4. 
#¿Como cambiaria el algoritmo para que el usuario pueda decidir la
#tabla de multiplicar a mostrar?
tabla = 1 

while tabla <= 12:
    print("4 x", tabla, "=", tabla * 4)
    tabla += 1 


#Clase 04 //// Ejercicio 7 
#Leer 10 numeros enteros e imprimir su promedio, el mayor valor leido
#y en que posicion se encontraba. Si se ingreso mas de una vez
#solo debe informar la primera 
init = 0 
mayorValor= 0 
suma = 0 
posicion = 0

while init < 10: 
    n = int(input("Ingrese un numero: "))



