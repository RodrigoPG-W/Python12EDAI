#Archivo: recorrido_no_recursivo.py
import turtle    #Importa biblioteca que nos permite usar tortugas
wn=turtle.Screen()    #Crea la ventana para mostrar las tortugas
wn.bgcolor("pale turquoise")    #Cambia el color del fondo
carrerin=turtle.Turtle()    #Crea una tortuga (que se llama carrerin)
carrerin.shape("turtle")    #Se le da el sprite de tortuga
carrerin.color("dark green")    #Cambia el color de la tortuga

carrerin.penup()    #Evita que quede una linea en la ruta de la tortuga
size=15     #Cambia el tamaño del centro de la espiral.
for i in range(60):    #Esta determinado que se impriman 30 huellas de la tortuga
    carrerin.stamp()    #Huella de tortuga
    size=size+2    #Incremento del paso de la tortuga por iteración
    carrerin.forward(size)    #Se mueve la tortuga hacia adelante
    carrerin.left(24)    #y gira a la izquierda

wn.mainloop()    #Auxiliar para que el usuario termine el programa


