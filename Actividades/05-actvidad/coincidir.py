import random

simulations = 5000

espera_hombre = 20
espera_mujer = 15

exito = 0

for sim in range(simulations):
    randh = random.randint(0, 60)
    randm = random.randint(0, 60)
    if(randh < randm):
        if((randh + espera_hombre) >= randm):
            exito += 1
    else:
        if((randm + espera_mujer >= randh)):
            exito += 1

print(exito/simulations)
