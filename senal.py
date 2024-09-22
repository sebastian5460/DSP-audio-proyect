import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def actualizar_grafica():
    t0 = t0_var.get()
    w = w_var.get()
    ciclo = ciclo_var.get()
    muestras = muestras_var.get()
    print(t0,w,ciclo,muestras)
    print(t0_var,w_var,ciclo_var,muestras_var)

    def fx(t):
        return np.sin(w * t)

    tn = ciclo * np.pi
    ti = np.linspace(t0, tn, muestras)
    senal = fx(ti)

    ax.clear()  # Limpiar la gráfica anterior
    ax.plot(ti, senal)
    ax.set_xlabel('t')
    ax.set_ylabel('Y')
    ax.axhline(0, color='green')
    ax.axvline(0, color='green')
    ax.grid()
    fig.canvas.draw()  # Dibujar la nueva gráfica

def obtener_valores():
    root = tk.Tk()
    root.title("Valores seno: ")

    global t0_var, w_var, ciclo_var, muestras_var
    t0_var = tk.IntVar()
    w_var = tk.DoubleVar()
    ciclo_var = tk.IntVar()
    muestras_var = tk.IntVar()

    tk.Label(root, text="Ingresa el valor de t0:").grid(row=0, column=0)
    tk.Entry(root, textvariable=t0_var).grid(row=0, column=1)

    tk.Label(root, text="Ingresa el valor de w:").grid(row=1, column=0)
    tk.Entry(root, textvariable=w_var).grid(row=1, column=1)

    tk.Label(root, text="Ingresa el ciclo final:").grid(row=2, column=0)
    tk.Entry(root, textvariable=ciclo_var).grid(row=2, column=1)

    tk.Label(root, text="Ingresa el número de muestras:").grid(row=3, column=0)
    tk.Entry(root, textvariable=muestras_var).grid(row=3, column=1)

    tk.Button(root, text="Actualizar", command=actualizar_grafica).grid(row=4, column=0)
    tk.Button(root, text="Salir", command=root.quit).grid(row=4, column=1)

    root.mainloop()

plt.ion()  # Activar modo interactivo
fig, ax = plt.subplots()

obtener_valores()

#plt.ioff()
#plt.show()