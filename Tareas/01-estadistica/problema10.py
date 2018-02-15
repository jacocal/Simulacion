import numpy as np

costoXordenar = 50
costoXunidadXano = 26
costoXfaltante = 25

dias_trabajo_ano = 260

inv0 = 15

demanda_diaria = np.random.choice(
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    1,
    p=[.04, .06, .1, .2, .3, .18, .08, .03, .01],
    replace=False
)[0]

entrega_dias = np.random.choice(
    [1, 2, 3, 4],
    1,
    p=[.25, .5, .2, .05],
    replace=False
)[0]
