import sys
from tkinter import *

# Config colors
bg_primary = "#212F3D"
bg_primary_ligth = "#34495E"
bg_secondary = "#8E44AD"
bg_white = "white"

# Make App
root = Tk()
# Added propieds for Application
root.title("Formularios")
root.configure(bg=bg_primary)
root.resizable(False, False)

# Config Vars uses
messageUser = StringVar()

def makeMessageToUser():
    messageUser.set('Hola, bienvenido: '+inputName.get()+' '+inputSurnames.get()+', ahora te podras Loggear con '+inputEmail.get())    

# Make Frame
frame = Frame(root, bg=bg_primary, width=450, height=600)
# Added propieds to Frame
frame.grid(row=0, column=0, padx=25, pady=25)

# Make Frame for Inputs
frameInputs = Frame(frame, bg=bg_primary, width=450, height=250)
# Added propieds to Frame Input
frameInputs.grid(row=1, column=0)

# Make Input Name
inputName = Entry(frameInputs, bg=bg_primary_ligth, fg=bg_white, font=("Arial", 14), border=0, width=32)
# Added propies to Input Name
inputName.grid(row=1, column=1, pady=3, ipady=5)

# Make Input Surnames
inputSurnames = Entry(frameInputs, bg=bg_primary_ligth, fg=bg_white, font=("Arial", 14), border=0, width=32)
# Added propies to Input Surnames
inputSurnames.grid(row=2, column=1, pady=3, ipady=5)

# Make Input Surnames
inputEmail = Entry(frameInputs, bg=bg_primary_ligth, fg=bg_white, font=("Arial", 14), border=0, width=32)
# Added propies to Input Surnames
inputEmail.grid(row=3, column=1, pady=3, ipady=5 )

# Make Frame Button
frameButtons = Frame(frame, width=450, height=100)
# Added propieds to Frame Button
frameButtons.grid(row=2, column=0, pady=5)

# Make Button 
button = Button(frameButtons, bg=bg_secondary, width=50, height=3, text="Mostrar datos", bd=0, fg=bg_white, command=makeMessageToUser)
# Added Propieds to Button
button.grid(row=0, column=0)

#Make Frame Labels 
frameLabel = Frame(frame, bg=bg_primary, width=450, height=150)
# Added Propieds to Frame
frameLabel.grid(row=3, column=0, pady=3)

#Make label 
label = Label(frameLabel, width=75, height=3, text="Hola!!", fg=bg_white, justify="center", bg=bg_primary, textvariable=messageUser)
# Added Propieds for Label
label.grid(row=0, column=0)

# Start Application
frame.mainloop()