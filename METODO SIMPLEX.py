import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


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
        def simplex(c, A, b, tipo):
         m, n = A.shape
    if tipo == "min":
        c = -c

    tableau = np.hstack((A, np.eye(m), b.reshape(-1, 1)))
    tableau = np.vstack((tableau, np.hstack((-c, np.zeros(m + 1)))))

    while True:
        if (tableau[-1, :-1] >= 0).all():
            break

        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios <= 0] = np.inf
        pivot_row = np.argmin(ratios)

        tableau = gauss_jordan(tableau, pivot_row, pivot_col)
        mostrar_tabla(tableau, pivot_row, pivot_col)

    solution = np.zeros(n)
    for i in range(m):
        col = tableau[i, :n]
        if np.count_nonzero(col) == 1:
            idx = np.argmax(col)
            solution[idx] = tableau[i, -1]

    return solution, tableau[-1, -1]
def mostrar_instrucciones():
    texto = (
        "🧠 Cómo ingresar los datos:\n\n"
        "🔹 Función objetivo:\n"
        "Escribe solo los coeficientes separados por espacio.\n"
        "Ejemplo: 3 5  → para Z = 3x₁ + 5x₂\n\n"
        "🔹 Restricciones:\n"
        "Cada restricción se divide en:\n"
        "1. Coeficientes (Ej: 2 1)\n"
        "2. Término independiente (Ej: 10)\n"
        "Ejemplo: 2x₁ + x₂ ≤ 10 → escribe: 2 1 y luego 10\n\n"
        "❌ No uses letras, símbolos ni signos como ≤ o ="
    )
    messagebox.showinfo("Instrucciones", texto)
def resolver():
    try:
        tipo = tipo_var.get()
        num_vars = int(entry_vars.get())
        num_constraints = int(entry_constraints.get())

        c = np.array(list(map(float, entry_obj.get().split())))
        if len(c) != num_vars:
            raise ValueError("La cantidad de coeficientes no coincide con el número de variables.")

        A = []
        b = []

        for i in range(num_constraints):
            fila = list(map(float, entries_A[i].get().split()))
            if len(fila) != num_vars:
                raise ValueError(f"Restricción {i+1}: número de coeficientes incorrecto.")
            A.append(fila)
            b_val = float(entries_b[i].get())
            b.append(b_val)

        A = np.array(A)
        b = np.array(b)

        resultado = simplex(c, A, b, tipo)
        mostrar_tabla(np.array([]), resultado=resultado)
    except Exception as e:
        messagebox.showerror("Error", f"❌ Ocurrió un problema:\n{str(e)}\n\nVerifica que los datos estén bien escritos y que las cantidades coincidan.")
def crear_campos():
    global entries_A, entries_b, entry_obj
    for widget in frame_inputs.winfo_children():
        widget.destroy()
    try:
        num_vars = int(entry_vars.get())
        num_constraints = int(entry_constraints.get())

        ctk.CTkLabel(frame_inputs, text="🔹 Coeficientes de la función objetivo (x₁ x₂ ...):",
                     font=("Consolas", 14), text_color=label_color).pack()
        entry_obj = ctk.CTkEntry(frame_inputs, border_width=2, placeholder_text="Ejemplo: 3 5")
        entry_obj.pack(pady=5)
        animar_entry(entry_obj, ["#A3D9A5", "#C0EAC2", "#DFF5E1"])

        entries_A = []
        entries_b = []

        for i in range(num_constraints):
            ctk.CTkLabel(frame_inputs, text=f"🔸 Restricción {i+1} - Coeficientes (x₁ x₂ ...):",
                         font=("Consolas", 13), text_color=label_color).pack()
            e = ctk.CTkEntry(frame_inputs, border_width=2, placeholder_text="Ejemplo: 2 1")
            e.pack(pady=2)
            animar_entry(e, ["#E6F2FF", "#CCE5FF", "#DDEEFF"])
            entries_A.append(e)

            ctk.CTkLabel(frame_inputs, text=f"🔸 Restricción {i+1} - Término independiente:",
                         font=("Consolas", 13), text_color=label_color).pack()
            eb = ctk.CTkEntry(frame_inputs, border_width=2, placeholder_text="Ejemplo: 10")
            eb.pack(pady=2)
            animar_entry(eb, ["#E6F2FF", "#CCE5FF", "#DDEEFF"])
            entries_b.append(eb)
    except:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos para variables y restricciones.")

        
root = ctk.CTk()
root.title("🧮 Optimización con Simplex y Gauss-Jordan")
root.geometry("750x900")


ctk.CTkLabel(root, text="🎯 Tipo de problema (max/min):", font=("Arial Rounded MT Bold", 18),
             text_color=label_color).pack()
tipo_var = ctk.StringVar(value="max")
ctk.CTkEntry(root, textvariable=tipo_var, border_width=2, placeholder_text="max o min").pack(pady=5)