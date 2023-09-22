notaA = int(input("Ingrese la nota del primer parcial: "))
notaB = int(input("Ingrese la nota del segundo parcial: "))

if notaA < 0 or notaA > 10 or notaB < 0 or notaB > 10:
    print("Error, las notas deben estar entre 0 y 10")
else:
    if notaA >= 7 and notaB >= 7:
        resultado = "Promocionó"
    elif notaA >= 4 and notaB >= 4:
        resultado = "Aprobó"
    else:
        resultado = "debe recuperar"
    print("El alumno", resultado)