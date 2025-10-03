import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
boton_color = "#AEDFF7"
hover_color = "#9FD4F0"
texto_color = "#2B6CB0"
label_color = "#A0C4FF"

def animar_entry(entry, colores, index=0):
    entry.configure(border_color=colores[index])
    root.after(600, lambda: animar_entry(entry, colores, (index + 1) % len(colores)))

def gauss_jordan(tableau, pivot_row, pivot_col):
    pivot_val = tableau[pivot_row, pivot_col]
    tableau[pivot_row] /= pivot_val
    for i in range(tableau.shape[0]):
        if i != pivot_row:
            tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]
    return tableau
def mostrar_tabla(tabla, pivot_row=None, pivot_col=None, resultado=None):
    plt.figure(figsize=(5, 3))
    ax = sns.heatmap(tabla, annot=True, cmap="PuBuGn", cbar=False,
                     linewidths=0.5, linecolor='white', fmt=".2f")
