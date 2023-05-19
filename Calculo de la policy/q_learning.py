from constantes import learning_rate, discount_factor
import numpy as np


def get_state(tabla):  # aca va a recibir la tabla en forma de 1x9 es decir el tabla.estado_espacio_
    return tuple(tabla)  # lo convierte en forma de tupla, ya que este no se puede modificar


def actualizar_q_valor(q_matrix, state, action, reward, next_state):
    max_q_next = np.max(q_matrix[next_state])
    q_matrix[state][action] += learning_rate * (
            reward + discount_factor * max_q_next - q_matrix[state, action]
    )