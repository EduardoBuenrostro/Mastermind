import matplotlib.pyplot as plt
import random

#Asiganación del código de colores a resolver
def asignacion():
    canicas = []
    colores = ['red','green','yellow','blue','purple','orange','black','pink']
    for i in range(4):
        rand= random.randint(0,len(colores)-1)
        canicas.append(colores.pop(rand))
    return canicas

#Para poder introducir un intento manualmente
def introducir():
    print('Introduzca los colores en inglés')
    canicasi = []
    for i in range(4):
        canicasi.append(input('Introduzca la canica '+str(i+1)+': '))
    return canicasi
 
#Para determinar las canicas acertadas    
def comparar(turno,reales):
    acertadas = 0
    exactas = 0
    comparacion = []
    auxiliar = []
    for copia in range(len(reales)):
        auxiliar.append(reales[copia])
        
    for i in range(len(turno)):
        for j in range(len(turno)):
            if auxiliar[i]==turno[j]:
                if auxiliar[i]==turno[i]:
                    exactas+=1
                else:
                    acertadas +=1
                auxiliar[i]='white'     #Lleno ese espacio con blanco para que no se duplique el valor de las acertadas en caso de que el color se repita en el intento
        
    comparacion.append(exactas)
    comparacion.append(acertadas)
    return comparacion

#Para ir guardando los intentos en una lista
def aniadirintento(intentos):
    intento = introducir()
    intentosn = intentos
    intentosn.append(intento)
    return intentosn

def aniadirintentoAuto(intentos,turno):
    intento = []
    for i in range(len(turno)):
        intento.append(turno[i])
    intentosn = intentos
    intentosn.append(intento)
    return intentosn

#Para imprimir en pantalla nuestros intentos
def imprimirintentos(intentos, reales):
    n = len(intentos)
    
    colores = ['red','green','yellow','blue','purple','orange','black','pink']
    for color in range(8):
        plt.plot( [0.66+(0.66*color),0.66+(0.66*color)], [-0.75,-0.75], marker='o', color=colores[color])
    plt.plot( [0,6], [-0.5,-0.5], color='black')
    plt.plot( [0,6], [-1,-1], color='black')
    
    for i in range(n):
        
        comparadas = comparar(intentos[i], reales)
        acertadas = comparadas[1]
        exactas = comparadas[0]
        malas = 4-acertadas-exactas
        cruces = []
        
        if exactas > 0:
            for k in range(exactas):
                cruces.append('green')
        if acertadas > 0:
            for j in range(acertadas):
                cruces.append('yellow')
        if malas > 0:
            for l in range(malas):
                cruces.append('red')
        
        for punto in range(4):
            plt.plot( [punto+1,punto+1], [i,i], marker='o', color=intentos[i][punto])
        
        plt.plot( [5,5],[i+0.25,i+0.25], marker='x', color=cruces[0])
        plt.plot( [5.5,5.5],[i+0.25,i+0.25], marker='x', color=cruces[1])
        plt.plot( [5,5],[i-0.25,i-0.25], marker='x', color=cruces[2])
        plt.plot( [5.5,5.5],[i-0.25,i-0.25], marker='x', color=cruces[3])
        
        plt.plot( [0,6], [(i+0.5),(i+0.5)], color='black')
        plt.plot( [4.5,4.5], [-0.5,i+0.5], color='black')
        plt.plot( [6,6], [-1,i+0.5], color='black')
        plt.plot( [0,0], [-1,i+0.5], color='black')
      
    plt.plot()
    plt.show()
        
def juegomanual():
    canicas = asignacion()
    print(canicas)
    intentos = []
    i = 0
    aniadirintento(intentos)
    imprimirintentos(intentos, canicas)
    
    comparacion = comparar(intentos[0], canicas)
    while not(comparacion[0]==4):
        aniadirintento(intentos)
        imprimirintentos(intentos, canicas)
        i += 1
        comparacion = comparar(intentos[i], canicas)

def juegoAuto():
    canicas = asignacion()
    colores = ['red','green','yellow','blue','purple','orange','black','pink']
    intentos = []
    probando=['','','','']
    espacios=[0,1,2,3]
    print(canicas)
    
    while probando!=canicas:
        for i in espacios:
            probando[i]=colores[random.randint(0, len(colores)-1)]
        print(probando, end=" ")
        
        aniadirintentoAuto(intentos,probando)
        
        acertadas = 0
        exactas = 0
        comparacion = []
        auxiliar=[]
        for i in range(4):
            auxiliar.append(probando[i])
        
        for i in range(len(probando)):
            color=True
            for j in range(len(probando)):
                if auxiliar[i]==canicas[j]:
                    if auxiliar[i]==canicas[i]:
                        exactas+=1
                        for k in espacios:
                            if k==i:
                                espacios.remove(i)
                                break
                        for k in colores:
                            if k==probando[i]:
                                colores.remove(probando[i])
                                break
                    else:
                        acertadas +=1
                    auxiliar[i]=''     #Lleno ese espacio con blanco para que no se duplique el valor de las acertadas en caso de que el color se repita en el intento
                    color=False
            if color:
                for k in colores:
                    if k==probando[i]:
                        colores.remove(probando[i])
                        break
        
        comparacion.append(exactas)
        comparacion.append(acertadas)
        print(comparacion)
        imprimirintentos(intentos, canicas)
    if probando == canicas:
        print("Has ganado, el código correcto es:",canicas)

def juegoAuto():
    canicas = asignacion()
    colores = ['red','green','yellow','blue','purple','orange','black','pink']
    intentos = []
    probando=['','','','']
    espacios=[0,1,2,3]
    print(canicas)
    
    while probando!=canicas:
        for i in espacios:
            probando[i]=colores[random.randint(0, len(colores)-1)]
        print(probando, end=" ")
        
        aniadirintentoAuto(intentos,probando)
        
        acertadas = 0
        exactas = 0
        comparacion = []
        auxiliar=[]
        for i in range(4):
            auxiliar.append(probando[i])
        
        for i in range(len(probando)):
            color=True
            for j in range(len(probando)):
                if auxiliar[i]==canicas[j]:
                    if auxiliar[i]==canicas[i]:
                        exactas+=1
                        for k in espacios:
                            if k==i:
                                espacios.remove(i)
                                break
                        for k in colores:
                            if k==probando[i]:
                                colores.remove(probando[i])
                                break
                    else:
                        acertadas +=1
                    auxiliar[i]=''     #Lleno ese espacio con blanco para que no se duplique el valor de las acertadas en caso de que el color se repita en el intento
                    color=False
            if color:
                for k in colores:
                    if k==probando[i]:
                        colores.remove(probando[i])
                        break
        
        comparacion.append(exactas)
        comparacion.append(acertadas)
        print(comparacion)
        imprimirintentos(intentos, canicas)
    if probando == canicas:
        print("Has ganado, el código correcto es:",canicas)
    
juegomanual()