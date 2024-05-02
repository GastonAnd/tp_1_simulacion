import random
import matplotlib.pyplot as plt
import numpy as np
import sys

args = sys.argv[1:]

if len(args) != 6 or args[0] != '-c' or args[2] != '-n' or args[4] != '-e' :
    print("Uso: python script.py -c <corridas> -t <tiradas> -n <numero>")
    sys.exit(1)

num_corridas = int(args[1])
cant_tiradas = int(args[3])
num_elegido = int(args[5])
monto_inicial=500
apuesta_gral=2
def tirar_ruleta():
    return random.randint(0, 36)

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
frecuencia=[]

def martingala():
    ganancia=0
    monto=monto_inicial
    apuesta=apuesta_gral
    contador_tirada=0
    for i in range(cant_tiradas):
        resultado=tirar_ruleta()
        contador_tirada+=1
        if resultado in rojos:
            monto+=apuesta * 2
            ganancia += apuesta *2           
            apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
            print("salio rojo en la tirada:",i+1,",ganancia-->" ,ganancia)
            print("monto acumulado-->",monto)
            print("La frecuencia esta en ",contador_tirada)
        else:
            apuesta *=2
            print("salio negro")
            print("apuesta doble",apuesta)
            if monto < apuesta:
                print("quedaste seco",i)
                break
            else:
                monto -=apuesta
                
    print("Frecuencia",frecuencia)

for i in range(num_corridas):
    martingala()
    valores_unicos, frecuencia_relativa=np.unique(frecuencia,return_counts=True)        
    plt.bar(valores_unicos, frecuencia_relativa, color='blue')
    plt.xlabel('Tiradas desde la última ganancia')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de tiradas desde la última ganancia')
    plt.show()