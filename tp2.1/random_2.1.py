import random
import msvcrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest
randomNumList =[]


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
    expected_count = len(bits) / 2.0
    if expected_count == 0:
        return float('inf')  # Retornar infinito si expected_count es cero para indicar un resultado extremo
    else:
        return abs(ones_count - expected_count) / expected_count

def convert_to_bits(numbers):
    return ''.join(format(num, '032b') for num in numbers)






def frequency_test_block(bits, block_size=8):
    
    num_blocks = len(bits) // block_size
    block_counts = [bits[i*block_size:(i+1)*block_size].count('1') for i in range(num_blocks)]
    
    
    block_proportions = [count / block_size for count in block_counts]
    expected_proportion = 0.5
    
    
    chi_square = sum(((proportion - expected_proportion) ** 2) / expected_proportion for proportion in block_proportions)
    
    return chi_square

def runs_test(bits):
    
    n = len(bits)
    runs = 1
    for i in range(1, n):
        if bits[i] != bits[i-1]:
            runs += 1
    
    
    expected_runs = ((2 * n) - 1) / 3
    variance_runs = ((16 * n) - 29) / 90
    
    
    z = (runs - expected_runs) / np.sqrt(variance_runs)
    
    return z




def doSimpleTests():
    bits_string = convert_to_bits(randomNumList)
    block_size = 8
    chi_square = frequency_test_block(bits_string, block_size)
    print(f"Frequency Test: Block (Tamaño del bloque = {block_size}): {chi_square}")
    z = runs_test(bits_string)
    print(f"Runs Test: z = {z}")



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

    doSimpleTests()

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



