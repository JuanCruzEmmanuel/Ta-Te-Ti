import numpy as np
import random

class state:
    def __init__(self, p1, p2):
        self.tablero = np.zeros((3, 3))
        self.game_over = False
        self.tamano_tablero = 3
        self.p1 = p1
        self.p2 = p2
        self.simbolo = 1
        self.boardHash = None

    def getHash(self):
        self.boardHash = str(self.tablero.reshape(3*3)) #esto me va a devolver el hash de la matriz, se reinicia en cada fin de juego
        return self.boardHash
    def reinicio(self):
        self.tablero = np.zeros((3, 3))
        self.game_over = False
        self.boardHash = None
        self.simbolo = random.choice([1,-1])

    def victoria(self):

        #check filas
        for i in range(3):
            if sum(self.tablero[i,:]) == 3:
                self.game_over = True
                return 1
            elif sum(self.tablero[:,i]) ==-3:
                self.game_over = True
                return -1
        #check columnas
        for j in range(3):
            if sum(self.tablero[:,j]) ==3:
                self.game_over = True
                return 1
            elif sum(self.tablero[:,j])==-3:
                self.game_over = True
                return -1
        #check diagonales

        diagonalP = sum([self.tablero[i, i] for i in range(3)])
        diagonalO = sum([self.tablero[i, 3-i-1] for i in range(3)])
        diagonal = max(abs(diagonalP),abs(diagonalO))
        if diagonal == 3:
            self.game_over = True
            if diagonalP == 3 or diagonalO == 3:
                return 1
            else:
                return -1

        if len(self.posicionesDisponibles()) == 0:
            self.game_over = True
            return 0

        self.game_over = False
        return None

    def posicionesDisponibles(self):
        posiciones = []
        for i in range(3): #posicion en x (filas)
            for j in range(3): #posicion en y(columnas)
                if self.tablero[i][j] == 0:
                    posiciones.append((i,j)) #esto me devuelve las posiciones x,y disponibles en la matriz. Es una tuple
        return posiciones

    def actualizarState(self, posiciones, simbolo):
        self.tablero[posiciones] = simbolo # Actualizo el state (en este caso el tablero)
        self.simbolo = -1 if self.simbolo == 1 else 1 #Cambio el simbolo

    def recompensar(self):
        resultado = self.victoria()
        if resultado == 1:
            self.p1.feedRecompensa(1)
            self.p2.feedRecompensa(0)
        elif resultado == -1:
            self.p1.feedRecompensa(0)
            self.p2.feedRecompensa(1)
        else:
            self.p1.feedRecompensa(0)
            self.p2.feedRecompensa(0.5)

    def entrenar(self, rondas=1000):

        for episodio in range(rondas):

            while not self.game_over:
                #jugador 1
                posiciones = self.posicionesDisponibles()  # me devuelve una tupla con todas las posiciones
                accion1 = self.p1.elegirAccion(posiciones=posiciones,tablero=self.tablero, simbolo = self.simbolo)

                self.actualizarState(posiciones = accion1,simbolo=self.simbolo)

                hash = self.getHash()

                self.p1.addState(hash)

                vict = self.victoria()

                if vict is not None:
                    self.recompensar()
                    self.p1.reset()
                    self.p2.reset()
                    self.reinicio()
                    break

                posiciones = self.posicionesDisponibles()  # me devuelve una tupla con todas las posiciones
                accion2 = self.p2.elegirAccion(posiciones=posiciones,tablero=self.tablero, simbolo = self.simbolo)

                self.actualizarState(posiciones=accion2, simbolo=self.simbolo)

                hash = self.getHash()

                self.p2.addState(hash)

                vict = self.victoria()

                if vict is not None:
                    self.recompensar()
                    self.p1.reset()
                    self.p2.reset()
                    self.reinicio()
                    break


if __name__ == "__main__":

    pass