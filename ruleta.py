import random
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
num_corridas = int(argv[1])
cant_tiradas = int(argv[2])
num_elegido = int(argv[3])

def tirar_ruleta():
    return random.randint(0, 36)

# Realizar  corridas
frecuencia_relativa_corridas=[]
promedio_corridas=[]
desvio_estandar_corridas=[]
varianza_corridas=[]
for i in range(num_corridas):
    resultado_num_elegido= np.zeros(cant_tiradas)
    resultados_corrida = []
    vpn=[]
    desvio_estandar=[]
    varianza=[]
    suma_resultado=0
    desvio_estandar=np.zeros(cant_tiradas)
    varianza=np.zeros(cant_tiradas)
    
    # Realizar  tiradas en la corrida actual
    
    for j in range(cant_tiradas):
        resultado = tirar_ruleta()
        resultados_corrida.append(resultado)
        suma_resultado+=resultado
        if resultado == num_elegido:    
           resultado_num_elegido[j]=1
            
         ### CALCULOS ### 
        vpn.append(np.mean(resultados_corrida[:j+1]))
        desvio_estandar[j]=np.std(resultados_corrida[:j+1])   
        varianza[j]=np.var(resultados_corrida[:j+1])
        
    frec_relativa = [sum(resultado_num_elegido[:i+1]) / (i+1) for i in range(cant_tiradas)]
    frecuencia_relativa_corridas.append(frec_relativa)
    promedio_estimado=suma_resultado/cant_tiradas
    promedio_corridas.append(vpn)
    desvio_estimado=np.std(resultados_corrida)
    varianza_estimada=np.var(resultados_corrida)
    desvio_estandar_corridas.append(desvio_estandar)
    varianza_corridas.append(varianza)
    
    ####### GRAFICOS ##########
    
    #######GRAFICA FRECUENCIA RELATIVA########
for i, frecuencia_relativa_corrida in enumerate(frecuencia_relativa_corridas):
    plt.plot(frecuencia_relativa_corrida, label=f'Corrida {i+1}')
plt.axhline(y=1/37, color='red', linestyle='--')
plt.xlabel('Número de tiradas')
plt.ylabel('Frecuencia Relativa')
plt.title(f'Frecuencia Relativa del número {num_elegido} en {cant_tiradas} tiradas')
plt.legend()
plt.ylim(0,0.07)
plt.savefig("grafica_frecuencia_relativa.png")
plt.show()


    ########GRAFICA PROMEDIO ##########
for i, promedio_corridas in enumerate(promedio_corridas):
    plt.plot( promedio_corridas, label=f'Corrida {i+1}')
plt.axhline(y=promedio_estimado, color='red', linestyle='--')
plt.xlabel('Número de tiradas')
plt.ylabel('Promedio de las Tiradas')
plt.title(f'Promedio de los numeros en {cant_tiradas} tiradas')
plt.legend()
plt.ylim(10,30)
plt.savefig("grafica_promedio.png")
plt.show()

    ########GRAFICA DESVÍO ESTANDAR#######
for i, desvio_estandar_corridas in enumerate(desvio_estandar_corridas):
    plt.plot(desvio_estandar_corridas, label=f'Corrida {i+1}')
plt.axhline( y=desvio_estimado, color='red', linestyle='--')
plt.xlabel('Número de tiradas')
plt.ylabel('Desvío Estandar')
plt.title(f'Desvío estandar en {cant_tiradas} tiradas')
plt.legend()
plt.ylim(5,15)
plt.savefig("grafica_desvio_estandar.png")
plt.show()

    #########GRAFICA VARIANZA##########
for i, varianza_corridas in enumerate(varianza_corridas):
    plt.plot(varianza_corridas, label=f'Corrida {i+1}')
plt.axhline(y=varianza_estimada, color='red', linestyle='--')
plt.xlabel('Número de tiradas')
plt.ylabel('Varianza')
plt.title(f'Varianza en {cant_tiradas} tiradas')
plt.legend()
plt.ylim(70,130)
plt.savefig("grafica_varianza.png")
plt.show()