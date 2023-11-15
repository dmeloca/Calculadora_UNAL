import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
from module import seleccionar_plan, inscribir_materias_pensum, materiasVistas
# Cargar materias de Ciencias de la Computación desde un archivo pickle
with open('pensum_cc.pkl', 'rb') as archivo:
    materias_cc = pickle.load(archivo)

# Lista que mantendrá las materias seleccionadas junto con las notas
carreraNombre = ''
materias_vistas = []
creditos_totales_carrera = {
    "Ciencias de la Computacion": 139,
    "Matematicas": 140,
    "Estadistica": 141,
    "Ingenieria de Sistemas": 165
}
creditos_adicionales = 0
# Calcular el total de créditos de todas las materias
total_creditos = sum(materia['creditos'] for materia in materias_cc)


def agregar_nueva_materia():
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Nueva Materia")

    # Campos de entrada: nombre, créditos y nota
    tk.Label(ventana_agregar, text="Nombre:").pack(pady=2)
    nombre_var = tk.StringVar()
    entrada_nombre = ttk.Entry(ventana_agregar, textvariable=nombre_var)
    entrada_nombre.pack(pady=2)

    tk.Label(ventana_agregar, text="Créditos:").pack(pady=2)
    creditos_var = tk.IntVar()
    entrada_creditos = ttk.Entry(ventana_agregar, textvariable=creditos_var)
    entrada_creditos.pack(pady=2)

    tk.Label(ventana_agregar, text="Nota:").pack(pady=2)
    nota_var = tk.DoubleVar()
    entrada_nota = ttk.Entry(ventana_agregar, textvariable=nota_var)
    entrada_nota.pack(pady=2)

    # Función para guardar la nueva materia
    def guardar_materia():
        nombre = nombre_var.get().strip()
        creditos = creditos_var.get()
        nota = nota_var.get()
        # Crear ID único a partir del nombre en minúsculas y sin espacios
        id_materia = nombre.replace(" ", "").lower()
        nueva_materia = {'id': id_materia, 'nombre': nombre,
                         'creditos': creditos, 'nota': nota}
        if nueva_materia['nota'] < 3:
            nueva_materia['perdida'] = 1
        else:
            nueva_materia['perdida'] = 0
        # Aquí asumimos que quieres añadir la materia al pensum general
        materias_vistas.append(nueva_materia)
        ventana_agregar.destroy()
        actualizar_lista_seleccionadas()
        calcular_avance()
        calcular_promedio()
        print('carrera', carreraNombre)
        actualizar_creditos_adicionales(carreraNombre)

    # Botón para guardar la nueva materia
    ttk.Button(ventana_agregar, text="Guardar Materia",
               command=guardar_materia).pack(pady=10)
    # Poner el foco en el campo de entrada del nombre y esperar a que la ventana se cierre
    entrada_nombre.focus_set()


def ingresar_nota(materia):
    # Crear una ventana emergente
    ventana_nota = tk.Toplevel(root)
    ventana_nota.title(f"Ingresar Nota para {materia['nombre']}")
    tk.Label(ventana_nota, text=f"Ingrese la nota para {materia['nombre']}:", font=(
        'Calibri', 12)).pack(pady=10)

    # Campo de entrada para la nota
    nota_var = tk.StringVar()
    entrada_nota = ttk.Entry(
        ventana_nota, textvariable=nota_var, font=('Calibri', 12))
    entrada_nota.pack(pady=5)

    # Función para guardar la nota y cerrar la ventana emergente
    def guardar_nota():
        try:
            # Aquí se podría validar la nota antes de asignarla
            nota = float(nota_var.get())
            if nota < 3:
                materia['perdida'] = 1
            else:
                materia['perdida'] = 0
            materia['nota'] = nota
            ventana_nota.destroy()
            actualizar_lista_seleccionadas()
            calcular_avance()
            calcular_promedio()
            print('carrera', carreraNombre)
            actualizar_creditos_adicionales(carreraNombre)
        except ValueError:
            tk.messagebox.showerror(
                "Error", "Por favor ingrese un valor numérico para la nota.")
    # Botón para guardar la nota
    boton_guardar = ttk.Button(
        ventana_nota, text="Guardar Nota", command=guardar_nota)
    boton_guardar.pack(pady=20)

    # Pone el foco en el campo de entrada y espera a que la ventana se cierre
    entrada_nota.focus_set()


def agregar_materia_seleccionada(materia):
    for materia_seleccionada in materias_vistas:
        # and materia['perdida'] == 0:
        if materia_seleccionada['id'] == materia['id'] and materia_seleccionada['perdida'] == 0:
            return  # No agregar si la materia ya está seleccionada y la paso
    materia_con_nota = {
        'id': materia['id'], 'nombre': materia['nombre'], 'nota': None, 'creditos': materia['creditos']}
    ingresar_nota(materia_con_nota)
    materias_vistas.append(materia_con_nota)
    print('total creditos', total_creditos)
    # calcular_avance()
    # calcular_promedio()
    print(materias_vistas)


def mostrar_materias(nombre_carrera):
    # Ocultar el frame de las carreras
    global carreraNombre
    carreraNombre = nombre_carrera
    frame_carreras.pack_forget()
    # Limpiar el canvas y el frame de contenido
    carrera = seleccionar_plan(nombre_carrera)
    for widget in frame_materias.winfo_children():
        widget.destroy()
    # Centrar el título de la carrera en el frame de materias
    tk.Label(frame_materias, text=nombre_carrera, font=(
        'Calibri', 16, 'bold')).pack(anchor='center')

    # Actualizar el frame con las materias de la carrera seleccionada
    for materia in carrera:
        label_materia = tk.Label(frame_materias, text=materia['nombre'], font=(
            'Calibri', 12), relief='raised')
        label_materia.pack(anchor='center', pady=2)
        label_materia.bind('<Button-1>', lambda e,
                           m=materia: agregar_materia_seleccionada(m))

    # Actualizar el área scrollable del canvas
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))


def actualizar_lista_seleccionadas():
    # Limpiar el frame de materias seleccionadas
    for widget in frame_materias_seleccionadas.winfo_children():
        widget.destroy()

    # Añadir las materias seleccionadas con un cuadro de texto para la nota
    for materia in materias_vistas:
        row_frame = ttk.Frame(frame_materias_seleccionadas)
        row_frame.pack(fill='x', padx=5, pady=5)
        tk.Label(row_frame, text=materia['nombre'], font=(
            'Calibri', 12)).pack(side='left')
        ttk.Label(row_frame, text=materia['nota'], font=(
            'Calibri', 12)).pack(
            side='right')


# def actualizar_lista_seleccionadas():
#     # Limpiar el frame de materias seleccionadas
#     for widget in frame_materias_seleccionadas.winfo_children():
#         widget.destroy()

#     # Añadir las materias seleccionadas a la cuadrícula
#     for index, materia in enumerate(materias_vistas):
#         columna = index % 3
#         fila = index // 3
#         tk.Label(frame_materias_seleccionadas, text=materia['nombre'], font=(
#             'Calibri', 12)).grid(row=fila, column=columna, sticky='w', padx=5, pady=5)

#     # Actualizar el frame para que se ajuste a la cuadrícula
#     frame_materias_seleccionadas.pack(side='top', fill='x', expand=True)


def calcular_avance():
    creditos_cursados = sum(materia['creditos'] for materia in [
                            x for x in materias_vistas if x['perdida'] == 0])
    print('creditosss', creditos_cursados)
    porcentaje_avance = (creditos_cursados / total_creditos) * 100
    lbl_avance.config(text=f"Avance de la carrera: {porcentaje_avance:.2f}%")


def actualizar_creditos_adicionales(carrera):
    global creditos_adicionales

    creditos_adicionales = 0  # Reiniciar los créditos adicionales
    limite_creditos = creditos_totales_carrera[carrera] / 2

    for materia in materias_vistas:
        if materia.get('perdida', 0) == 1:
            # Restar los créditos de la materia si se perdió
            creditos_adicionales -= materia['creditos']
        else:
            # Aumentar los créditos de la materia si se pasó
            creditos_adicionales += materia['creditos'] * 2

    # No permitir que los créditos adicionales sobrepasen el límite
    creditos_adicionales = min(creditos_adicionales, limite_creditos)

    # Actualizar el label con el nuevo valor de créditos adicionales
    label_creditos_adicionales['text'] = f"Créditos adicionales: {creditos_adicionales}"


def calcular_promedio():
    total_notas = 0
    cantidad_materias = 0
    for materia in materias_vistas:
        try:
            nota = float(materia['nota'])
            total_notas += nota
            cantidad_materias += 1
        except ValueError:
            pass  # Ignorar si no es un número
    if cantidad_materias > 0:
        promedio = total_notas / cantidad_materias
        lbl_promedio.config(text=f"Promedio: {promedio:.2f}")
    else:
        lbl_promedio.config(
            text="Introduce notas válidas para calcular el promedio.")
# Función para actualizar los créditos adicionales
# ... (Tu función 'actualizar_creditos_adicionales') ...

# Función que se llama cuando se presiona el botón "OK"


def confirmar_creditos_cancelados():
    global creditos_adicionales
    try:
        # Convertir el texto ingresado en el cuadro a un número
        creditos_cancelados = float(entrada_creditos_cancelados.get())
        # Actualizar los créditos adicionales
        creditos_adicionales -= creditos_cancelados
        # Asegurarse de que no sean menores de cero
        creditos_adicionales = max(creditos_adicionales, 0)
        # Actualizar la etiqueta de créditos adicionales
        label_creditos_adicionales['text'] = f"Créditos adicionales: {creditos_adicionales}"
    except ValueError:
        messagebox.showerror(
            "Error", "Por favor ingrese un número válido de créditos cancelados.")


# Configuraciones iniciales
root = tk.Tk()
root.title("Calculadora UNAL - Doble Titulación")
root.geometry('800x600')  # Ajusta el tamaño de la ventana principal
# Estilos y configuraciones
style = ttk.Style()
style.configure("TButton", font=('Calibri', 12), padding=10)
style.configure("TLabel", font=('Calibri', 12), padding=10)
style.configure("TEntry", font=('Calibri', 12), padding=10)
# Frame para los botones de las carreras
frame_carreras = ttk.Frame(root)
frame_carreras.pack(side='top', fill='x', pady=20)
# Crear un canvas y una scrollbar para las materias
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Empaquetar la scrollbar y el canvas para las materias
scrollbar.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=True)
# Label para mostrar los créditos adicionales
label_creditos_adicionales = ttk.Label(root, text="Créditos adicionales: 0")
label_creditos_adicionales.pack(side='bottom')
# Frame para mostrar las materias dentro del canvas
frame_materias = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame_materias, anchor='nw')
# Botón para agregar nueva materia
boton_agregar_materia = ttk.Button(
    root, text="Agregar Materia", command=agregar_nueva_materia)
boton_agregar_materia.pack(side='bottom', pady=10)

# Frame para mostrar las materias seleccionadas y sus notas
frame_materias_seleccionadas = ttk.Frame(root)
frame_materias_seleccionadas.pack(side='bottom', fill='x', pady=20)
# Botón para calcular el promedio
# btn_calcular = ttk.Button(
#     root, text="Calcular Promedio", command=calcular_promedio)
# btn_calcular.pack(side='bottom', pady=5)

# Etiqueta para mostrar el promedio
lbl_promedio = ttk.Label(root, text="Promedio: 0", font=('Calibri', 14))
lbl_promedio.pack(side='bottom', pady=5)
# Etiqueta para mostrar el avance de la carrera
lbl_avance = ttk.Label(
    root, text="Avance de la carrera: 0%", font=('Calibri', 14))
lbl_avance.pack(side='bottom', pady=5)
# Cuadro de texto para los créditos cancelados
label_creditos_cancelados = ttk.Label(root, text="Créditos cancelados:")
label_creditos_cancelados.pack(side='bottom', pady=(5, 0))

entrada_creditos_cancelados = ttk.Entry(root)
entrada_creditos_cancelados.pack(side='bottom', pady=(0, 5))

# Botón "OK" para confirmar los créditos cancelados
boton_confirmar = ttk.Button(
    root, text="OK", command=confirmar_creditos_cancelados)
boton_confirmar.pack(side='bottom', pady=5)
# Información de las carreras y las materias
materias = {
    "Ciencias de la Computación": materias_cc,
    # ... otras carreras
}
carreras = {'Ciencias de la Computacion', 'Matematicas',
            'Estadistica', 'Ingenieria de Sistemas'}
# Botones para las carreras
# carreras = materias.keys()
for carrera in carreras:
    boton = ttk.Button(frame_carreras, text=carrera,
                       command=lambda c=carrera: mostrar_materias(c))
    boton.pack(side='left', padx=10)
boton = tk.Button(root, text="Haz clic en mí",
                  fg="white",
                  bg="blue",
                  activeforeground="yellow",
                  activebackground="green",
                  borderwidth=2,
                  relief="raised",
                  padx=10,
                  pady=5,
                  font=("Helvetica", 12, "bold"))
boton.pack(pady=10)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
