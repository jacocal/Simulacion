import numpy as np

dim = 8
articulos = 1000
costo = 0
completados = 0

estados_totales = np.zeros((dim,dim))

maquinaA =      [0, .93, 0, 0, 0, 0, .07, 0]
inspectorA =    [.04, 0, .94, 0, .0, 0, .02, 0]
maquinaB =      [0, 0, 0, .95, 0, 0, .05, 0]
inspectorB =    [0, 0, .03, 0, .96, 0, .01, 0]
maquinaC =      [0, 0, 0, 0, 0, .97, .03, 0]
inspectorC =    [0, 0, 0, 0, .01, 0, .01, .98]
desechos =      [0, 0, 0, 0, 0, 0, 1, 0]
empaque =       [0, 0, 0, 0, 0, 0, 0, 1]

items = [articulos, 0, 0, 0, 19, 0, 0, 0]
vector = np.array(items)

hora_hombre = [3, .25, 2.5, .25, 1.5, .25, 0, .1]
costo_hora = [10, 10, 10, 10, 12, 10, 0, 8]
gastos = []

for h, c in zip(hora_hombre, costo_hora):
    gastos.append(h*c)

for x in range(dim):
    estados_totales[0,x] = maquinaA[x]
    estados_totales[1,x] = inspectorA[x]
    estados_totales[2,x] = maquinaB[x]
    estados_totales[3,x] = inspectorB[x]
    estados_totales[4,x] = maquinaC[x]
    estados_totales[5,x] = inspectorC[x]
    estados_totales[6,x] = desechos[x]
    estados_totales[7,x] = empaque[x]

c1 = 0

while(int(vector[-1] < articulos)):
    if(int(vector[-1]) < articulos and round(vector[-1] + vector[-2], 0) >= articulos):
        vector[0] += 1
    costo += (vector.dot(gastos) - (c1 * gastos[-1]))
    c1 = int(vector[-1])
    vector = vector.dot(estados_totales)

print('Se necesita {} articulos para lograr empacar y transportar {}\n'
    'El costo de empacar {} es: ${}'
    .format(int(vector[-1] + vector[-2]), articulos, articulos, round(costo,2))
    )
