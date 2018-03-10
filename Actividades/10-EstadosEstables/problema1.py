import numpy as np

dim = 6
alumnos = 100

estados_totales = np.zeros((dim,dim))

primer =        [.1, .8, 0, 0, .1, 0]
intermedio =    [0, .1, .85, 0, .05, 0]
avanzado =      [0, 0, .15, .8, .05, 0]
final =         [0, 0, 0, .1, .05, .85]
desertan =      [0, 0, 0, 0, 1, 0]
graduan =       [0, 0, 0, 0, 0, 1]

estudiantes = [alumnos, 0, 0, 0, 0, 0]
vector = np.array(estudiantes)

cont = 0
primero = 0
ultimo = 0

for x in range(dim):
    estados_totales[0,x] = primer[x]
    estados_totales[1,x] = intermedio[x]
    estados_totales[2,x] = avanzado[x]
    estados_totales[3,x] = final[x]
    estados_totales[4,x] = desertan[x]
    estados_totales[5,x] = graduan[x]

while(True and cont<100):
    if(vector[-1] > 0):
        primero = cont
    if((round(vector[-1] + vector[-2], 0)) < alumnos):
        vector = vector.dot(estados_totales)
        cont += 1
    else:
        ultimo = cont
        print('De {} estudiantes, {} se graduaron y {} desertaron\n'
            'La probabilidad de graduarse es: {}\n'
            'El primedio de tiempo en la universidad es: {}'
            .format(alumnos, int(vector[-1]), int(vector[-2]), round(vector[-1]/alumnos, 2), (primero+ultimo)/2)
            )
        break
