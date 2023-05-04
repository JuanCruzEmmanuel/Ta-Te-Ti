import sys

sys.path.append("C:/Users/juanc/Desktop/proyectos/ta-te-ti/funciones")

import funciones

if __name__ == '__main__':

    finalizo = False
    valusuriao = list()
    valIA = list()
    print("Jugar al tateti \nlas posiciones son: \n     0|1|2 \n     3|4|5\n     6|7|8")
    pos = funciones.crearPosiciones()
    tablero = funciones.Tablero()
    turno = funciones.seleccionPersonaje()
    while not finalizo:
        if turno == "Jugador":
            a = int(input("seleccione una posicion: "))
            funciones.checkNum(a, pos)
            valusuriao.append(a)
            fila, columna = funciones.definirNum(a)
            tablero.update(fila, columna, "X")
            tablero.mostrar()
            finalizo, turno = funciones.checkGanar(valusuriao, turno)
        else:
            b = funciones.inteligenciaArtificial(pos)
            valIA.append(b)
            fila, columna = funciones.definirNum(b)
            tablero.update(fila, columna, "O")
            tablero.mostrar()
            finalizo, turno = funciones.checkGanar(valIA, turno)

    print("Felicidades has ganado", turno)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
