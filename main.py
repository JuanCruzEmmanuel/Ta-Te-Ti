import os,sys

sys.path.append("Q_learning")
sys.path.append("funciones")
sys.path.append("interfaz")
sys.path.append("sonido")


import funciones, pygame
from Q_learning import player
from interfaz import Interfaz2

pygame.init()

juego = Interfaz2.TaTeTi()
#participante = funciones.seleccionPersonaje()
#Creo el objeto cpu que se encarga de elegir la mejor jugada en cada momento. En este caso el agente esta entrenado, por eso cargo la "policy"
CPU = player.Player("CPU", exp_rate=0)
CPU.loadPolicy("policy_p1")
participante = 1 #en este caso, empieza siempre la maquina
if __name__ == '__main__':

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif participante == -1:
                if event.type == pygame.MOUSEBUTTONDOWN and not juego.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    filaCliqueada = int(mouseY // Interfaz2.TamanCuadrado) #convierto el valor entre 0 y 2
                    colCliqueada = int(mouseX // Interfaz2.TamanCuadrado) #converierto el valor entre 0 y 2
                    posicion = tuple([filaCliqueada, colCliqueada])
                    if juego.comprobarVacio(posicion):
                        juego.marca(posicion, participante)
                        if juego.checkVictoria(participante):
                            juego.game_over = True
                        elif juego.tableroCompleto():
                            juego.game_over = True
                        else:
                            participante = -1 if participante == 1 else 1 #cambio de jugador
            elif participante == 1:
                posicionDisponibles = juego.posicionesDisponibles() #obtengo las posiciones del tablero que son 0
                hash = juego.getHash() #me devuelve el hash en forma de dic para yo poder trabajar sobre esto
                posicion = CPU.eleccionMovimiento(posicionDisponibles,juego.tablero, participante)
                CPU.addState(posicion)
                juego.marca(posicion, participante)
                if juego.checkVictoria(participante):
                    juego.game_over = True
                elif juego.tableroCompleto():
                    juego.game_over = True
                else:
                    participante = -1 if participante == 1 else 1

            juego.dibujar()

            if juego.game_over:
                pygame.time.wait(1000)
                juego.reinicio()
                CPU.reset()
                participante = funciones.seleccionPersonaje()
            pygame.display.update()




