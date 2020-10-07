from tkinter import *

root = Tk()

miFrame = Frame(root, width=800, height=600)
miFrame.pack()

miImagen = PhotoImage(file="D:\CursoBotLAB\Python\MaterialPython\GUI\shield.png")
Label(miFrame, image=miImagen).place(x=300, y=50) # Forma abreviada para el Label

miLabel = Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18))
miLabel.place(x=100, y=200)
#miLabel.pack()

root.mainloop()