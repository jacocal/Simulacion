import numpy as np
from random import *

dias = 1250
trabajadoXano = 250

costo_camion_anual = 100000

max_camiones = 15

costo_tonelada = 100

camiones = []

costos = []
gasto = 0

for i in range(max_camiones+1):
    camiones.append(i)

for camion in camiones:
    gasto = 0
    for dia in range(dias):
        produccion = np.random.choice(
            [randint(50,55), randint(55,60), randint(60,65),
            randint(65,70), randint(75,80), randint(80,85)],
            1,
            p=[.1, .15, .3, .35, .08, .02],
            replace=False
        )[0]

        for c in range(camion):
            trasladoXcamion = np.random.choice(
                [round(uniform(4.0, 4.5), 1), round(uniform(4.5, 5.0), 1), round(uniform(5.0, 5.5), 1), round(uniform(5.5, 6.0), 1)],
                1,
                p=[.3, .4, .2, .1],
                replace=False
            )[0]
            if(produccion > trasladoXcamion):
                produccion -= trasladoXcamion
            else:
                produccion = 0

        gasto += produccion * costo_tonelada

        if(((dia % trabajadoXano-1) == 0) and dia != 0):
            gasto += costo_camion_anual * camion
    costos.append([gasto, camion])

print("El costo minimo en %i dias es de: $%i\n"
    "Teniendo %i camiones"
    % (dias, min(costos)[0], min(costos)[1]))
