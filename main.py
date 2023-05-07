import sys

sys.path.append("C:/Users/juanc/Desktop/proyectos/ta-te-ti/funciones")
sys.path.append("C:/Users/juanc/Desktop/proyectos/ta-te-ti/interfaz")
sys.path.append("C:/Users/juanc/Desktop/proyectos/ta-te-ti/efecto/sonido")


import funciones, Interfaz2, pygame, pygame.mixer

pygame.init()

juego = Interfaz2.TaTeTi()
participante = funciones.seleccionPersonaje()
colect = list()
if __name__ == '__main__':

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            elif participante == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and not juego.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    filaCliqueada = int(mouseY // Interfaz2.TamanCuadrado)
                    colCliqueada = int(mouseX // Interfaz2.TamanCuadrado)
                    colect.append(funciones.guardar(filaCliqueada, colCliqueada))
                    if juego.comprobarVacio(filaCliqueada, colCliqueada):
                        juego.marca(filaCliqueada, colCliqueada, participante)
                        if juego.checkVictoria(participante):
                            juego.game_over = True
                        elif juego.tableroCompleto():
                            juego.game_over = True
                        else:
                            participante = participante % 2 + 1
            elif participante == 2:
                filaCliqueada, colCliqueada = funciones.eleccionMovimiento(colect)
                juego.marca(filaCliqueada, colCliqueada, participante)
                if juego.checkVictoria(participante):
                    juego.game_over = True
                elif juego.tableroCompleto():
                    juego.game_over = True
                else:
                    participante = participante % 2 + 1

            juego.dibujar()

            if juego.game_over:
                pygame.time.wait(1000)
                juego.reinicio()
                colect = list()
                participante = funciones.seleccionPersonaje()
            pygame.display.update()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
