import numpy as np
from queue import Queue

ventanilla1 = False
ventanilla2 = False
llegada = Queue()
servicio = Queue()

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
        llegada.put(1)
    elif(t_l <= prob_llegada[1]):
        llegada.put(2)
    elif(t_l <= prob_llegada[2]):
        llegada.put(3)
    elif(t_l <= prob_llegada[3]):
        llegada.put(4)
    elif(t_l <= prob_llegada[4]):
        llegada.put(5)

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

for t_s in service:
    t_s = t_s/100
    if(t_s <= prob_llegada[0]):
        servicio.put(1)
    elif(t_s <= prob_llegada[1]):
        servicio.put(2)
    elif(t_s <= prob_llegada[2]):
        servicio.put(3)
    elif(t_s <= prob_llegada[3]):
        servicio.put(4)
    elif(t_s <= prob_llegada[4]):
        servicio.put(5)
    elif(t_s <= prob_llegada[5]):
        servicio.put(6)

costo1a = salarios_anuales/8760 + costo_anual_ventanilla[0]/8760
extra1a = 0
transcurrido = 0
for t_l, t_s in zip(min_llegada, min_servicio):
    if(transcurrido >= sim1):
        break
    else:
        t_s += extra1a
        if(t_l == t_s):
            transcurrido += t_l
        if(t_l > t_s):
            if(extra1a > (t_l - t_s)):
                extra1a = t_l - t_s
            else:
                extra1a = 0
            transcurrido += t_l
        elif(t_s > t_l):
            transcurrido += t_s
            costo1a += t_s - t_l
            extra1a += t_s - t_l
r_sim1.append(costo1a)

costo1b = salarios_anuales/8760 * 2 + costo_anual_ventanilla[1]/8760
extra1b = 0
transcurrido = [0, 0]
transcurridoTotal = 0
while(llegada.empty() == False):
    if(transcurridoTotal >= sim1):
        break
    if(ventanilla1 == False):
        l1 = llegada.get()
        s1 = servicio.get()
        ventanilla1 = True
    else:
        s1 += extra1b
        if(l1 == s1):
            transcurrido[0] += l1
        if(l1 > s1):
            if(extra1b > (l1 - s1)):
                extra1b= l1 - s1
            else:
                extra1b = 0
            transcurrido[0] += l1
        elif(t_s > t_l):
            transcurrido[0] += s1
            costo1b += s1 - l1
            extra1b += s1 - l1
    if(ventanilla2 == False):
        l2 = llegada.get()
        s2 = servicio.get()
        ventanilla2 = True
    else:
        s2 += extra1b
        if(l2 == s2):
            transcurrido[0] += l2
        if(l2 > s2):
            if(extra1b > (l2 - s2)):
                extra1b = l2 - s2
            else:
                extra1b = 0
            transcurrido[0] += l2
        elif(t_s > t_l):
            transcurrido[0] += s2
            costo1b += s2 - l2
            extra1b += s2 - l2
    transcurridoTotal += max(transcurrido)
r_sim1.append(costo1b)

r_sim2.append(r_sim1[0]*7*200 + salarios_anuales + costo_anual_ventanilla[0])
r_sim2.append(r_sim1[1]*7*200 + salarios_anuales*2 + costo_anual_ventanilla[1])

if(r_sim1[0] < r_sim1[1]):
    print("Es mas barato con 1 ventanilla durante 1 hora, con un costo de: $%.2f\n"
        "2 ventanillas cuestan: $%.2f"
        % (r_sim2[0], r_sim2[1]))
elif(r_sim1[1] < r_sim1[0]):
    print("Es mas barato con 2 ventanillas durante 1 hora, con un costo de: $%.2f\n"
        "1 ventanilla cuesta: $%.2f"
        % (r_sim2[1], r_sim2[0]))
else:
    print("Ambas opciones cuestan lo mismo: $%.2f por hora" % r_sim1[1])

if(r_sim2[0] < r_sim2[1]):
    print("Es mas barato con 1 ventanilla anual, con un costo de: $%.2f\n"
        "2 ventanillas cuestan: $%.2f"
        % (r_sim2[0], r_sim2[1]))
elif(r_sim2[1] < r_sim2[0]):
    print("Es mas barato con 2 ventanillas anual, con un costo de: $%.2f\n"
        "1 ventanillas cuesta: $%.2f"
        % (r_sim2[1], r_sim2[0]))
else:
    print("Ambas opciones cuestan lo mismo: $%.2f por hora" % r_sim2[1])
