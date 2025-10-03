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
    highlight_color = "#B0DAE6"  
    border_color = '#2B6CB0'    
    if pivot_col is not None:
        for i in range(tabla.shape[0]):
            ax.add_patch(plt.Rectangle((pivot_col, i), 1, 1, fill=True,
                                       edgecolor=border_color, facecolor=highlight_color, lw=2))
    if pivot_row is not None:
        for j in range(tabla.shape[1]):
            ax.add_patch(plt.Rectangle((j, pivot_row), 1, 1, fill=True,
                                       edgecolor=border_color, facecolor=highlight_color, lw=2))

    if pivot_row is not None:
        plt.text(0, -0.5, f"🔴 Fila pivote: {pivot_row + 1}", fontsize=12, color=border_color)

    plt.title("Tabla Simplex ", fontsize=14, color=border_color)
    plt.tight_layout()
    plt.show()

    if resultado is not None:
        final_tabla = np.array([["x" + str(i+1) for i in range(len(resultado[0]))],
                                [f"{val:.2f}" for val in resultado[0]]])
        plt.figure(figsize=(4, 1.5))
        sns.heatmap(final_tabla, annot=True, fmt="", cmap="PuBuGn", cbar=False,
                    linewidths=0.5, linecolor='white')
        plt.title(f"Resultado óptimo: {resultado[1]:.2f}", fontsize=12, color=border_color)
        plt.tight_layout()
        plt.show()

