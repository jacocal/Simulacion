import numpy as np
from random import *

minutos = 5000
hora = 60

lamda = 10/hora

lugares = [0, 0, 0, 0, 0, 0]

perdidos = 0
estacionado = 0
espacios = 0

clientes = 0

for m in range(minutos):
    llegadas = np.random.poisson(lam=lamda)
    clientes += llegadas
    if llegadas != 0:
        for x in range(llegadas):
            try:
                lugares[lugares.index(0)] = randint(10, 30)
                estacionado += 1
            except ValueError:
                perdidos += 1
    for i, lugar in enumerate(lugares):
        if(lugar > 0):
            lugares[i] = lugar - 1

    espacios += sum(l == 0 for l in lugares)

print("Porcentaje de clientes perdidos: %.2f%%\n"
    "Probabilidad de encontrar lugar: %.2f%%\n"
    "Promedio de lugares disponibles: %.2f"
    % (perdidos/clientes, estacionado/clientes, espacios/minutos))
