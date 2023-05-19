"""Imagine yourself in a treasure hunt in a maze . The game is as follows :
    From any state you can go left, right, up or down or stay in the same place provided you don’t cross the premises
    of the maze. Each action will take you to a cell of the grid (a different state). Now, there is a treasure chest at
    one of the states (the goal state). Also, the maze has a pit of snakes in certain positions/states. Your goal is to
    travel from the starting state to the goal state by following a path that doesn’t have snakes in it.
"""

""" vamos a trabajar con una grilla 2x2 con una posicion inicial de (0,0) y el tesoro en (1,1)"""

import random
import numpy as np

factor_descuento = 0.8
espacio_accion = [0, 1, 2, 3, 4]  # representa up,down,right,left, not move
espacio_estado = [x for x in range(4)]
n_iter = 10000
Q = np.zeros((len(espacio_estado), len(espacio_accion)))
# recompensas por el movimiento de un estado a otro
recompensas = np.array([[0, -10, 0, -1, -1],
                        [0, 10, -1, 0, -1],
                        [-1, 0, 0, 10, -1],
                        [-1, 0, -10, 0, 10]])
# me indica a que estado voy
transicion = np.array([[-1, 2, -1, 1, 0],
                       [-1, 3, 0, -1, 1],
                       [0, -1, -1, 3, 2],
                       [1, -1, 2, -1, 3]])
# inidica las acciones
mov_validos = np.array([[1, 3, 4],
                        [1, 2, 4],
                        [0, 3, 4],
                        [0, 2, 4]])

for episodio in range(n_iter):
    start_state = 0
    state = start_state
    while state != 3:
        action = random.choice(mov_validos[state])
        next_state = transicion[state][action]
        future_reward = []

        for action_next in mov_validos[next_state]:
            future_reward.append(Q[next_state][action_next]) #me gusta esta solucion para encontrar el punto optimo futuro
        Q_state = Q[state][action] + 0.2 * (recompensas[state][action] + factor_descuento * max(future_reward) -Q[state][action])
        Q[state][action] = Q_state
        state = next_state
        if state == 3:
            break
print("final")
print(Q)
