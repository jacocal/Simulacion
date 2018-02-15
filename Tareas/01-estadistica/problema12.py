import numpy as np
from random import *

minutos = 5000
hora = 60

lamda = 20
exponencial = 2

fila1 = 0
fila2 = 0

for x in range(minutos):
    if(x % hora == 0):
        #Llegadas por hora
        llegadas = np.random.poisson(lam=lamda)
    else:
        llegadas = 0

    fila1 += llegadas
    #Servicio por minuto en fila 1
    servicio1 = int(np.random.exponential(scale=2))
    if(fila1 > servicio1):
        fila1 -= servicio1
        fila2 += servicio1
    else:
        fila1 = 0
        fila2 += servicio1 - fila1

    #Servicio por minuto en fila 2
    servicio2 = randint(1,2)
    if(fila2 > servicio2):
        fila2 -= servicio2
    else:
        fila2 = 0

print("El tamaño de la fila 1 es: %s\n"
    "El tamaño de la fila 2 es %s"
    % (fila1, fila2))

if(fila1 < fila2):
    print("La fila 1 es mas corta")
elif(fila2 < fila1):
    print("La fila 2 es mas corta")
else:
    print("Ambas tienen el mismo")
