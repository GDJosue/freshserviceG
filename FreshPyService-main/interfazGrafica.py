import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from C_Tickets import *

def consultar():
    opcion_seleccionada = opcion_var.get()
    fecha_inicio = fecha_inicio_cal.get_date()
    fecha_fin = fecha_fin_cal.get_date()

    if opcion_seleccionada == "Departamento":
        # Realizar la consulta por departamento
        modulo.departamentos(fecha_fin, fecha_inicio)

    elif opcion_seleccionada == "Subcategoría":
        # Realizar la consulta por subcategoría
        modulo.categorias(fecha_fin, fecha_inicio)

    elif opcion_seleccionada == "Prioridad":
        # Realizar la consulta por subcategoría
        modulo.prioridad(fecha_fin, fecha_inicio)

    else:
        # No se seleccionó ninguna opción
        messagebox.showwarning("Error", "Selecciona una opción válida")
        return

modulo = C_Tickets()

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz de Consulta")
window.geometry("400x500")
window.configure(bg="#F7F7F7")

# Cargar y mostrar la imagen en el centro
image = Image.open("camenQ.png")
image = image.resize((100, 100))
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image_tk, bg="#F7F7F7")
image_label.pack(pady=(30, 10), anchor=tk.CENTER)

# Etiqueta de título
title_label = tk.Label(window, text="Consulta de Tickets", font=("Helvetica", 16), bg="#F7F7F7")
title_label.pack(pady=(0, 10))

# Marco para los radio buttons
radio_frame = tk.Frame(window, bg="#F7F7F7")
radio_frame.pack(pady=(0, 10))

opcion_var = tk.StringVar()
opcion_var.set("Departamento")

departamento_radio = tk.Radiobutton(radio_frame, text="Departamento", variable=opcion_var, value="Departamento",
                                    font=("Helvetica", 12), bg="#F7F7F7")
departamento_radio.pack(pady=5)

subcategoria_radio = tk.Radiobutton(radio_frame, text="Subcategoría", variable=opcion_var, value="Subcategoría",
                                    font=("Helvetica", 12), bg="#F7F7F7")
subcategoria_radio.pack(pady=5)

prioridad_radio = tk.Radiobutton(radio_frame, text="Prioridad", variable=opcion_var, value="Prioridad",
                                 font=("Helvetica", 12), bg="#F7F7F7")
prioridad_radio.pack(pady=5)

# Campos de fecha con calendarios emergentes
fecha_frame = tk.Frame(window, bg="#F7F7F7")
fecha_frame.pack(pady=(0, 10))

fecha_inicio_label = tk.Label(fecha_frame, text="Fecha de inicio:", font=("Helvetica", 12), bg="#F7F7F7")
fecha_inicio_label.grid(row=0, column=0, padx=(0, 10))

fecha_inicio_cal = DateEntry(fecha_frame, date_pattern="yyyy/mm/dd", font=("Helvetica", 12))
fecha_inicio_cal.grid(row=0, column=1)

fecha_fin_label = tk.Label(fecha_frame, text="Fecha de fin:", font=("Helvetica", 12), bg="#F7F7F7")
fecha_fin_label.grid(row=1, column=0, padx=(0, 10))

fecha_fin_cal = DateEntry(fecha_frame, date_pattern="yyyy/mm/dd", font=("Helvetica", 12))
fecha_fin_cal.grid(row=1, column=1)

# Botón de consulta
consulta_button = tk.Button(window, text="Consultar", command=consultar, font=("Helvetica", 14), bg="#4CAF50", fg="white")
consulta_button.pack(pady=(10, 0))

# Iniciar el bucle principal de la ventana
window.mainloop()

