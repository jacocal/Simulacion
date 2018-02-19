import numpy as np
from random import *

simulations = 5000

dim = 3
mat = np.zeros((dim,dim))
matrixes = []
avg_mat = np.zeros((dim, dim))

for sim in range(simulations):
    for r in range(dim):
        for c in range(dim):
            mat[r,c] = round(random(),2)

    for r in range(dim):
        div = mat[r].sum()
        for c in range(dim):
            if(c == dim-1):
                mat[r,c] = 1-(mat[r,:-1].sum())
            else:
                mat[r,c] = round(mat[r,c]/div,2)

    matrixes.append(mat)

for r in range(dim):
    for c in range(dim):
        suma = 0
        for m in matrixes:
            suma += m[r,c]
        avg_mat[r,c] = suma/simulations

print(avg_mat)
