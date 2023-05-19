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
        consulta = f"Consulta por departamento\nFecha inicio: {fecha_inicio}\nFecha fin: {fecha_fin}"
        modulo.departamentos(fecha_fin, fecha_inicio)

    elif opcion_seleccionada == "Subcategoría":
        # Realizar la consulta por subcategoría
        consulta = f"Consulta por subcategoría\nFecha inicio: {fecha_inicio}\nFecha fin: {fecha_fin}"
        modulo.categorias(fecha_fin, fecha_inicio)

    elif opcion_seleccionada == "Prioridad":
        # Realizar la consulta por subcategoría
        consulta = f"Consulta por subcategoría\nFecha inicio: {fecha_inicio}\nFecha fin: {fecha_fin}"
        modulo.prioridad(fecha_fin, fecha_inicio)

    else:
        # No se seleccionó ninguna opción
        messagebox.showwarning("Error", "Selecciona una opción válida")
        return

modulo = C_Tickets()

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz de Consulta")
window.geometry("400x300")

# Cargar y mostrar la imagen en la parte superior derecha
image = Image.open("camenQ.png")
image = image.resize((100, 100))  # Ajusta el tamaño de la imagen según tus necesidades
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image_tk)
image_label.pack(anchor=tk.NE)

# Radio buttons para seleccionar la opción
opcion_var = tk.StringVar()
opcion_var.set("Departamento")

departamento_radio = tk.Radiobutton(window, text="Departamento", variable=opcion_var, value="Departamento")
departamento_radio.pack()

subcategoria_radio = tk.Radiobutton(window, text="Subcategoría", variable=opcion_var, value="Subcategoría")
subcategoria_radio.pack()

prioridad_radio = tk.Radiobutton(window, text="Prioridad", variable=opcion_var, value="Prioridad")
prioridad_radio.pack()

# Campos de fecha con calendarios emergentes
fecha_inicio_label = tk.Label(window, text="Fecha de inicio:")
fecha_inicio_label.pack()

fecha_inicio_cal = DateEntry(window, date_pattern="yyyy/mm/dd")
fecha_inicio_cal.pack()

fecha_fin_label = tk.Label(window, text="Fecha de fin:")
fecha_fin_label.pack()

fecha_fin_cal = DateEntry(window, date_pattern="yyyy/mm/dd")
fecha_fin_cal.pack()

# Botón de consulta
consulta_button = tk.Button(window, text="Consultar", command=consultar)
consulta_button.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()
