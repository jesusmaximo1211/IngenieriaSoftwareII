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

#usamos la funcion factorial para, obteniendo el rango poder hacer el factorial.
def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print(f"Factorial de {num} es {factorial(num)}")

#en caso de no ingresar un numero y apretar Ejecutar, la consola muestra un mensaje pidiendo que informe un numero, permitiendo que lo ingrese. de no volver a ingresarlo, el programa se torna invalido y se cierra.
if len(sys.argv) > 1:
    argumento = sys.argv[1]
else:
    argumento = input("Ingrese un número o un rango (ej. 4-8 o -10 o 5-): ")


#Para saber si es un solo numero o un rango (ademas de si tiene o no limite inferior/superior)
if '-' in argumento:
    #  sin límite inferior
    if argumento.startswith('-'):
        hasta = int(argumento[1:])  
        desde = 1 
        calcular_factoriales(desde, hasta)

    # sin límite superior
    elif argumento.endswith('-'):
        desde = int(argumento[:-1])  
        hasta = 60  
        calcular_factoriales(desde, hasta)

    # Rango con ambos límites
    else:
        desde, hasta = map(int, argumento.split('-'))
        calcular_factoriales(desde, hasta)

else:
    num = int(argumento)
    print(f"Factorial de {num} es {factorial(num)}")
  