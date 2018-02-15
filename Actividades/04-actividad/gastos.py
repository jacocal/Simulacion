import random

simulations = 5000

salario = 3000
gastos_transporte = [1300, 1800, 2300, 2800, 3300, 3800]
apartar = 0.4
apartar_neg = 0.1

ahorro = 0

for x in range(simulations):
    rand = random.randint(0,len(gastos_transporte)-1)
    gasto = gastos_transporte[rand]
    if((salario - gasto) >= 0):
        dinero = salario - gasto
        dinero *= 1-apartar
    else:
        ahorro += salario - gasto
        ahorro -= salario * apartar_neg
        dinero = 0
    ahorro += dinero

print("Ahorro promedio: " + str(ahorro))
