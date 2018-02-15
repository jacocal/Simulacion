import numpy as np

simulations = 5000

n = 6
theta = 1/2
lamda = 3

costoXunidadXdia = 1
costoXfaltanteXunidad = 10
costoXorden = 50

max_inventario = 30

costo1 = 0
costo2 = 0

inventario1 = 0
inventario2 = 0

falta1 = 0
falta2 = 0

def ordenar(inventario, entrega, costo, flag=False):
    if(flag == False):
        if(inventario < max_inventario):
            inventario += entrega
            costo += costoXorden
            entrega = np.random.poisson(lam=lamda)
            return ordenar(inventario, entrega, costo)
        else:
            return max_inventario, costo
    else:
        if(inventario <= 10):
            return ordenar(inventario, entrega, costo)
        else:
            return inventario, costo

for sim in range(simulations):
    demanda = np.random.binomial(n, theta)
    entrega = np.random.poisson(lam=lamda)

    if(sim == 0 or sim % 7):
        inventario1, costo1 = ordenar(inventario1, entrega, costo1)

    inventario2, costo2 = ordenar(inventario2, entrega, costo2, True)

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
    % (costo1/simulations, costo2/simulations))

if(costo1/simulations < costo2/simulations):
    print("La opción 1 es mas economica")
elif(costo2/simulations < costo1/simulations):
    print("La opción 2 es mas economica")
else:
    print("Ambas cuestan lo mismo")
