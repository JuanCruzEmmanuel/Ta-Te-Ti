import random


def seleccionPersonaje():
    numeroAleatorio = random.randint(0, 100)
    if numeroAleatorio % 2 == 0:
        return "Jugador"
    else:
        return "AI"


"""Con esto me aseguro de elegir correctamente la fila"""


def definirNum(num):
    if num <= 2:
        fila = 0
        columna = num
        return fila, columna
    elif 3 <= num <= 5:
        fila = 1
        columna = num - 3
        return fila, columna
    else:
        fila = 2
        columna = num - 6
        return fila, columna


"""creo y muestro el tablero"""


class Tablero:

    def __init__(self):
        self.filas = 3
        self.columnas = 3
        self.celdas = [["-"] * self.columnas for _ in range(self.filas)]

    def mostrar(self):
        for fila in self.celdas:
            print("|".join(str(celda) for celda in fila))

    def update(self, fila, columna, valor):
        self.celdas[fila][columna] = valor


"""chequeo que los numeros que elijo aun se pueden obtener"""


def checkNum(num, list):
    correcto = False
    while not correcto:
        if num > 8:
            num = int(input("Ingrese un numero correcto: "))
            correcto = False
        else:
            if num in list:

                correcto = True
            else:
                num = int(input("Ingrese un numero correcto: "))
                correcto = False
    list.remove(num)





def crearPosiciones():
    lista = [x for x in range(9)]
    return lista


if __name__ == "__main__":
    print("Jugar al tateti \nlas posiciones son: \n     0|1|2 \n     3|4|5\n     6|7|8")
    pos = crearPosiciones()
    a = int(input("ingrese un valor: "))
    checkNum(a, pos)
    definirNum(a)
