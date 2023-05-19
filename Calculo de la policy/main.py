from State import state
from CPU import cpu

if __name__ == "__main__":


    p1 = cpu("p1")
    p2 = cpu("p2")

    st = state(p1,p2)
    print("se inicia el entrenamiento")
    st.entrenar(rondas=5000)
    print("se finalizo el entrenamiento de 1000")

    p1.savePolicy()
    print(p1.state_values)
