import random
import matplotlib.pyplot as plt
import numpy as np
import sys
args = sys.argv[1:]

if len(args) !=8 or args[0] != '-c' or args[2] != '-n' or args[4] != '-a' or args[6] !='-m' :
    print("Uso: python script.py -c <corridas> -n <tiradas> -e <numero>")
    sys.exit(1)

num_corridas = int(args[1])
cant_tiradas = int(args[3])
capital = (args[5])
estrategia=(args[7])

monto_inicial=5000
apuesta_gral=150
def tirar_ruleta():
    return random.randint(0, 36)
def seq_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
frecuencia=[]
montoTotal=[]
def martingala():
    ganancia=0
    monto=monto_inicial
    apuesta=apuesta_gral
    contador_tirada=0
    for i in range(1,cant_tiradas+1):
        resultado=tirar_ruleta()
        contador_tirada+=1
        if resultado in rojos:
            monto+=apuesta * 2
            ganancia += apuesta *2           
            apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
            montoTotal.append(monto)
            print("salio rojo en la tirada:",i+1,",ganancia-->" ,ganancia)
            print("monto acumulado-->",monto)
            print("La frecuencia esta en ",contador_tirada)
        else:
            apuesta *=2
            print("salio negro")
            print("apuesta doble",apuesta)
            monto -=apuesta
            montoTotal.append(monto)            
            if monto < apuesta:
                print("quedaste seco",i)
                break
    print(montoTotal)

def fibonacci():
    monto = monto_inicial
    apuesta = apuesta_gral
    fib_sequence = seq_fibonacci(cant_tiradas)
    tiradas_realizadas = 0
    fib_index=0
    contador_tirada=0
    for _ in range(1,cant_tiradas+1):
        resultado = tirar_ruleta()
        tiradas_realizadas += 1
        contador_tirada+=1
        if resultado in rojos :
            monto += apuesta * 2
            print("Salio rojo en la tirada:", tiradas_realizadas)
            print("Monto acumulado-->", monto)
            fib_index = max(0, fib_index - 2)  # Retrocede dos pasos en la secuencia
            frecuencia.append(contador_tirada)
            contador_tirada=0
            montoTotal.append(monto)
        else:
            apuesta = fib_sequence[min(fib_index + 1, len(fib_sequence) - 1)] * apuesta_gral
            print("salio negro")
            print("Apuesta:", apuesta)
            monto -= apuesta
            montoTotal.append(monto)
            fib_index += 1  # Avanza al siguiente número en la secuencia
            if monto < apuesta:
                print("No tienes suficiente dinero para seguir apostando.")
                break
    print(montoTotal)  

def dalembert():
    monto = monto_inicial
    apuesta = apuesta_gral
    contador_tirada = 0
    for i in range(1,cant_tiradas + 1):
        resultado=tirar_ruleta()
        contador_tirada+=1
        if resultado in rojos:
            monto+=apuesta * 2
            print("Ganaste! Monto actual es:", monto,"jugando,",apuesta)
            apuesta-=apuesta_gral
            if apuesta < apuesta_gral:
                apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
            montoTotal.append(monto)
            
        else:
            print("perdiste la apuesta jugando,",apuesta)
            apuesta+=apuesta_gral 
            monto-=apuesta
            print("tu monto ahora es",monto)
            montoTotal.append(monto)
            if monto < apuesta_gral:
                print("te quedaste sin dinsero")
                break
    print(montoTotal)
"""def redbet():
    monto=monto_inicial
    apuestarojo=apuesta_gral
    apuestanegro=10
    for i in range(cant_tiradas):
        resultado= tirar_ruleta()
        if cant_tiradas==0:
            if resultado in rojos:
                """

def martingala_infi():
    ganancia=0
    monto=monto_inicial
    apuesta=apuesta_gral
    contador_tirada=0
    for i in range(1,cant_tiradas+1):
        resultado=tirar_ruleta()
        contador_tirada+=1
        if resultado in rojos:
            monto+=apuesta * 2
            ganancia += apuesta *2           
            apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
            montoTotal.append(monto)
            print("salio rojo en la tirada:",i+1,",ganancia-->" ,ganancia)
            print("monto acumulado-->",monto)
        else:
            apuesta *=2
            monto -=apuesta
            montoTotal.append(monto)
    print(montoTotal)  

def fibonacci_infi():
    monto = monto_inicial
    apuesta = apuesta_gral
    fib_sequence = seq_fibonacci(cant_tiradas)
    tiradas_realizadas = 0
    fib_index=0
    contador_tirada=0
    for _ in range(1,cant_tiradas+1):
        resultado = tirar_ruleta()
        tiradas_realizadas += 1
        contador_tirada+=1
        if resultado in rojos :
            monto += apuesta * 2
            print("Salio rojo en la tirada:", tiradas_realizadas)
            print("Monto acumulado-->", monto)
            fib_index = max(0, fib_index - 2)  # Retrocede dos pasos en la secuencia
            frecuencia.append(contador_tirada)
            contador_tirada=0
            montoTotal.append(monto)
        else:
            apuesta = fib_sequence[min(fib_index + 1, len(fib_sequence) - 1)] * apuesta_gral
            print("salio negro")
            print("Apuesta:", apuesta)
            monto -= apuesta
            montoTotal.append(monto)
            fib_index += 1  # Avanza al siguiente número en la secuencia
    print(montoTotal)    
def dalembert_infi():
    monto = monto_inicial
    apuesta = apuesta_gral
    contador_tirada = 0
    for i in range(1,cant_tiradas + 1):
        resultado=tirar_ruleta()
        contador_tirada+=1
        if resultado in rojos:
            monto+=apuesta * 2
            apuesta-=apuesta_gral
            if apuesta < apuesta_gral:
                apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
            montoTotal.append(monto)
            print("Ganaste! Monto actual es:", monto)
            print("Tu proxima apuesta es",apuesta)
        
        else:
            apuesta+=apuesta_gral
            monto-=apuesta
            print("Perdiste,tu proxima apuesta es",apuesta)
            montoTotal.append(monto)

    print(frecuencia)
    print(montoTotal)

for i in range(num_corridas):
    if estrategia =='m' and capital=='f':
        martingala()
        vu_MG, fr_MG=np.unique(frecuencia,return_counts=True)        
        plt.bar(vu_MG, fr_MG, color='blue')
        plt.xlabel('Tiradas desde la última ganancia')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de tiradas desde la última ganancia')
        plt.show()

        plt.plot(montoTotal,color='red')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--')
        plt.show()

    elif estrategia=='f' and capital=='f' : 
        fibonacci()
        vu_FIB, fr_FIB=np.unique(frecuencia,return_counts=True)
        plt.bar(vu_FIB, fr_FIB, color='blue')
        plt.xlabel('Tiradas desde la última ganancia')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de tiradas desde la última ganancia')
        plt.show()
        plt.plot(montoTotal,color='red')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--')
        plt.savefig("grafica_flujo_caja.png")
        plt.show()
    elif estrategia=='f' and capital=='i' : 
        fibonacci_infi()
        vu_FIB, fr_FIB=np.unique(frecuencia,return_counts=True)
        plt.bar(vu_FIB, fr_FIB, color='blue')
        plt.xlabel('Tiradas desde la última ganancia')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de tiradas desde la última ganancia')
        plt.show()
        plt.plot(montoTotal,color='red')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--')
        plt.show()
    elif estrategia=='d' and capital=='f':
        dalembert()
        vu_DAL,fr_DAL=np.unique(frecuencia,return_counts=True)
        plt.bar(vu_DAL,fr_DAL,color='blue')
        plt.xlabel('Tiradas desde la última ganancia')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de tiradas desde la última ganancia')
        plt.show()
        plt.plot(montoTotal,color='red')

        plt.axhline(y=monto_inicial, color='blue', linestyle='--')
        plt.show()
    elif estrategia=='d' and capital=='i':
        dalembert_infi()
        vu_DAL,fr_DAL=np.unique(frecuencia,return_counts=True)
        plt.bar(vu_DAL,fr_DAL,color='blue')
        plt.xlabel('Tiradas desde la última ganancia')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de tiradas desde la última ganancia')
        plt.show()
        plt.plot(montoTotal,color='red')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--')
        plt.show()
    elif estrategia == 'm' and capital =='i':
        martingala_infi()
        vu_MG, fr_MG=np.unique(frecuencia,return_counts=True)        
        plt.bar(vu_MG, fr_MG, color='blue')
        plt.xlabel('Tiradas desde la última ganancia')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de tiradas desde la última ganancia')
        plt.show()

        plt.plot(montoTotal,color='red')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--')
        plt.show()