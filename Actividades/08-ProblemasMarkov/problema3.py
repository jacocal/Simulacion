import numpy as np

dim = 3
matrix = np.zeros((dim,dim))

mercado = [.3,.5,.2]
new_mercado = [.38, .42, .2]
vector = np.array(mercado)

hicourt_ret = [.8, .1, .1]
printing_ret = [.2, .7, .1]
gandy_ret = [.2, .2, .6]

for x in range(dim):
    matrix[0,x] = hicourt_ret[x]
    matrix[1,x] = printing_ret[x]
    matrix[2,x] = gandy_ret[x]

it = 0

while(True):
    tmp = vector
    vector = np.dot(vector,matrix)
    it += 1
    if(np.array_equal(vector, tmp)):
        print("El vector estable es: {}\nSe logro en {} iteraciones".format(vector, it))
        break
    else:
        continue
