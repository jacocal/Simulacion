import numpy as np
import random

I2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
R2 = np.array([[.05, .1, 0, 0, 0, 0], [.02, 0, .2, .5, 0, 0], [.01, 0, 0, 0, .6, .2]])
Q2 = np.array([[.3, .55, 0], [0, .2, .08], [0, 0, .19]])
F2 = np.linalg.inv(np.subtract(I2, Q2))
FR2 = np.matmul(F2, R2)
print("Ejercicio 2")
print("Probabilidad de que un recien nacido muera: {}".format(round(FR2[0][0],2)))
ganancia2 = 0
for i in range(1000):
    rand2 = random.random()
    # Venta nivel 1
    if rand2 <= FR2[0][1]:
        ganancia2 += 2000
    elif FR2[0][1] < rand2 <= FR2[0][2]:
        ganancia2 += 3000
    elif FR2[0][2] < rand2 <= FR2[0][3]:
        ganancia2 += 5000
    elif FR2[0][3] < rand2 <= FR2[0][4]:
        ganancia2 += 10000
    elif FR2[0][4] < rand2 <= FR2[0][5]:
        ganancia2 += 20000
print("La ganancia promedio para un animal recien nacido es de {}".format(ganancia2/1000))
