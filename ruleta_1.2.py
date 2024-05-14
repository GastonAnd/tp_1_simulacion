import random
import matplotlib.pyplot as plt
import numpy as np
import sys
args = sys.argv[1:]

if len(args) !=8 or args[0] != '-c' or args[2] != '-n' or args[4] != '-s' or args[6] !='-a' :
    print("Uso: python script.py -c <corridas> -n <tiradas> -s <estrategia(m,f,d)> -a <capital(f,i)>")
    sys.exit(1)

num_corridas = int(args[1])
cant_tiradas = int(args[3])
capital = (args[7])
estrategia=(args[5])
rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
monto_inicial=5000
apuesta_gral=150
tiradas=0
def tirar_ruleta():
    return random.randint(0, 36)
def seq_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def martingala():
    monto=monto_inicial
    apuesta=apuesta_gral
    contador_tirada=0  #contador frecuencia absoluta
    global tiradas
    for i in range(1,cant_tiradas+1):
        resultado=tirar_ruleta()
        contador_tirada+=1
        monto -=apuesta
        montoTotal.append(monto)
        tiradas+=1
        if resultado in rojos:
            monto+=apuesta * 2
            apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
        else:
            apuesta *=2                        
            if monto < apuesta:
                break
def fibonacci():
    monto = monto_inicial
    apuesta = apuesta_gral
    fib_sequence = seq_fibonacci(cant_tiradas)
    tiradas_realizadas = 0
    fib_index=0
    contador_tirada=0
    global tiradas
    for _ in range(1,cant_tiradas+1):
        resultado = tirar_ruleta()
        tiradas_realizadas += 1
        contador_tirada+=1
        monto -= apuesta
        montoTotal.append(monto)
        tiradas+=1
        if resultado in rojos :
            monto += apuesta * 2
            fib_index = max(0, fib_index - 2)  # Retrocede dos pasos en la secuencia
            frecuencia.append(contador_tirada)
            contador_tirada=0
        else:
            apuesta = fib_sequence[min(fib_index + 1, len(fib_sequence) - 1)] * apuesta_gral            
            fib_index += 1  # Avanza al siguiente número en la secuencia
            if monto < apuesta:
                break
def dalembert():
    monto = monto_inicial
    apuesta = apuesta_gral
    contador_tirada = 0
    global tiradas
    for _ in range(1,cant_tiradas + 1):
        resultado=tirar_ruleta()
        contador_tirada+=1
        monto-=apuesta
        montoTotal.append(monto)
        tiradas+=1
        if resultado in rojos:
            monto+=apuesta * 2
            apuesta-=apuesta_gral
            if apuesta < apuesta_gral:
                apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
        else:
            apuesta+=apuesta_gral 
            if monto < apuesta:
                break
def labouchere():
    monto = monto_inicial
    secuencia_inicial = [50,50,50]  # Secuencia inicial de Labouchere, se puede cambiar
    secuencia = secuencia_inicial.copy()
    frecuencia = []
    montoTotal = []
    contador_tirada = 0
    for i in range(cant_tiradas):
        if len(secuencia) == 0:
            secuencia = secuencia_inicial.copy()  # Reiniciar la secuencia
        apuesta = secuencia[0] if len(secuencia) == 1 else secuencia[0] + secuencia[-1]
        if monto < apuesta:
            print(f"No hay suficiente capital para continuar después de {i} tiradas.")
            break
        resultado = tirar_ruleta()
        contador_tirada += 1
        monto -= apuesta
        if resultado in rojos:
            monto += apuesta * 2
            if len(secuencia) > 1:
                secuencia = secuencia[1:-1]  # Eliminar primer y último número
            else:
                secuencia.pop(0)  # Eliminar el único número que queda
            frecuencia.append(contador_tirada)
            contador_tirada = 0
        else:
            secuencia.append(apuesta)  # Añadir apuesta al final de la secuencia

        montoTotal.append(monto)
    return montoTotal, frecuencia
def martingala_infi():
    monto=monto_inicial
    apuesta=apuesta_gral
    contador_tirada=0
    for i in range(cant_tiradas):
        resultado=tirar_ruleta()
        contador_tirada+=1
        monto -=apuesta
        if resultado in rojos:
            monto+=apuesta * 2       
            apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
        else:
            apuesta *=2
        montoTotal.append(monto)
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
        monto -= apuesta
        montoTotal.append(monto)
        if resultado in rojos :
            monto += apuesta * 2
            fib_index = max(0, fib_index - 2)  # Retrocede dos pasos en la secuencia
            frecuencia.append(contador_tirada)
            contador_tirada=0
        else:
            apuesta = fib_sequence[min(fib_index + 1, len(fib_sequence) - 1)] * apuesta_gral
            fib_index += 1  # Avanza al siguiente número en la secuencia
def dalembert_infi():
    monto = monto_inicial
    apuesta = apuesta_gral
    contador_tirada = 0
    for _ in range(cant_tiradas ):
        resultado=tirar_ruleta()
        contador_tirada+=1
        monto-=apuesta
        montoTotal.append(monto)
        if resultado in rojos:
            monto+=apuesta * 2
            apuesta-=apuesta_gral
            if apuesta < apuesta_gral:
                apuesta=apuesta_gral
            frecuencia.append(contador_tirada)
            contador_tirada=0
        else:
            apuesta+=apuesta_gral
def labouchere_infi():
    monto = monto_inicial
    secuencia_inicial = [50,50,50]  # Secuencia inicial de Labouchere, puedes cambiarla
    secuencia = secuencia_inicial.copy()
    frecuencia = []
    montoTotal = []
    contador_tirada = 0
    for i in range(cant_tiradas):
        if len(secuencia) == 0:
            secuencia = secuencia_inicial.copy()  # Reiniciar la secuencia
        apuesta = secuencia[0] if len(secuencia) == 1 else secuencia[0] + secuencia[-1]
        resultado = tirar_ruleta()
        contador_tirada += 1
        monto -= apuesta
        if resultado in rojos:
            monto += apuesta * 2
            if len(secuencia) > 1:
                secuencia = secuencia[1:-1]  # Eliminar primer y último número
            else:
                secuencia.pop(0)  # Eliminar el único número que queda
            frecuencia.append(contador_tirada)
            contador_tirada = 0
        else:
            secuencia.append(apuesta)  # Añadir apuesta al final de la secuencia

        montoTotal.append(monto)
    return montoTotal, frecuencia
for i in range(1,num_corridas+1):
    frecuencia=[]
    montoTotal=[]
    if estrategia =='m' and capital=='f':
        martingala()
        vu_MG, fr_MG=np.unique(frecuencia,return_counts=True)   
        frec_rel_MG=[]    
        for i in range(0,len(fr_MG)):
            frec_rel_MG.append(fr_MG[i]/tiradas) 
        plt.bar(vu_MG, frec_rel_MG, color='blue')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_martingala_finito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_martingala.png")
        plt.show()
    elif estrategia=='f' and capital=='f' : 
        fibonacci()
        vu_FIB, fr_FIB=np.unique(frecuencia,return_counts=True)
        fr_rel_FIB=fr_FIB/  np.sum(fr_FIB)     
        frec_rel_FIB=[]    
        for i in range(0,len(fr_FIB)):
            frec_rel_FIB.append(fr_FIB[i]/tiradas)
        plt.bar(vu_FIB, fr_rel_FIB, color='blue')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_fibonacci_finito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_fibonacci.png")
        plt.show()
    elif estrategia=='f' and capital=='i' : 
        fibonacci_infi()
        vu_FIB, fr_FIB=np.unique(frecuencia,return_counts=True)
        frec_rel_FIB=[]    
        for i in range(0,len(fr_FIB)):
            frec_rel_FIB.append(fr_FIB[i]/cant_tiradas)
        plt.bar(vu_FIB, frec_rel_FIB, color='blue')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_fibonacci_infinito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_fibonacci_infinito.png")
        plt.show()
    elif estrategia=='d' and capital=='f':
        dalembert()
        vu_DAL,fr_DAL=np.unique(frecuencia,return_counts=True)
        frec_rel_DAL=[]    
        for i in range(0,len(fr_DAL)):
            frec_rel_DAL.append(fr_DAL[i]/tiradas)
        plt.bar(vu_DAL, frec_rel_DAL, color='blue')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_dalembert_finito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_dalembert.png")
        plt.show()
    elif estrategia=='d' and capital=='i':
        dalembert_infi()
        vu_DAL,fr_DAL=np.unique(frecuencia,return_counts=True)
        frec_rel_DAL=[]    
        for i in range(0,len(fr_DAL)):
            frec_rel_DAL.append(fr_DAL[i]/cant_tiradas)
        plt.bar(vu_DAL, frec_rel_DAL, color='blue')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_dalembert_infinito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_dalembert_infinito.png")        
        plt.show()
    elif estrategia == 'm' and capital =='i':
        martingala_infi()
        vu_MG, fr_MG=np.unique(frecuencia,return_counts=True) 
        frec_rel_MG=[]    
        for i in range(0,len(fr_MG)):
            frec_rel_MG.append(fr_MG[i]/cant_tiradas)
        plt.bar(vu_MG, frec_rel_MG, color='blue')    
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_martingala_infinito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_martingala_infito.png")
        plt.show()
    elif estrategia=='l' and capital=='f':
        montoTotal,frecuencia=labouchere()
        vu_MG, fr_MG=np.unique(frecuencia,return_counts=True) 
        frec_rel_MG=[]    
        for i in range(0,len(fr_MG)):
            frec_rel_MG.append(fr_MG[i]/cant_tiradas)
        plt.bar(vu_MG, frec_rel_MG, color='blue')    
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_labouchere_finito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_laboucher_finito.png")
        plt.show()
    elif estrategia=='l' and capital=='i':
        montoTotal,frecuencia=labouchere_infi()
        vu_MG, fr_MG=np.unique(frecuencia,return_counts=True) 
        frec_rel_MG=[]    
        for i in range(0,len(fr_MG)):
            frec_rel_MG.append(fr_MG[i]/cant_tiradas)
        plt.bar(vu_MG, frec_rel_MG, color='blue')    
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Frecuencia Relativa')
        plt.title('Frecuencia relativa de obtener apuesta favorable')
        plt.savefig("grafica_frecuencia_relativa_labouchere_infinito.png")        
        plt.show()
        plt.plot(montoTotal,color='red',label='Flujo de Caja')
        plt.xlabel('Numero de Tiradas')
        plt.ylabel('Cantidad de Capital')
        plt.title('Flujo de caja')
        plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
        plt.legend()
        plt.savefig("grafica_flujo_caja_laboucher_infinito.png")
        plt.show()
