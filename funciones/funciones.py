import random


def seleccionPersonaje():
    numeroAleatorio = random.randint(1, 2)
    if numeroAleatorio == 2:
        numeroAleatorio = -1
    return numeroAleatorio


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


"""Cheque el numero clickeado"""


def guardar(fila, col):
    a = 3 * fila + col
    return a


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


def eleccionMovimiento(list):
    a = random.randint(0, 8)
    while a in list:
        a = random.randint(0, 8)
    list.append(a)
    fila = a // 3
    col = a - 3 * fila
    return fila, col


def inteligenciaArtificial(list):
    b = random.choice(list)
    checkNum(b, list)
    return b


def checkGanar(list, turno):
    if len(list) >= 3:
        ganar = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combinacion in ganar:
            similitud = all(elem in list for elem in combinacion)

            if similitud:
                return True, turno
            else:
                if turno == "Jugador":

                    return False, "IA"
                else:
                    return False, "Jugador"

    else:
        if turno == "Jugador":

            return False, "IA"
        else:
            return False, "Jugador"


if __name__ == "__main__":
    print(seleccionPersonaje())
