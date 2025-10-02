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
Animación de color en campos de entrada
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