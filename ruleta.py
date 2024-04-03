import random
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
num_corridas = int(argv[1])
num_valores = int(argv[2])
num_elegido = int(argv[3])

def tirar_ruleta():
    return random.randint(0, 36)

# Realizar  corridas

for i in range(num_corridas):
   
    resultado_num_elegido= np.zeros(num_valores)
    resultados_corrida = []
    vpn=[]
    desvio_estandar=[]
    varianza=[]
    suma_resultado=0
    desvio_estandar=np.zeros(num_valores)
    varianza=np.zeros(num_valores)
    
    # Realizar  tiradas en la corrida actual
    
    for j in range(num_valores):
        resultado = tirar_ruleta()
        resultados_corrida.append(resultado)
        suma_resultado+=resultado
        if resultado == num_elegido:    
          resultado_num_elegido[j]=1
            
         ### CALCULOS ### 
        vpn.append(np.mean(resultados_corrida[:j+1]))
        desvio_estandar[j]=np.std(resultados_corrida[:j+1])   
        varianza[j]=np.var(resultados_corrida[:j+1])
        
    frec_relativa = [sum(resultado_num_elegido[:i+1]) / (i+1) for i in range(num_valores)]

    promedio_estimado=suma_resultado/num_valores
    
    desvio_estimado=np.std(resultados_corrida)
    
    varianza_estimada=np.var(resultados_corrida)
    
    
    ####### GRAFICOS ##########
    
    #######GRAFICA FRECUENCIA RELATIVA########
    plt.plot(range(1, num_valores + 1), frec_relativa, label='Frecuencia Relativa', color='red')
    plt.axhline(y=1/37, color='blue', linestyle='--')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.title(f'Frecuencia Relativa del número {num_elegido} en {num_valores} tiradas')
    plt.legend()
    plt.savefig("grafica_frecuencia_relativa.png")
    plt.show()

    ########GRAFICA PROMEDIO ##########
    plt.plot(range(1, num_valores + 1), vpn, label='Promedio', color='red')
    plt.axhline(y=promedio_estimado, color='blue', linestyle='--')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Promedio de las Tiradas')
    plt.title(f'Promedio de los numeros en {num_valores} tiradas')
    plt.legend()
    plt.savefig("grafica_promedio.png")
    plt.show()
    
    ########GRAFICA DESVÍO ESTANDAR#######
    plt.plot(range(1, num_valores + 1),desvio_estandar ,label='Desvío Estandar', color='red')
    plt.axhline( y=desvio_estimado,color='blue', linestyle='--')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Desvío Estandar')
    plt.title(f'Desvío estandar en {num_valores} tiradas')
    plt.legend()
    plt.savefig("grafica_desvio_estandar.png")
    plt.show()

    #########GRAFICA VARIANZA##########
    plt.plot(range(1, num_valores + 1),varianza ,label='Varianza', color='red')
    plt.axhline(y=varianza_estimada ,color='blue', linestyle='--')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Varianza')
    plt.title(f'Varianza en {num_valores} tiradas')
    plt.legend()
    plt.savefig("grafica_varianza.png")
    plt.show()