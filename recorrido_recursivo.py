#Archivo: recorrido_recursivo.py
import argparse    #Importa biblioteca que nos permite leer desde la línea de comandos
import turtle    #Importa biblioteca que nos permite usar tortugas

ap = argparse.ArgumentParser()    #Instanciando como ap
ap.add_argument("--huellas", required=True, help="número de huellas")#Especificando la bandera
#También se verifica con True que sea ingresada para que el programa funcione.
args = vars(ap.parse_args())    #Lo que se obtiene es un diccionario (llave:valor) , en este caso llamado args
huellas = int(args["huellas"])    #Los valores del diccionario son cadenas por lo que se tiene que transformar a entero

wn=turtle.Screen()    #Crea la ventana para mostrar las tortugas
wn.bgcolor("yellow")    #Cambia el color del fondo
carrerin=turtle.Turtle()    #Crea una tortuga (que se llama carrerin)
carrerin.shape("turtle")    #Se le da el sprite de tortuga
carrerin.color("dark green")    #Cambia el color de la tortuga
carrerin.penup()    #Evita que quede una linea en la ruta de la tortuga
size=20     #Cambia el tamaño del centro de la espiral.

def recorrido_recursivo(carrerin,size,huellas):
    if huellas > 0:    #Condicional para imprimir de 1 a n tortugas
        carrerin.stamp()    #Huella de tortuga
        size=size+2    #Incremento del paso de la tortuga por iteración
        carrerin.forward(size)    #Se mueve la tortuga hacia adelante
        carrerin.right(24)    #y gira a la izquierda
        recorrido_recursivo(carrerin, size, huellas-1)#Recursividad, reduciendo huellas hasta que llegue a 0

recorrido_recursivo(carrerin,size,huellas)    #Se llama a la función para ejecutarse
        
wn.mainloop()    #Auxiliar para que el usuario termine el programa


