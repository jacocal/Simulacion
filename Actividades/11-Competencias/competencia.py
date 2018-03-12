# Evaluacion de competencias A01021795 Jacobo Calderon Miklos
sobrantes = 0
totales = 0
descargas_totales = 0
dias_retraso = 0

arrivals = 0
unload = 0

llegadas =  [37, 77, 13, 10, 2, 18, 31, 19, 32, 85, 31, 94, 81, 43, 31]
descargas = [69, 84, 12, 94, 51, 36, 17, 2, 15, 29, 16, 52, 56, 43, 26]

# print("{} - {}".format(len(llegadas), len(descargas)))

for l, d in zip(llegadas, descargas):
    if(1 < l <= 13):
        arrivals = 0
    elif(13 < l <= 30):
        arrivals = 1
    elif(30 < l <= 45):
        arrivals = 2
    elif(45 < l <= 70):
        arrivals = 3
    elif(70 < l <= 90):
        arrivals = 4
    elif(90 < l <= 100):
        arrivals = 5
    else:
        print("Probabilidad inexistente")
        break
    if(1 < d <= 5):
        unload = 1
    elif(5 < d <= 20):
        unload = 2
    elif(20 < d <= 70):
        unload = 3
    elif(70 < d <= 90):
        unload = 4
    elif(90 < d <= 100):
        unload = 5
    else:
        print("Probabilidad inexistente")
        break
    totales += arrivals
    sobrantes += arrivals
    if(unload < arrivals):
        dias_retraso += 1
    if(sobrantes <= unload):
        descargas_totales += sobrantes
        sobrantes = 0
    else:
        descargas_totales += unload
        sobrantes -= unload

print("Promedio de retrasos:\t{}\n"
    "Promedio de llegadas:\t{}\n"
    "Promedio de descargas:\t{}\n"
    .format(round(sobrantes/dias_retraso, 2), round(totales/len(llegadas), 2), round(descargas_totales/len(llegadas), 2))
    )
