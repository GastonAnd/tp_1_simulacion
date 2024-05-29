import random
import msvcrt

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


def GeneradorGCL(semilla= 12345,c = 10): #Generador de numeros pseudoaleatorios 1
    global randomNumList
    gen = GCL(semilla)
    randomNumList = [next(gen) for _ in range(c)]
    

    
def GeneradorRamdom(n=1,m=100, c=10): #Generacion de numeros aleatorios random (de n a m y la cantidad es c)
    global randomNumList
    for i in range(c):
        n =random.randint(n, m)
        randomNumList.append(n)



def Generador2(): #Generador de numeros pseudoaleatorios 2
    global randomNumList
    print("Generador 2") 


def Test1(): #Test 1
    print("Test 1")

def Test2(): #Test 2
    print("Test 2")

def Test3(): #Test 3
    print("Test 3")

def Test4(): #Test 4
    print("Test 4")



def doTest():
    Test1()
    Test2()
    Test3()
    Test4()


def Menu():
    i = '0'
    while i != 'S':
        print("╔═════════════════════════╗")
        print("║          Menu           ║")
        print("╠═══════╦═════════════════╣")
        print("║ 'R'   ║ GeneradorRandom ║")
        print("║ 'GCL' ║ GeneradorGCL    ║")
        print("║ 'S'   ║     Salir       ║")
        print("╚═══════╩═════════════════╝")
        i = input("Ingrese una opción: ")

        
        if(i=='R'): GeneradorRamdom()
        elif(i=='GCL'): GeneradorGCL()
        
        if(i!='S'): 
            print(randomNumList)
            doTest()
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
            randomNumList.clear()

        if(i=='S'): 
            print("Fin del programa")
            
        
        


Menu()



