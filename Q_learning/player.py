"""voy a crear una clase player para que interactue con el entorno, este pueda cargar nuevas iteraccion"""
import numpy as np

class Player:

    def __init__(self, nombre, exp_rate):

        self.nombre = nombre
        self.exp_rate = exp_rate
        self.state = []
        self.discount_factor = 0.85
        self.lr = 0.2
        self.state_values = {}

    def getHash(self, tablero): #es importante tener el hash para despues poder leer los valores
        hash = str(tablero.reshape(3*3))
        return hash

    def eleccionMovimiento(self, posicion,tablero, simbolo):

        if np.random.uniform(0,1) <= self.exp_rate: #esta linea es por el caso si se entrena el agente, va elegir aleatoriamente entre las opciones disponibles
            idx = np.random.choice(len(posicion)) # la posicion es una lista con una serie de tuplas
            accion = posicion[idx] # al elegir el indice de la lista de tuplas, y luego los valores de la tupla
        else:
            maxValue = -999

            for pos in posicion:
                tableroFuturo = tablero.copy()
                tableroFuturo[pos] = simbolo
                nextHashTablero = self.getHash(tableroFuturo)
                # el valor sera 0 en caso que no haya ningun valor, sino, el value vale lo que me diga el diccionario para ese hash
                value = 0 if self.state_values.get(nextHashTablero) is None else self.state_values.get(nextHashTablero)
                if value > maxValue: #esto me garantiza elegir siempre la opcion con mayor valor del diccionario
                    maxValue = value
                    accion = pos
        return accion



