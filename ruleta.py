import random
import matplotlib.pyplot as plt
import numpy as np
num_corridas = int(input("Ingrese corridas: "))
num_valores = int(input("Ingrese tiradas: "))
num_elegido = int(input("Número a elegir: "))

def tirar_ruleta():
    return random.randint(0, 36)

# Lista para almacenar los resultados de las corridas
resultados_corridas = []
num_ruleta=np.arange(37)
promedio_esperado= np.mean(num_ruleta)
varianza_esperada = np.var(num_ruleta)
desvio_esperado = np.std(num_ruleta)


# Realizar  corridas
for i in range(num_corridas):
    frec_absol_elegido = []
   
    resultados_corrida = []
    vpn=[]
    # Realizar  tiradas en la corrida actual
    for j in range(num_valores):
        resultado = tirar_ruleta()
        resultados_corrida.append(resultado)
        if resultado == num_elegido:
          frec_absol_elegido.append(1)
        else:
           frec_absol_elegido.append(0)
        vpn.append(np.mean(resultados_corrida[:j+1]))      
    # Agregar los resultados de la corrida actual a la lista de resultados de corridas
    
    frec_relativa = [sum(frec_absol_elegido[:i+1]) / (i+1) for i in range(num_valores)]
    #### GRAFICOS ##########
    plt.plot(range(1, num_valores + 1), frec_relativa, label='Frecuencia Relativa', color='red')

    plt.axhline(y=1/37, color='blue', linestyle='--')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.title(f'Frecuencia Relativa del número {num_elegido} en {num_valores} tiradas')
    plt.legend()
    plt.show()
    
    
    plt.plot(range(1, num_valores + 1), vpn, label='Promedio', color='red')
    plt.axhline(y=promedio_esperado, color='blue', linestyle='--')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Promedio de las Tiradas')
    plt.title(f'Promedio de los numeros en {num_valores} tiradas')
    plt.legend()
    plt.show()