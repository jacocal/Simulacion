import numpy as np

dim = 4

estados_totales = np.zeros((dim,dim))

pay =           [1, 0, 0, 0]
incobrable =    [0, 1, 0, 0]
menor_mes =     [.6, 0, .1, .3]
mes_a_3 =       [.3, .3 , .2, .2]

estudiantes = [50, 30]
vector = np.array(estudiantes)

for x in range(dim):
    estados_totales[0,x] = pay[x]
    estados_totales[1,x] = incobrable[x]
    estados_totales[2,x] = menor_mes[x]
    estados_totales[3,x] = mes_a_3[x]

I = np.matrix([[estados_totales[0,0], estados_totales[0,1]],
                [estados_totales[1,0], estados_totales[1,1]]])
o = np.matrix([[estados_totales[0,2], estados_totales[0,3]],
               [estados_totales[1,2], estados_totales[1,3]]])
A = np.matrix([[estados_totales[2,0], estados_totales[2,1]],
                [estados_totales[3,0], estados_totales[3,1]]])
B = np.matrix([[estados_totales[2,2], estados_totales[2,3]],
                [estados_totales[3,2], estados_totales[3,3]]])

F = np.subtract(I,B)

invF = np.linalg.inv(F)

res = np.dot(invF, A)

print("{} estudiantes aprobaran\n{} estudiantes reprobaran".format(round(vector.dot(res)[0,0]), round(vector.dot(res)[0,1])))
