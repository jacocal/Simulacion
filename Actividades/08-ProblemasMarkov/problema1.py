import numpy as np

dim = 3
returnMatrix = np.zeros((dim, dim))

northside = [.8,.1,.1]
westend = [.2,.7,.1]
suburban = [.25,.15,.6]

vector = [100, 80, 60]
autos = np.array(vector)

for x in range(dim):
    returnMatrix[0,x] = northside[x]
    returnMatrix[1,x] = westend[x]
    returnMatrix[2,x] = suburban[x]

print("El vector resultante es: {}".format(np.dot(autos,returnMatrix)))
