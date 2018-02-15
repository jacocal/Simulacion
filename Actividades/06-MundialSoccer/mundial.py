import numpy as np
from math import *

class Equipo:
    pais = None
    media_gol = 0
    penal = 0
    nextGol = 0
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

    def setNextGol(self, gol):
        self.nextGol += gol

    def setGol(self, gol):
        self.nextGol = gol

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
        return goles90

    def getGoles30(self):
        return goles30

    def getPenales(self):
        return exitosPen

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
                    win = False
                    while(win == False):
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
                            win = True
                        elif(sum(penal2) > sum(penal1)):
                            self.setGanador(self.equipo2)
                            win = True
                        else:
                            continue
                self.exitosPen[0] = sum(penal1)/len(penal1)
                self.exitosPen[1] = sum(penal2)/len(penal2)
        self.restartGol()

class Division:
    nombre = None
    equipo1 = None
    equipo2 = None
    equipo3 = None
    equipo4 = None

    def __init__(self, nom, e1, e2, e3, e4):
        self.nombre = nom
        self.equipo1 = e1
        self.equipo2 = e2
        self.equipo3 = e3
        self.equipo4 = e4

def main():
    simulations = 5000
    equipos = []
    ganadores = []
    equipos.append(Equipo("Alemania", 48, .58))
    equipos.append(Equipo("Portugal", 53, .4))
    equipos.append(Equipo("Argentina", 50, .55))
    equipos.append(Equipo("Brasil", 48, .5))

    for x in range(simulations):

        partidos = np.random.choice(
            equipos,
            len(equipos),
            replace=False
        )

        semi1 = Partido(partidos[0], partidos[1])
        semi1.tiempoPartido()

        semi2 = Partido(partidos[2], partidos[3])
        semi2.tiempoPartido()

        final = Partido(semi1.getGanador(), semi2.getGanador())
        final.tiempoPartido()

        ganadores.append(final.getGanador().getPais())

    # print("Semi1: %s\nSemi2: %s\nFinal: %s" % (semi1.getGanador().getPais(), semi2.getGanador().getPais(), final.getGanador().getPais()))

    print("En %i simulaciones, el ganador mas frecuente fue: %s" % (simulations, max(set(ganadores), key=ganadores.count)))

if __name__ == '__main__':
    main()
