from tkinter import *

raiz = Tk()
raiz.title("Ventana de prueba") 
#raiz.resizable(0, 0) # Bloquea o no el tamaño de la ventana
raiz.iconbitmap("D:\CursoBotLAB\Python\MaterialPython\GUI\logo.ico")
#raiz.geometry("650x350") # Define un tamaño especifico para la ventana
#raiz.config(bg="blue")

miFrame = Frame() # Instancia del objeto miFrame
miFrame.pack()
#miFrame.pack(fill="both", expand="True")
#miFrame.pack(side="right", anchor="s") # Empaqueta el frame en la raíz
miFrame.config(bg="#383C45")
miFrame.config(width="650", height="350") # Ajusta el tamaño del frame
#miFrame.config(bd="30") # Ancho del borde
#miFrame.config(relief="groove")
miFrame.config(relief="sunken") # Tipo de borde
miFrame.config(cursor="pirate") # Tipo de cursor sobre el frame
#miFrame.config(cursor="pirate")

raiz.mainloop() # Bucle infinito