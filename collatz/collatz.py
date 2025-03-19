import matplotlib.pyplot as plt #importar la libreria matplotlib (su modulo pyplot) y darle el alias "plt"  sirve para poder hacer el grafico solicitado

# Función para calcular la secuencia de collatz (3n+1)
def secuencia_collatz(n):
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2 
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

#listas para almacenar los números y las iteraciones
numeros = []
iteraciones = []

for i in range(1, 10000):
    iteracion = secuencia_collatz(i)
    numeros.append(i)
    iteraciones.append(iteracion)

# grafico
plt.figure(figsize=(10, 6))
plt.scatter(numeros, iteraciones, s=1, color='blue')

plt.title("Número de iteraciones de la Conjetura de Collatz") #titulo
plt.xlabel("Número inicial (n)") #nombre en eje x
plt.ylabel("Número de iteraciones") #nombre en eje y
plt.show() #mostrar