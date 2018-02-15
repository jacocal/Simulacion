import numpy as np
import random

#Horas
horas = 20000
tiempo_transcurrido1 = 0
tiempo_transcurrido2 = 0

#Integer
componentes = 4

#Horas
horas_vida_media = 600
horas_std_dev = 100

#horas de desconexion
desc1 = 1
desc4 = 2

#Dinero
costoComponente = 200
costoDescHora = 100

costo1 = 0
costo2 = 0

while(tiempo_transcurrido1 < horas):
    tiempos = []
    for i in range(componentes):
        rand = random.randint((horas_vida_media - horas_std_dev), (horas_vida_media + horas_std_dev))
        tiempos.append(rand)
    tiempo_transcurrido1 += max(tiempos)
    if(tiempo_transcurrido1 >= horas):
        pass
    else:
        costo1 += (costoComponente + (costoDescHora * desc1)) * componentes

while(tiempo_transcurrido2 < horas):
    rand = random.randint((horas_vida_media - horas_std_dev), (horas_vida_media + horas_std_dev))
    tiempo_transcurrido2 += rand
    if(tiempo_transcurrido2 >= horas):
        pass
    else:
        costo2 += (costoComponente * componentes) + (costoDescHora * desc4)

print("El promedio de la opcion 1 cuesta: %s la hora\n"
    "El promedio de la opcion 2 cuesta %s la hora"
    % (costo1/horas, costo2/horas))

if(costo1/horas < costo2/horas):
    print("La opción 1 es mas economica")
elif(costo2/horas < costo1/horas):
    print("La opción 2 es mas economica")
else:
    print("Ambas cuestan lo mismo")
