import random
import msvcrt
import matplotlib.pyplot as plt
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

def GCL(seed, a=1664525, c=1013904223, m=2**32): 
    while True:
        seed = (a * seed + c) % m
        yield seed


def GeneradorGCL(semilla= 12345,c = 10000): #Generador de numeros pseudoaleatorios 1
    global randomNumList
    gen = GCL(semilla)
    randomNumList = [next(gen) for _ in range(c)]
    

    
def GeneradorRamdom(n=1,m=100, c=10): #Generacion de numeros aleatorios random (de n a m y la cantidad es c)
    global randomNumList
    for i in range(c):
        n =random.randint(n, m)
        randomNumList.append(n)



def MetododelCuadrado(seed=12345678,width=8,c=10000): #Generador de metodo del cuadrado
    global randomNumList
    current_value=seed
    for _ in range(c):
        squared=str(current_value **2).zfill(2 * width) #Eleva al cuadrado el valor actual
        
        start=(len(squared)-width) // 2     #Obtiene los numeros centrales
        end = start + width
        current_value = int(squared[start:end])

        randomNumList.append(current_value)


def Test1(): #Test 1
    print("Test 1")

def Test2(): #Test 2
    print("Test 2")

def Test3(): #Test 3
    print("Test 3")

def Test4(): #Test 4
    print("Test 4")



def doTest():
    PlotDispersión()
    PlotHistograma()

def PlotDispersión():
    # Crear la gráfica de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(randomNumList)), randomNumList, color='blue')

# Etiquetas y título
    plt.title('Gráfica de Dispersión de Números Generados')
    plt.xlabel('Índice')
    plt.ylabel('Valor Generado')

# Mostrar la gráfica
    plt.show()

def PlotHistograma():

    plt.figure(figsize=(10, 6))
    plt.hist(randomNumList, bins=10, edgecolor='k', alpha=0.7)
    
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
            print(randomNumList)
            doTest()
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
            randomNumList.clear()

        if(i=='S'): 
            print("Fin del programa")
            
        
        


Menu()



