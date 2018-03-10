import numpy as np

dim = 3
clientes_iniciales = 200000
matrix = np.zeros((dim,dim))

doorway = [.8,.1,.1]
bell = [.05,.9,.05]
kumpaq = [.2,.1,.7]

cantidad = [clientes_iniciales, clientes_iniciales, clientes_iniciales]
vector = np.array(cantidad)

for x in range(dim):
    matrix[0,x] = doorway[x]
    matrix[1,x] = bell[x]
    matrix[2,x] = kumpaq[x]

it = 0

while(True):
    tmp = vector
    vector = np.dot(vector,matrix)
    it += 1
    if(np.array_equal(vector, tmp)):
        print("El vector etable es: {}\nSe logro en {} iteraciones".format(vector, it))
        break
    else:
        continue
