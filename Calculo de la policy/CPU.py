import numpy as np
import pickle


class cpu:
    def __init__(self, nombre, exp_rate=0.3):
        self.nombre = nombre
        self.exp_rate = exp_rate
        self.discount_factor = 0.85 # me importa mucho el valor siguiente
        self.lr = 0.2
        self.state = []
        self.state_values = {}

    def getHash(self, tablero):
        """

        :param tablero tipe: objet
        :return:
        """
        hash = str(tablero.reshape(3*3))
        return hash

    def elegirAccion(self, posiciones, tablero, simbolo):

        if np.random.uniform(0,1)<= self.exp_rate:
            indicePos = np.random.choice(len(posiciones))
            accion = posiciones[indicePos]

        else:

            maxValue = -999 # valor inicial para explorar y no me genere conflicto

            for pos in posiciones:
                nextTablero = tablero.copy()
                nextTablero[pos] = simbolo
                nextHash = self.getHash(nextTablero)
                # voy viendo el valor que tengo en el diccionario valores estado para elegir la mejor
                valor = 0 if self.state_values.get(nextHash) is None else self.state_values.get(nextHash)
                if valor >maxValue:
                    maxValue =valor
                    accion = pos

        return accion

    def addState(self,state):

        self.state.append(state)

    def feedRecompensa(self, recompensa):
        #como la recompensa tiene que agregarse a varios stados, debo realizar una iteracion de estos
        for st in reversed(self.state):
            if self.state_values.get(st) is None:
                self.state_values[st] = 0
            self.state_values[st] += self.lr*(self.discount_factor*recompensa-self.state_values[st])
            recompensa = self.state_values[st]
    def reset(self):

        self.state = []

    def savePolicy(self):
        fw = open('policy_' + str(self.nombre), 'wb')
        pickle.dump(self.state_values, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.state_values = pickle.load(fr)
        fr.close()






if __name__ =="__main__":

    p = cpu(nombre="p1")


