import numpy as np

dias = 20

n = 6
theta = 1/2
lamda = 3

costoXunidadXdia = 1
costoXfaltanteXunidad = 10
costoXorden = 50

max_inventario = 30
min_inventario = 10

costo1 = 0
costo2 = 0

inventario1 = 0
inventario2 = 0

falta1 = 0
falta2 = 0

for dia in range(dias):
    demanda = np.random.binomial(n, theta)

    if((dia % 7) == 0):
        entrega1 = np.random.poisson(lam=lamda)
        costo1 += costoXorden
        llegada1 = dia + entrega1

    if(inventario2 <= min_inventario):
        entrega2 = np.random.poisson(lam=lamda)
        costo2 += costoXorden
        llegada2 = dia + entrega1

    if(dia == llegada1):
        inventario1 = max_inventario

    if(dia == llegada2):
        inventario2 = max_inventario

    if(inventario1 >= demanda):
        inventario1 -= demanda
        costo1 += inventario1 * costoXunidadXdia
    else:
        falta1 += demanda - inventario1

    if(inventario2 >= demanda):
        inventario2 -= demanda
        costo2 += inventario2 * costoXunidadXdia
    else:
        falta2 += demanda - inventario2

costo1 += abs(inventario1 - falta1) * costoXfaltanteXunidad
costo2 += abs(inventario2 - falta2) * costoXfaltanteXunidad

print("El promedio de la opcion 1 cuesta: %s\n"
    "El promedio de la opcion 2 cuesta %s"
    % (costo1/dias, costo2/dias))

if(costo1/dias < costo2/dias):
    print("La opción 1 es mas economica")
elif(costo2/dias < costo1/dias):
    print("La opción 2 es mas economica")
else:
    print("Ambas cuestan lo mismo")
