import numpy as np
from random import *

minutos = 5000
hora = 60

lamda = 40

fila = 0

cajero1 = 0
cajero2 = 0
cajero3 = 0

cajeros = [cajero1, cajero2, cajero3]
clientes = []
tiempos = []
exito = 0

for minuto in range(minutos):
    if((minuto % hora) == 0):
        exito += 1
        llegadas = np.random.poisson(lam=lamda)
        clientes.append(llegadas)
        fila += llegadas

    for cajero in cajeros:
        while(cajero == 0):
            if fila == 0:
                break
            else:
                transaccion = randint(0, 1)
                tiempos.append(transaccion)
                fila -= 1
                cajero = transaccion

print("Promedio clientes: %.2f\n"
    "Promedio tiempos: %.2f"
    % (sum(clientes)/len(clientes), sum(tiempos)/len(tiempos)))
