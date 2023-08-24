try:
    horas = float(input("Introduzca las Horas: "))
    tarifa = float(input("Introduzca la Tarifa por hora: "))
except:
    print("Error, por favor introduzca un número")
else:
    if horas > 40:
        salario = 40 * tarifa + (horas - 40) * (tarifa * 1.5)
    else:
        salario = horas * tarifa

    print("Salario:", salario)
