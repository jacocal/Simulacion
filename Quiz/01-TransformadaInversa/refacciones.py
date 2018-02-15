import numpy as np
import random
import math
from scipy.special import ndtri

simulations = 5000
lista_porcentaje = [75, 80, 85, 90, 95]

costos = []

for sim in range(simulations):
    costo = 0
    random_carros = np.random.choice(
        [3,4,5,6,7,8],
        6,
        p=[.05,.15,.3,.25,.15,.1],
        replace=False
    )[0]

    for carro in range(random_carros):
        random_tamaño = random.randint(0,2)
        if(random_tamaño == 0):
            costo += np.random.choice(
                [350,1575,1925,2450,700],
                5,
                p=[.45,.15,.2,.1,.1],
                replace=False
            )[0]
        elif(random_tamaño == 1):
            costo += np.random.choice(
                [550,1975,2545,2925,700],
                5,
                p=[.25,.25,.15,.2,.15],
                replace=False
            )[0]
        else:
            costo += np.random.choice(
                [750,2275,2845,3415,700],
                5,
                p=[.1,.15,.3,.4,.05],
                replace=False
            )[0]
    costos.append(costo)

for pg in lista_porcentaje:
    print("Confianza para " + str(pg) + "%: [" +
        str(sum(costos)/simulations - ndtri((pg/100+1)/2)*(np.std(costos)/math.sqrt(simulations))) + ", " +
        str(sum(costos)/simulations + ndtri((pg/100+1)/2)*(np.std(costos)/math.sqrt(simulations))) + "]")
