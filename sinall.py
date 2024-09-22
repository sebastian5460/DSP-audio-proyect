import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

def obtener_valores():
    
    root = tk.Tk()
    root.title("Entradas")

    
    t0_var = tk.IntVar()
    w_var = tk.DoubleVar()
    ciclo_var = tk.IntVar()
    muestras_var = tk.IntVar()

    # Crear y colocar las etiqeutas y cmpos de entrada
    tk.Label(root, text="Ingresa el valor de t0:").grid(row=0, column=0)
    tk.Entry(root, textvariable=t0_var).grid(row=0, column=1)

    tk.Label(root, text="Ingresa el valor de w:").grid(row=1, column=0)
    tk.Entry(root, textvariable=w_var).grid(row=1, column=1)

    tk.Label(root, text="Ingresa el ciclo final:").grid(row=2, column=0)
    tk.Entry(root, textvariable=ciclo_var).grid(row=2, column=1)

    tk.Label(root, text="Ingresa el número de muestras:").grid(row=3, column=0)
    tk.Entry(root, textvariable=muestras_var).grid(row=3, column=1)

    
    def submit():
        root.quit()
        root.destroy()

   
    tk.Button(root, text="Enviar", command=submit).grid(row=4, columnspan=2)

    
    root.mainloop()

    return t0_var.get(), w_var.get(), ciclo_var.get(), muestras_var.get()

t0, w, ciclo, muestras = obtener_valores()
tn=ciclo*np.pi
def fx(t):
    return np.sin(w*t)

ti=np.linspace(t0,tn,muestras)
senal= fx(ti)

plt.plot(ti,senal)
plt. xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()