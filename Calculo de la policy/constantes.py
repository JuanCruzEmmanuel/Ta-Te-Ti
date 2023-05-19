#se definen las recomenzas para implementarlas en el Q learning

recompenzas = dict(Ganar=10, Perder=-10, Empate=4)

#parametros del Q learning

learning_rate = 0.1
discount_factor = 0.9
n_iter = 1000
