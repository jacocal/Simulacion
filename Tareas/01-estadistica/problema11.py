import numpy as np

costoXordenar = 100
costoXunidadXano = 52
costoXfaltanteXespera = 20
costoXfaltanteNoespera = 50

dias_trabajo_ano = 260

inv0 = 100

demanda_diaria = np.random.choice(
    [25, 26, 27, 28, 29, 30, 31, 32, 33, 34],
    1,
    p=[.02, .04, .06, .12, .2, .24, .15, .10, .05, .02],
    replace=False
)[0]

entrega_dias = np.random.choice(
    [1, 2, 3, 4],
    1,
    p=[.2, .3, .25, .25],
    replace=False
)[0]

espera_dias = np.random.choice(
    [0, 1, 2, 3, 4],
    1,
    p=[.4, .2, .15, .15, .1],
    replace=False
)[0]
