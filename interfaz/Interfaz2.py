import pygame, pygame.mixer

WIDTH = 600
HEIGHT = 600
FILAS = 3
COLUMNAS = 3
TamanCuadrado = int(WIDTH // 3)
GrosorLinea = 15
GrosorCirculo = 16
GrosorCruz = 25
Radio = 55
Separacion = 50
# Definimos los colores que usaremos en el juego

ColorFondo = (28, 170, 156)
ColorLinea = (23, 145, 135)
ColorCirculo = (239, 231, 200)
ColorCruz = (66, 66, 66)
#pygame.mixer.init()
#sonBurbujas = pygame.mixer.Sound("C:/Users/juanc/Desktop/proyectos/ta-te-ti/efecto/sonido/burbujas.mp3")

class TaTeTi:

    def __init__(self):
        self.pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Ta-Te-Ti")
        self.tablero = [[0 for x in range(FILAS)] for y in range(COLUMNAS)]
        self.game_over = False

    def dibujarTablero(self):
        # Lineas horizontales
        pygame.draw.line(self.pantalla, ColorLinea, (
            0, TamanCuadrado), (WIDTH, TamanCuadrado), GrosorLinea)
        pygame.draw.line(self.pantalla, ColorLinea, (
            0, 2 * TamanCuadrado), (WIDTH, 2 * TamanCuadrado), GrosorLinea)
        # Lineas Verticales
        pygame.draw.line(self.pantalla, ColorLinea, (
            TamanCuadrado, 0), (TamanCuadrado, HEIGHT), GrosorLinea)
        pygame.draw.line(self.pantalla, ColorLinea, (
            2 * TamanCuadrado, 0), (2 * TamanCuadrado, HEIGHT), GrosorLinea)

    def circulo(self, fila, col):
        pygame.draw.circle(self.pantalla, ColorCirculo,
                           (int(col * TamanCuadrado + TamanCuadrado // 2),
                            int(fila * TamanCuadrado + TamanCuadrado // 2)),
                           Radio, GrosorLinea)

    def cruz(self, fila, col):
        pygame.draw.line(self.pantalla, ColorCruz,
                         (col * TamanCuadrado + Separacion, fila * TamanCuadrado + Separacion),
                         (col * TamanCuadrado + TamanCuadrado - Separacion, fila * TamanCuadrado + TamanCuadrado -
                          Separacion), GrosorCruz)
        pygame.draw.line(self.pantalla, ColorCruz,
                         (col * TamanCuadrado + Separacion, fila * TamanCuadrado + TamanCuadrado - Separacion),
                         (col * TamanCuadrado + TamanCuadrado - Separacion, fila * TamanCuadrado + Separacion),
                         GrosorCruz)

    def comprobarVacio(self, fila, col):
        return self.tablero[fila][col] == 0

    def marca(self, fila, col, participante):
        self.tablero[fila][col] = participante

    def dibujarFigura(self):
        for fila in range(FILAS):
            for col in range(COLUMNAS):
                if self.tablero[fila][col] == 1:
                    #sonBurbujas.play()
                    self.circulo(fila, col)
                elif self.tablero[fila][col] == 2:
                    self.cruz(fila, col)


    def tableroCompleto(self):

        for fila in range(FILAS):
            for col in range(COLUMNAS):
                if self.tablero[fila][col] == 0:
                    return False

        return True

    def dibujarLineaVictoria(self, inicio, final):

        pygame.draw.line(self.pantalla, ColorLinea, inicio, final, GrosorLinea)
        pygame.display.update()


    def checkVictoria(self, participante):
        # Check horizontal

        for fila in range(FILAS):
            if self.tablero[fila][0] == participante and self.tablero[fila][1] == participante and self.tablero[fila][2] == participante:
                self.dibujarLineaVictoria((0, fila*TamanCuadrado+TamanCuadrado//2), (WIDTH, fila*TamanCuadrado+TamanCuadrado//2))
                return True

        # Check vertical

        for col in range(COLUMNAS):
            if self.tablero[0][col] == participante and self.tablero[1][col] == participante and self.tablero[2][col] == participante:
                self.dibujarLineaVictoria((col*TamanCuadrado + TamanCuadrado//2, 0), (col * TamanCuadrado + TamanCuadrado//2, HEIGHT))
                return True

        #CHECK DIAGONAL PRINCIPAL

        if self.tablero[0][0] == participante and self.tablero[1][1] == participante and self.tablero[2][2] == participante:
            self.dibujarLineaVictoria((0, 0), (WIDTH, HEIGHT))
            return True

        if self.tablero[2][0] == participante and self.tablero[1][1] == participante and self.tablero[0][2] == participante:
            self.dibujarLineaVictoria((0, HEIGHT), (WIDTH, 0))
            return True

        return False

    def dibujar(self):
        self.pantalla.fill(ColorFondo)
        self.dibujarTablero()
        self.dibujarFigura()


    def reinicio(self):

        self.tablero = [[0 for x in range(FILAS)] for y in range(COLUMNAS)]
        self.game_over = False







