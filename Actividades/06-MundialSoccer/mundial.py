import numpy as np
from math import *
from random import *
from queue import Queue
from time import sleep

class Equipo:
    pais = None
    media_gol = 0
    penal = 0
    nextGol = 0
    puntos_divisionales = 0
    dif_goles = 0

    def __init__(self, pais, mg, pen):
        self.pais = pais
        self.media_gol = mg
        self.penal = pen

    def getPais(self):
        return self.pais
    def getMedia(self):
        return self.media_gol
    def getPenal(self):
        return self.penal
    def getGol(self):
        return self.nextGol
    def getPuntos(self):
        return self.puntos_divisionales
    def getDif(self):
        return self.dif_goles

    def setNextGol(self, gol):
        self.nextGol += gol
    def setGol(self, gol):
        self.nextGol = gol
    def setDif(self, dif):
        self.dif_goles = dif

    def incPuntos(self):
        self.puntos_divisionales += 1

class Partido:
    equipo1 = None
    equipo2 = None
    ganador = None
    penales = 0
    goles90 = [0,0]
    goles30 = [0,0]
    exitosPen = [0, 0]

    def __init__(self, e1, e2, pen = 5):
        self.equipo1 = e1
        self.equipo2 = e2
        self.penales = pen

    def getGanador(self):
        return self.ganador

    def getGoles90(self):
        return self.goles90

    def getGoles30(self):
        return self.goles30

    def getPenales(self):
        return self.exitosPen

    def setGanador(self, equipo):
        self.ganador = equipo

    def restartGol(self):
        self.equipo1.setGol(0)
        self.equipo2.setGol(0)

    def tiempoPartido(self, minutos = 90, golE1 = 0, golE2 = 0):
        tiempo = 0
        self.equipo1.setNextGol(round(np.random.exponential(self.equipo1.getMedia())))
        self.equipo2.setNextGol(round(np.random.exponential(self.equipo2.getMedia())))
        while(tiempo <= minutos):
            if(self.equipo1.getGol() == tiempo):
                golE1 += 1
                self.equipo1.setNextGol(round(np.random.exponential(self.equipo1.getMedia())))
            if(self.equipo2.getGol() == tiempo):
                golE2 += 1
                self.equipo2.setNextGol(round(np.random.exponential(self.equipo2.getMedia())))
            if(self.equipo1.getGol() < self.equipo2.getGol()):
                tiempo = self.equipo1.getGol()
            else:
                tiempo = self.equipo2.getGol()
        self.goles90[0] = golE1
        self.goles90[1] = golE2
        if(golE1 > golE2):
            self.setGanador(self.equipo1)
        elif(golE2 > golE1):
            self.setGanador(self.equipo2)
        else:
            while(tiempo <= minutos+30):
                if(self.equipo1.getGol() == tiempo):
                    golE1 += 1
                    self.equipo1.setNextGol(round(np.random.exponential(self.equipo1.getMedia())))
                if(self.equipo2.getGol() == tiempo):
                    golE2 += 1
                    self.equipo2.setNextGol(round(np.random.exponential(self.equipo2.getMedia())))
                if(self.equipo1.getGol() < self.equipo2.getGol()):
                    tiempo = self.equipo1.getGol()
                else:
                    tiempo = self.equipo2.getGol()
            self.goles30[0] = golE1 - self.goles90[0]
            self.goles30[1] = golE2 - self.goles90[1]
            if(golE1 > golE2):
                self.setGanador(self.equipo1)
            elif(golE2 > golE1):
                self.setGanador(self.equipo2)
            else:
                penal1 = []
                penal2 = []
                for x in range(self.penales):
                    penal1.append(np.random.choice(
                            [1, 0],
                            1,
                            p=[self.equipo1.getPenal(), 1-self.equipo1.getPenal()],
                            replace=False
                        )[0]
                    )
                    penal2.append(np.random.choice(
                            [1, 0],
                            1,
                            p=[self.equipo2.getPenal(), 1-self.equipo2.getPenal()],
                            replace=False
                        )[0]
                    )
                if(sum(penal1) > sum(penal2)):
                    self.setGanador(self.equipo1)
                elif(sum(penal2) > sum(penal1)):
                    self.setGanador(self.equipo2)
                else:
                    self.setGanador(np.random.choice(
                        [self.equipo1, self.equipo2],
                        1,
                        replace=False
                        )[0]
                    )
                    # while(win == False):
                    #     penal1.append(np.random.choice(
                    #             [1, 0],
                    #             1,
                    #             p=[self.equipo1.getPenal(), 1-self.equipo1.getPenal()],
                    #             replace=False
                    #         )[0]
                    #     )
                    #     penal2.append(np.random.choice(
                    #             [1, 0],
                    #             1,
                    #             p=[self.equipo2.getPenal(), 1-self.equipo2.getPenal()],
                    #             replace=False
                    #         )[0]
                    #     )
                    #     if(sum(penal1) > sum(penal2)):
                    #         self.setGanador(self.equipo1)
                    #         break
                    #     elif(sum(penal2) > sum(penal1)):
                    #         self.setGanador(self.equipo2)
                    #         break
                    #     else:
                    #         continue
                self.exitosPen[0] = sum(penal1)/len(penal1)
                self.exitosPen[1] = sum(penal2)/len(penal2)
        self.restartGol()

    def scoreGoles(self):
        self.equipo1.setDif(self.equipo1.getDif() + self.goles90[0] - self.goles90[1] + self.goles30[0] - self.goles30[1])
        self.equipo2.setDif(self.equipo2.getDif() + self.goles90[1] - self.goles90[0] + self.goles30[1] - self.goles30[0])

class Division:
    primerLugar = None
    segundoLugar = None
    equipos = []
    matches = []

    def __init__(self, e1, e2, e3, e4):
        self.equipos = []
        self.matches = []
        self.equipos.append(e1)
        self.equipos.append(e2)
        self.equipos.append(e3)
        self.equipos.append(e4)

    def get1(self):
        return self.primerLugar
    def get2(self):
        return self.segundoLugar
    def getEquipos(self):
        return self.equipos

    def match(self):
        self.matches.append([self.equipos[0], self.equipos[1]])
        self.matches.append([self.equipos[0], self.equipos[2]])
        self.matches.append([self.equipos[0], self.equipos[3]])
        self.matches.append([self.equipos[1], self.equipos[2]])
        self.matches.append([self.equipos[1], self.equipos[3]])
        self.matches.append([self.equipos[2], self.equipos[3]])

    def play(self):
        for m in self.matches:
            p = Partido(m[0], m[1])
            p.tiempoPartido()
            p.scoreGoles()
            p.getGanador().incPuntos()

    def winner(self):
        tmp = self.equipos[0]
        for i in range(len(self.equipos)-1):
            if(tmp.getPuntos() < self.equipos[i+1].getPuntos()):
                tmp = self.equipos[i+1]
            elif(tmp.getPuntos() == self.equipos[i+1].getPuntos()):
                if(tmp.getDif() < self.equipos[i+1].getDif()):
                    tmp = self.equipos[i+1]
                elif(tmp.getDif() == self.equipos[i+1].getDif()):
                    tmp = np.random.choice(
                        [tmp, self.equipos[i+1]],
                        1,
                        replace=False
                    )[0]
                else:
                    continue
            else:
                continue
        self.primerLugar = tmp
        self.equipos.remove(tmp)

    def runner(self):
        tmp = self.equipos[0]
        for i in range(len(self.equipos)-1):
            if(tmp.getPuntos() < self.equipos[i+1].getPuntos()):
                tmp = self.equipos[i+1]
            elif(tmp.getPuntos() == self.equipos[i+1].getPuntos()):
                if(tmp.getDif() < self.equipos[i+1].getDif()):
                    tmp = self.equipos[i+1]
                elif(tmp.getDif() == self.equipos[i+1].getDif()):
                    tmp = np.random.choice(
                        [tmp, self.equipos[i+1]],
                        1,
                        replace=False
                    )[0]
                else:
                    continue
            else:
                continue
        self.segundoLugar = tmp
        self.equipos.append(self.primerLugar)

# def main():
#     simulations = 5000
#     equipos = []
#     ganadores = []
#     equipos.append(Equipo("Alemania", 48, .58))
#     equipos.append(Equipo("Portugal", 53, .4))
#     equipos.append(Equipo("Argentina", 50, .55))
#     equipos.append(Equipo("Brasil", 48, .5))
#
#     for x in range(simulations):
#         partidos = np.random.choice(
#             equipos,
#             len(equipos),
#             replace=False
#         )
#
#         semi1 = Partido(partidos[0], partidos[1])
#         semi1.tiempoPartido()
#
#         semi2 = Partido(partidos[2], partidos[3])
#         semi2.tiempoPartido()
#
#         final = Partido(semi1.getGanador(), semi2.getGanador())
#         final.tiempoPartido()
#
#         ganadores.append(final.getGanador().getPais())
#
#     print("En %i simulaciones, el ganador mas frecuente fue: %s" % (simulations, max(set(ganadores), key=ganadores.count)))
#
#     div1 = Division(equipos[0], equipos[1], equipos[2], equipos[3])
#     div1.match()
#     div1.play()
#     div1.winner()
#     div1.runner()
#
#     for e in equipos:
#         print("%s: %i puntos, %i goles" % (e.getPais(), e.getPuntos(), e.getDif()))
#
#     print(div1.get1().getPais())
#     print(div1.get2().getPais())

def main():
    simulations = 1000
    equipos = Queue()
    nombres = ["Rusia", "Araia Saudi", "Egipto", "Uruguay",
            "Portugal", "Espana", "Marruecos", "Iran",
            "Francia", "Australia", "Peru", "Dinamarca",
            "Argentina", "Islandia", "Croacia", "Nigeria",
            "Brasil", "Suiza", "Costa Rica", "Serbia",
            "Alemania", "Mexico", "Suecia", "Corea",
            "Belgica", "Panama", "Tunez", "Inglaterra",
            "Polonia", "Senegal", "Colombia", "Japon"]
    media = [55, 130, 120, 57,
            55, 58, 98, 154,
            50, 106, 71, 53,
            53, 90, 69, 90,
            42, 66, 79, 61,
            43, 84, 56, 90,
            71, 90, 135, 71,
            63, 64, 62, 109]
    penal = []
    grupos = []

    for x in range(len(nombres)):
        penal.append(round(random()))

    for n, m, p in zip(nombres, media, penal):
        equipos.put(Equipo(n, m, p))

    while(equipos.empty() == False):
        e1 = equipos.get()
        e2 = equipos.get()
        e3 = equipos.get()
        e4 = equipos.get()
        # print("%s - %s - %s - %s" % (e1.getPais(), e2.getPais(), e3.getPais(), e4.getPais()))
        grupos.append(Division(e1, e2, e3, e4))

    campeones = []

    for sim in range(simulations):
        winners = []
        runners = []

        octavos = []
        cuartos = []
        semis = []

        for grupo in grupos:
            grupo.match()
            grupo.play()
            grupo.winner()
            grupo.runner()
            winners.append(grupo.get1())
            runners.append(grupo.get2())

        shuffle(winners)
        shuffle(runners)

        for w, r in zip(winners, runners):
            p = Partido(w, r)
            p.tiempoPartido()
            octavos.append(p.getGanador())

        for i in range(len(octavos)):
            if(i % 2 == 0):
                p = Partido(octavos[i], octavos[i+1])
                p.tiempoPartido()
                cuartos.append(p.getGanador())
            else:
                continue

        for i in range(len(cuartos)):
            if(i % 2 == 0):
                p = Partido(cuartos[i], cuartos[i+1])
                p.tiempoPartido()
                semis.append(p.getGanador())
            else:
                continue

        final = Partido(semis[0], semis[1])
        final.tiempoPartido()
        campeones.append(final.getGanador().getPais())
    print("En %i simulaciones, el ganador mas frecuente fue: %s" % (simulations, max(set(campeones), key=campeones.count)))

if __name__ == '__main__':
    main()
