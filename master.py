import matplotlib.pyplot as plt
import random
import os
import time

#Asiganación del código de colores a resolver
def asignacion():
    canicas = []
    colores = ['red','green','yellow','blue','purple','orange','black','pink'] #Posibles colores
    for i in range(4): #Ciclo que añade semialeatoriamente cuatro colores distintos a una lista.
        rand= random.randint(0,len(colores)-1)
        canicas.append(colores.pop(rand)) #Eliminamos el color seleccionado para que no se repita
    return canicas

#Para poder introducir un intento manualmente
def introducir():
    print('\nIntroduzca los colores en inglés') #En una futura actualización voy a añadir manejo de errores con una mejor manera de elegir los colores
    canicasIngles = []
    for i in range(4): #Con un ciclo le pedimos al usuario las canícas una por una
        canicasIngles.append(input('Introduzca la canica '+str(i+1)+': '))
    return canicasIngles #NOTA: Importante mejorar, pues si escriben mal un color, truena
 
#Para determinar las canicas acertadas    
def comparar(turno,reales):
    acertadas = 0
    exactas = 0
    comparacion = []
    auxiliar = []
    for copia in range(len(reales)): #Copiamos el código a adivinar en una lista auxiliar
        auxiliar.append(reales[copia])
        
    for i in range(len(turno)): #Comparamos color y posición y vamos guardando la cantidad de aciettos de cada opción
        for j in range(len(turno)):
            if auxiliar[i]==turno[j]:
                if auxiliar[i]==turno[i]:
                    exactas+=1
                else:
                    acertadas +=1
                auxiliar[i]='white'     #Lleno ese espacio con blanco para que no se duplique el valor de las acertadas en caso de que el color se repita en el intento
        
    comparacion.append(exactas)
    comparacion.append(acertadas)
    return comparacion #Regresa una lista con dos cantidades, de exactas y acertadas (color presente en mala posición)

#Para ir guardando los intentos en una lista
def aniadirIntento(intentos):
    intento = introducir() #Guardamos un nuevo intento
    intentosNuevos = intentos #Guardamos los intentos previos en una lista
    intentosNuevos.append(intento)
    return intentosNuevos #Al final esta función sirve en síntesis, para guardar todos los intentos que se han hecho y generar uno nuevo.

def aniadirIntentoAuto(intentos,turno):
    intento = []
    for i in range(len(turno)):
        intento.append(turno[i])
    intentosNuevos = intentos
    intentosNuevos.append(intento)
    return intentosNuevos #Esta función hace exactamente lo mismo que la anterior, solo que no pide al usuario un nuevo intento, lo genera en automático.

#Para imprimir en pantalla nuestros intentos
def imprimirIntentos(intentos, reales):
    n = len(intentos)
    
    colores = ['red','green','yellow','blue','purple','orange','black','pink'] #Lista de colores para imprimir (graficar) en pantalla.
#Mediante un ciclo imprimimos 'o' en pantalla que representan los 8 colores posibles.
#Además vamos imprimiendo las lineas que nos sirven como borde del tablero.
    for color in range(8):
        plt.plot( [0.66+(0.66*color),0.66+(0.66*color)], [-0.75,-0.75], marker='o', color=colores[color])
    plt.plot( [0,6], [-0.5,-0.5], color='black')
    plt.plot( [0,6], [-1,-1], color='black')
    

    for i in range(n):
    #Guardamos la información de nuestras cruces o 'x' que vamos a colocar en pantalla, principalmente la cantidad.    
        comparadas = comparar(intentos[i], reales)
        acertadas = comparadas[1]
        exactas = comparadas[0]
        malas = 4-acertadas-exactas
        cruces = []

#Imprimimos en pantalla la cantidad de cruces dependiendo de cuantas cruces de cada color existan        
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

      #Generamos la gráfica y la mostramos en una nueva ventana
    plt.plot()
    plt.show()   

#Se genera un juego manual        
def juegoManual():
    canicas = asignacion()
    
    intentos = []
    i = 0
    aniadirIntento(intentos)
    imprimirIntentos(intentos, canicas)
    
    comparacion = comparar(intentos[0], canicas)
    while not(comparacion[0]==4):
        aniadirIntento(intentos)
        imprimirIntentos(intentos, canicas)
        i += 1
        comparacion = comparar(intentos[i], canicas)

    print("\nHas ganado, el código correcto es:",canicas)

#Se genera un juego automatico con todo e instrucciones
#Incluye un algoritmo de resolución automática 100% infalible
def juegoAuto():
    canicas = asignacion()
    colores = ['red','green','yellow','blue','purple','orange','black','pink']
    intentos = []
    probando=['','','','']
    espacios=[0,1,2,3]
    print("\nLa forma de jugar es la siguiente:")
    print("1. El juego va a generar un código de colores que son representados como canícas en pantalla.")
    print("     Para este caso en específico, el código es el siguiente: ", canicas)
    print("2. Siempre habrá cuatro canícas en cada juego.")
    print("3. Cada caníca del código tendrá un color único e irrepetible.")
    print("4. Los posibles colores de las canícas son los siguientes: ", colores)
    print("5. En cada intento podrás elegir cuatro colores, uno para cada caníca.")
    print("6. Si te sirve para tu estrategia, puedes repetir colores en el mismo intento.")
    print("7. Después de cada intento, se mostrará en pantalla los colores que elegiste.")
    print("8. Del lado izquierdo de la pantalla, se mostrarán cuatro 'x'.")
    print("     Las 'x' en rojo representan la cantidad de colores colocados que no existen en la respuesta.")
    print("     La cantidad de 'x' amarillas representan la cantidad de colores que tienes bien, están en la respuesta, pero no están en el orden correcto.")
    print("     Las 'x' en verde representan cuantas canícas has acertado, tanto en color, como en posición.")
    print(" Debes tener presente que las 'x' solo representan la cantidad, más no la posición de las canícas en tu intento.")
    print("9. Deberás analizar detenidamente las pistas para saber como hacer tu próximo movimiento.")
    print("10. Al tener todas las canícas con el color y la posición correctas, habrás ganado.")
    print("\n NOTA: Después de introducir cada intento, se mostrará en pantalla una nueva ventana con el tablero, por favor cierra la ventana antes de continuar con el siguiente intento.")
    print("\n A continuación se muestra un ejemplo de la resolución automática del código generado en este intento: ")
    
    while probando!=canicas:
        for i in espacios:
            probando[i]=colores[random.randint(0, len(colores)-1)]
        print(probando, end=" ")
        
        aniadirIntentoAuto(intentos,probando)
        
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
        imprimirIntentos(intentos, canicas)
    if probando == canicas:
        print("\nHas ganado, el código correcto es:",canicas)

#Genera un título bonito    
def titulo():
    os.system("figlet Mastermind")

#Genera un menú básico
def menu():
    while True:
        print("\nMenú:")
        print("1. Jugar")
        print("2. Autoplay")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            juegoManual()
        elif opcion == '2':
            juegoAuto()
        elif opcion == '3':
            print("Saliendo del juego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#Inicia el título y menú
if __name__ == "__main__":
    titulo()
    menu()