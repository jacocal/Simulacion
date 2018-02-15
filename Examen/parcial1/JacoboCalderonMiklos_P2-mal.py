import numpy as np

horas_abiertas = 7
dias_trabajados = 200

sim1 = 60
sim2 = 60*horas_abiertas*dias_trabajados

ventanillas = [1, 2]
costo_anual_ventanilla = [12000, 20000]
salarios_anuales = 16000
costoXminuto = 1
personal_extra = 16000

observaciones = 1000

interrival = [52, 37, 82, 69, 98, 96, 33, 50, 88, 90, 50, 27, 45, 81, 66, 74, 30, 59, 67, 28, 2, 74, 35, 24, 3, 29, 60, 74, 85, 90]
service =    [60, 60, 80, 53, 69, 37, 6, 63, 57, 2, 94, 52, 69, 33, 32, 30, 48, 88, 33, 48, 72, 33, 62, 13, 74, 68, 22, 44, 42, 9]

ocurrencias_llegada = [200/observaciones, 250/observaciones, 300/observaciones, 150/observaciones, 100/observaciones]
ocurrencias_servicio = [100/observaciones, 150/observaciones, 350/observaciones, 150/observaciones, 150/observaciones, 100/observaciones]
minutos_llegada = [1, 2, 3, 4, 5]
minutos_servicio = [1, 2, 3, 4, 5, 6]

prob_llegada = [0.2, 0.45, 0.75, .90, 1]
prob_servicio = [0.1, 0.25, 0.6, 0.75, 0.9, 1]

min_llegada = []
min_servicio = []

r_sim1 = []
r_sim2 = []

for t_l in interrival:
    t_l = t_l/100
    if(t_l <= prob_llegada[0]):
        min_llegada.append(1)
    elif(t_l <= prob_llegada[1]):
        min_llegada.append(2)
    elif(t_l <= prob_llegada[2]):
        min_llegada.append(3)
    elif(t_l <= prob_llegada[3]):
        min_llegada.append(4)
    elif(t_l <= prob_llegada[4]):
        min_llegada.append(5)

for t_s in service:
    t_s = t_s/100
    if(t_s <= prob_llegada[0]):
        min_servicio.append(1)
    elif(t_s <= prob_llegada[1]):
        min_servicio.append(2)
    elif(t_s <= prob_llegada[2]):
        min_servicio.append(3)
    elif(t_s <= prob_llegada[3]):
        min_servicio.append(4)
    elif(t_s <= prob_llegada[4]):
        min_servicio.append(5)
    elif(t_s <= prob_llegada[5]):
        min_servicio.append(6)

for idx, ventanilla in enumerate(ventanillas):
    costo += salarios_anuales/525600 + costo_anual_ventanilla[1]/525600
    extra = 0
    transcurrido = 0
    for t_l, t_s in zip(min_llegada, min_servicio):
        if(transcurrido >= sim1):
            break
        else:
            t_s += extra
            if(t_l == t_s):
                transcurrido += t_l
            if(t_l > t_s):
                if(extra > (t_l - t_s)):
                    extra = t_l - t_s
                else:
                    extra = 0
                transcurrido += t_l
            elif(t_s > t_l):
                transcurrido += t_s
                costo += t_s - t_l
                extra += t_s - t_l
    r_sim1.append(costo)

for idx, ventanilla in enumerate(ventanillas):
    costo = costo_anual_ventanilla[idx] + salarios_anuales * ventanilla
    extra = 0
    transcurrido = 0
    for x in range(sim2):
        if(x + transcurrido >= sim2):
            break
        if(x % 1440 == 0):
            extra = 0
        llegada = np.random.choice(
            minutos_llegada,
            1,
            p=ocurrencias_llegada,
            replace=False
        )[0]

        servicio = np.random.choice(
            minutos_servicio,
            1,
            p=ocurrencias_servicio,
            replace=False
        )[0]

        servicio += extra
        if(llegada == servicio):
            transcurrido += llegada-1
        if(llegada > servicio):
            if(extra > (llegada - servicio)):
                extra = llegada - servicio
            else:
                extra = 0
            transcurrido += llegada-1
        elif(servicio > llegada):
            transcurrido += servicio-1
            costo += servicio - llegada
            extra += servicio - llegada
    r_sim2.append(costo)

if(r_sim1[0] < r_sim1[1]):
    print("Es mas barato con 1 ventanilla durante 1 hora, con un costo de: $%i" % r_sim1[0])
elif(r_sim1[1] < r_sim1[0]):
    print("Es mas barato con 2 ventanillas durante 1 hora, con un costo de: $%i" % r_sim1[1])
else:
    print("Ambas opciones cuestan lo mismo: $%i por hora" % r_sim1[1])

if(r_sim2[0] < r_sim2[1]):
    print("Es mas barato con 1 ventanilla anual, con un costo de: $%i" % r_sim2[0])
elif(r_sim2[1] < r_sim2[0]):
    print("Es mas barato con 2 ventanillas anual, con un costo de: $%i" % r_sim2[1])
else:
    print("Ambas opciones cuestan lo mismo: $%i anual" % r_sim2[1])
