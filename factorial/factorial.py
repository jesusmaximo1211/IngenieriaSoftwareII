#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#en caso de no ingresar un numero y apretar Ejecutar, la consola muestra un mensaje pidiendo que informe un numero, permitiendo que lo ingrese. de no volver a ingresarlo, el programa se torna invalido y se cierra.
if len(sys.argv) == 1:
    try:
        num = int(input("Debe informar un número!"))
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
        sys.exit(1)
else:
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("El argumento proporcionado no es un número válido.")
        sys.exit(1)

print("Factorial", num, "! es", factorial(num)) 