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


nombres_estrategia={
'm':'Martingala',
'f':'Fibonacci',
'd':'Dalembert',
'l':'Labouchere'
}

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
    global tiradas
    contador_tirada = 0
    for i in range(cant_tiradas):
        if len(secuencia) == 0:
            secuencia = secuencia_inicial.copy()  # Reiniciar la secuencia
        apuesta = secuencia[0] if len(secuencia) == 1 else secuencia[0] + secuencia[-1]
        if monto < apuesta:
            tiradas=i
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
    secuencia_inicial = [1000,500,1500,700,800,500]  # Secuencia inicial de Labouchere, puedes cambiarla
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

def plot_flujo_caja(montoTotalCorrida,filename,estrategia):
    for i, montoTotal in enumerate(montoTotalCorrida):
        plt.plot(montoTotal,label=f'Flujo de Caja en corrida {i +1}')
    plt.xlabel('Numero de Tiradas')
    plt.ylabel('Cantidad de Capital')
    nombre_estrategia=nombres_estrategia.get(estrategia,estrategia)
    plt.title(f'Flujo de caja estrategia:{nombre_estrategia}')
    plt.axhline(y=monto_inicial, color='blue', linestyle='--',label='Flujo de Caja Inicial')
    plt.legend()
    plt.savefig(filename)
    plt.show()

def plot_frecuencia_relativa(frecuencia,tiradas,corrida,estrategia):
    vu, fr=np.unique(frecuencia,return_counts=True)   
    frec_rel=[]    
    for i in range(0,len(fr)):
        frec_rel.append(fr[i]/tiradas) 
    plt.bar(vu, frec_rel, color='blue')
    plt.xlabel('Numero de Tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.ylim(0,0.25)
    nombre_estrategia=nombres_estrategia.get(estrategia,estrategia)
    plt.title(f'Frecuencia relativa de obtener apuesta favorable en la corrida {corrida}-Estrategia:{nombre_estrategia}')
    plt.savefig(f'grafica_frecuencia_relativa_estrategia_{nombre_estrategia}_capita_{capital}_corrida_{corrida}.png')        
    plt.show()
def plot_frecuencia_relativa_infi(frecuencia,corrida,estrategia):
    vu, fr=np.unique(frecuencia,return_counts=True)   
    frec_rel=[]    
    for i in range(0,len(fr)):
        frec_rel.append(fr[i]/cant_tiradas) 
    plt.bar(vu, frec_rel, color='blue')
    plt.xlabel('Numero de Tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.ylim(0,0.30)
    nombre_estrategia=nombres_estrategia.get(estrategia,estrategia)
    plt.title(f'Frecuencia relativa de obtener apuesta favorable en la corrida {corrida}-Estrategia:{nombre_estrategia}')
    plt.savefig(f'grafica_frecuencia_relativa_estrategia_{nombre_estrategia}_capital_{capital}_corrida_{corrida}.png')        
    plt.show()    
montoTotalCorrida=[]
for corrida in range(1,num_corridas+1):
    frecuencia=[]
    montoTotal=[]
    corrida=corrida
    if estrategia =='m' and capital=='f':
        martingala()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa(frecuencia,tiradas,corrida,estrategia)
    elif estrategia=='f' and capital=='f' : 
        fibonacci()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa(frecuencia,tiradas,corrida,estrategia)
    elif estrategia=='f' and capital=='i' : 
        fibonacci_infi()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa_infi(frecuencia,corrida,estrategia)
    elif estrategia=='d' and capital=='f':
        dalembert()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa(frecuencia,tiradas,corrida,estrategia)
    elif estrategia=='d' and capital=='i':
        dalembert_infi()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa_infi(frecuencia,corrida,estrategia)
    elif estrategia == 'm' and capital =='i':
        martingala_infi()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa_infi(frecuencia,corrida,estrategia)
    elif estrategia=='l' and capital=='f':
        montoTotal,frecuencia=labouchere()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa(frecuencia,tiradas,corrida,estrategia)
    elif estrategia=='l' and capital=='i':
        montoTotal,frecuencia=labouchere_infi()
        montoTotalCorrida.append(montoTotal)
        plot_frecuencia_relativa_infi(frecuencia,corrida,estrategia)

plot_flujo_caja(montoTotalCorrida,f'flujo_caja_estrategia_{estrategia}_capital_{capital}',estrategia)