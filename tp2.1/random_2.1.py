import random
import msvcrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest
randomNumList =[]

"""
Generador GCL: (semilla= primer valor, c= cantidad de valores a generar)
Genera los numeros seudoaleatorios


GCL:
    X(n+1) = (aXn + c) mod(m)
    
    m>0
    multiplicador 0<=a<m
    incremento c<=m
    Semilla 0<=X0<m
    
    X es la secuencia de números pseudoaleatorios.
    a es el multiplicador. (Encontrado empíricamente para proporcionar buenas propiedades estadísticas cuando se usa con un módulo m)
    c es el incremento. (Se elige de manera que sea impar y no tenga factores en común con m)
    𝑚 es el módulo.  (Rango de numeros que genera)
    X0 es la semilla inicial.

    Inicio
    Transicion
    Salida
    
"""
"""
Se estuvieron modificando los distintos valores de cada generador para probar,
habria que definir que valores usar
"""
def GCL(seed, a=134775813, c=1, m=2**32): 
    while True:
        seed = (a * seed + c) % m
        yield seed


def GeneradorGCL(semilla= 973160574,c = 100000): #Generador de numeros pseudoaleatorios 1
    global randomNumList
    gen = GCL(semilla)
    randomNumList = [next(gen) for _ in range(c)]
    

    
def GeneradorRamdom(n=1,m=2**32, c=50000): #Generacion de numeros aleatorios random (de n a m y la cantidad es c)
    global randomNumList
    for i in range(c):
        j =random.randint(n, m)
        randomNumList.append(j)



def MetododelCuadrado(seed=875302,width=6,c=1000000): #Generador de metodo del cuadrado
    global randomNumList
    current_value=seed
    for _ in range(c): 
        squared=str(current_value **2).zfill(2 * width) #Eleva al cuadrado el valor actual
        
        start=(len(squared)-width) // 2     #Obtiene los numeros centrales
        end = start + width
        current_value = int(squared[start:end])

        randomNumList.append(current_value)


def kol_smir_test(): #Kolmogorov smirnov test      d_stat=Estadístico D, p_value=Valor P
    d_stat, p_value = kstest(randomNumList,'uniform',
                             args=(min(randomNumList),
                             max(randomNumList)-min(randomNumList)))
    return d_stat,p_value
    
def monobit_test(bits): #Test 2 : test de monobit--> Esta prueba verifica si hay una distribucion equitativa de 1 y 0 en un conjun to de bits.
    ones_count = np.sum(bits == '1')
    zeros_count = len(bits) - ones_count
    expected_count = len(bits) / 2
    return abs(ones_count - expected_count) / expected_count

def convert_to_bits(numbers):
    return ''.join(format(num, '032b') for num in numbers)


def Test3(): #Test 3
    print("Test 3")

def Test4(): #Test 4
    print("Test 4")


def aprobtest(stat,value): #Temporal para un solo test, modificar para que todos se evaluan segun su resultado
    print(f"Kolmogorov-Smirnov Test:\nD-statistic = {stat}\np-value = {value}")
    if value < 0.05:
        print("Los números generados no parecen seguir una distribución uniforme (rechazo de la hipótesis nula).")
    else:
        print("Los números generados parecen seguir una distribución uniforme (no rechazo de la hipótesis nula).")


def doTest():
     # Convertir los números generados en una cadena de bits
    bits_string = convert_to_bits(randomNumList)
    
    # Realizar la prueba del monobit
    result = monobit_test(bits_string)
    print(f"Resultado Monobit: {result}")

    d_stat ,p_value = kol_smir_test()
    aprobtest(d_stat,p_value)
    PlotDispersión()
    PlotHistograma()

def PlotDispersión():
    # Crear la gráfica de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(randomNumList)), randomNumList,s=0.5,color='black')

# Etiquetas y título
    plt.title('Gráfica de Dispersión de Números Generados')
    plt.xlabel('Índice')
    plt.ylabel('Valor Generado')

# Mostrar la gráfica
    plt.show()

def PlotHistograma():

    plt.figure(figsize=(10, 6))
    plt.hist(randomNumList, bins=20, edgecolor='k', alpha=0.7)
    
    plt.title('Histograma de los Números Generados')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    
    plt.show()

def Menu():
    i = '0'
    while i != 'S':
        print("╔══════════════════════════════╗")
        print("║             Menu             ║")
        print("╠═══════╦══════════════════════╣")
        print("║ 'R'   ║ GeneradorRandom      ║")
        print("║ 'GCL' ║ GeneradorGCL         ║")
        print("║ 'C'   ║ GeneradorCuadrado    ║")
        print("║ 'S'   ║     Salir            ║")
        print("╚═══════╩══════════════════════╝")
        i = input("Ingrese una opción: ")

        
        if(i=='R'): GeneradorRamdom()
        elif(i=='GCL'): GeneradorGCL()
        elif(i=='C'):MetododelCuadrado()
        if(i!='S'): 
            #print(randomNumList)
            doTest()
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
            randomNumList.clear()

        if(i=='S'): 
            print("Fin del programa")
            
        
        


Menu()



