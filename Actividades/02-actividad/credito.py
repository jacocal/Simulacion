import random
import math
from scipy.stats import norm

simulations = 5000
continues = 0
success = 0
hombres = 0
standard = 0

contesta = 0.3
mujer = 0.8
venta_mujer = 0.15
venta_hombre = 0.25

comision = 200
condicion = 5000

comisiones = []
descriptiva = []

standard_sum = 0

for x in range(simulations):
    tmp = random.random()
    hombre = False
    if(tmp <= contesta):
        tmp = random.random()
    else:
        continue
    if(tmp > mujer):
        hombre = True
        hombres += 1
    tmp = random.random()
    if(hombre):
        if(tmp <= venta_hombre):
            tmp = random.random()
            if(tmp <= 0.1):
                credito = 5000
            elif(tmp > 0.1 and tmp <= 0.5):
                credito = 10000
            elif(tmp > 0.5 and tmp <= 0.8):
                credito = 15000
            else:
                credito = 20000
        else:
            continue
        comisiones.append((credito/condicion)*comision)
    else:
        if(tmp <= venta_mujer):
            tmp = random.random()
            if(tmp <= 0.6):
                credito = 5000
            elif(tmp > 0.6 and tmp <= 0.9):
                credito = 10000
            else:
                credito = 15000
        else:
            continue
        comisiones.append((credito/condicion)*comision)

for item in comisiones:
    standard_sum += (item-(sum(comisiones)/len(comisiones)))**2

standard = math.sqrt(standard_sum/(len(comisiones)-1))

print("Comisiones: " + str(int(sum(comisiones))))
print("Standard deviation: " + str(standard))
print("Confianza (+): " + str((sum(comisiones)/len(comisiones)) + (1.96 * standard/math.sqrt(len(comisiones)))))
print("Confianza (-): " + str((sum(comisiones)/len(comisiones)) - (1.96 * standard/math.sqrt(len(comisiones)))))
