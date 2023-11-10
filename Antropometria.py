#UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO
#FACULTAD DE ESTUDIOS SUPERIORES ARAGON
#INGENIERIA EN COMPUTACION
#CRUZ JUAREZ EZEQUIEL AMADO
#SISTEMAS EXPERTOS
import sys
#GUI
#Importacion del modulo y componentes de tkinter
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from tkinter.font import Font
from  Paciente import Paciente
from  Paciente import Paciente_salud
def harris_benedict(paciente:Paciente):
    if paciente.sexo == 'm':
        geb = 655.1 + (9.563*paciente.peso_actual) + (1.849*paciente.talla_cm) - (4.67*paciente.edad)
    else:
        geb = 66.47 + (13.75 * paciente.peso_actual) + (5 * paciente.talla_cm) - (6.75 * paciente.edad)
    requerimiento_calorico = geb + (geb * .1) + paciente.frecuencia_actividad
    return requerimiento_calorico
paciente1 = Paciente(72,1.82,16,25,21,'h',30)
print(harris_benedict(paciente1))
def tipo_dieta_deseada(objetivo:str,paciente:Paciente):
    if objetivo == 'bajar de peso':
        dieta = 'baja en carbohidratos'
    else:
        if paciente.frecuencia_actividad >= 40:
            dieta = 'alta en carbohidratos'
        else:
            dieta = 'regular' #Distribucion equitativa
def ventana_inicial():
    # Creamos un objeto la clase Tk
    ventana_inicial = tk.Tk()
    # Estilos de los elementos
    font_size = Font(family='Roboto Cn', size=12)
    # Modificamos el tamaño de la ventana
    ventana_inicial.geometry('800x600')
    # Cambiamos el nombre de la ventana
    ventana_inicial.title('INICIO - RECOPILACION DE DATOS DEL PACIENTE')
    # Configuramos el icono de la ventana
    ventana_inicial.iconbitmap('../eze_icon.ico')
    # Configuramos el grid

    # Width es la cantidad de caracteres que ocupa el textbox
    txt_edad = ttk.Entry(ventana_inicial, width=30, font=font_size, )
    txt_edad.grid(row=0, column=1, sticky='W', pady=10)
    txt_edad.insert(0, '21')
    # Etiqueta  edad (label)
    lbl_edad = tk.Label(ventana_inicial, text='Introduce tu edad (Ej. 21):', font=font_size)
    lbl_edad.grid(row=0, column=0, pady=10, sticky='W')
    # Text box peso
    txt_peso = ttk.Entry(ventana_inicial, width=30, font=font_size)
    txt_peso.grid(row=1, column=1, pady=10)
    txt_peso.insert(0, '71.6')
    # Etiqueta peso
    lbl_peso = tk.Label(ventana_inicial, text='Ingresa tu peso en kg (Ej. 71.6):', font=font_size)
    lbl_peso.grid(row=1, column=0, sticky='W', pady=10)
    # Text box Talla
    txt_talla = ttk.Entry(ventana_inicial, width=30, font=font_size)
    txt_talla.grid(row=2, column=1, pady=10)
    txt_talla.insert(0, '1.82')
    # Etiqueta Talla
    lbl_talla = tk.Label(ventana_inicial, text='Ingresa tu altura en metros (Ej. 1.82):', font=font_size)
    lbl_talla.grid(row=2, column=0, sticky='W', pady=10)
    # Text box porcentaje de grasa
    txt_porcien_grasa = ttk.Entry(ventana_inicial, width=30, font=font_size)
    txt_porcien_grasa.grid(row=3, column=1, pady=10)
    txt_porcien_grasa.insert(0, '16')
    # Etiqueta porcentaje de grasa
    lbl_porcien_grasa = tk.Label(ventana_inicial, text='Ingresa tu porcentaje de grasa(Ej. 16):', font=font_size)
    lbl_porcien_grasa.grid(row=3, column=0, sticky='W', pady=10)
    # Text box indice cintura cadera
    txt_icc = ttk.Entry(ventana_inicial, width=30, font=font_size)
    txt_icc.grid(row=4, column=1, pady=10)
    txt_icc.insert(0, '1.74')
    # Etiqueta indice cintura cadera
    lbl_icc = tk.Label(ventana_inicial, text='Ingresa tu indice cintura cadera (Ej. 1.74):', font=font_size)
    lbl_icc.grid(row=4, column=0, sticky='W', pady=10)
    # Text box nivel de actividad fisica
    txt_actividad_fisica = ttk.Entry(ventana_inicial, width=30, font=font_size)
    txt_actividad_fisica.grid(row=5, column=1, pady=10)
    txt_actividad_fisica.insert(0, '30')
    # Etiqueta nivel de actividad fisica
    lbl_actividad_fisica = tk.Label(ventana_inicial, text='Ingresa tu nivel de actividad fisica  (Ej. 30):',
                                    font=font_size)
    lbl_actividad_fisica.grid(row=5, column=0, sticky='W', pady=10)
    # Text box sexo
    txt_sexo = ttk.Entry(ventana_inicial, width=30, font=font_size)
    txt_sexo.grid(row=6, column=1, pady=10)
    txt_sexo.insert(0, 'h')
    # Etiqueta sexo
    lbl_sexo = tk.Label(ventana_inicial, text='Ingresa tu sexo "m" para mujer y "h" para hombre  (Ej. h):',
                        font=font_size)
    lbl_sexo.grid(row=6, column=0, sticky='W', pady=10)

    # Creamos un metodo evento_click
    def enviar_informacion_paciente():
        # Recuperamos la informacion de los text box para inicializar nuestro objeto paciente
        print(txt_edad.get())
        peso = float(txt_peso.get())
        talla = float(txt_talla.get())
        porcien_grasa = int(txt_porcien_grasa.get()),
        icc = float(txt_icc.get())
        edad = int(txt_edad.get())
        sexo = txt_sexo.get()
        actividad_fisica = int(txt_actividad_fisica.get())
        nuevo_paciente = Paciente(peso, talla, porcien_grasa, icc, edad, sexo, actividad_fisica)
        mensaje1 = nuevo_paciente.__str__()
        messagebox.showinfo('DATOS DEL PACIENTE', mensaje1)
        print(nuevo_paciente)
        ventana_inicial.quit()
        ventana_inicial.destroy()
        ventana_padecimientos(nuevo_paciente)


    # Funcion para cerrar la ventana
    def salir():
        ventana_inicial.quit()
        ventana_inicial.destroy()
        print('Salimos...')
        sys.exit()

    def crear_menu():
        # Configurar el menu principal
        menu_principal = Menu(ventana_inicial)
        menu_principal.add_command(label='Salir', command=salir)
        # Mostramos el menu en la ventana principal
        ventana_inicial.config(menu=menu_principal)

    # N (arriba), E(derecha), S(abajo), W(izquierda)
    boton1 = tk.Button(ventana_inicial, text='Enviar', command=enviar_informacion_paciente, font=font_size)
    boton1.grid(row=7, column=2, padx=40, pady=40)
    crear_menu()
    # Iniciamos la ventana (esta linea se debe ejecutar al final)
    # Si se ejecuta antes, no se muestran los cambios anteriores
    ventana_inicial.mainloop()
def ventana_padecimientos(paciente:Paciente):
    # Creamos un objeto la clase Tk
    ventana_padecimientos = tk.Tk()
    # Estilos de los elementos
    font_size = Font(family='Roboto Cn', size=12)
    # Modificamos el tamaño de la ventana
    ventana_padecimientos.geometry('800x600')
    # Cambiamos el nombre de la ventana
    ventana_padecimientos.title('INICIO - RECOPILACION DE DATOS DEL PACIENTE')
    # Configuramos el icono de la ventana
    ventana_padecimientos.iconbitmap('../eze_icon.ico')
    # Configuramos el grid

    #Creamos una lista usando List comprhension
    datos = [x+1 for x in range(10)]
    combobox = ttk.Combobox(ventana_padecimientos,width=15,values= datos)
    combobox.grid(row=0,column=0,padx=10,pady=10)

    # Creamos un metodo evento_click
    def enviar_informacion_paciente():
        print('hola')

    # Funcion para cerrar la ventana
    def salir():
        ventana_padecimientos.quit()
        ventana_padecimientos.destroy()
        print('Salimos...')
        sys.exit()

    def crear_menu():
        # Configurar el menu principal
        menu_principal = Menu(ventana_padecimientos)
        menu_principal.add_command(label='Salir', command=salir)
        # Mostramos el menu en la ventana principal
        ventana_padecimientos.config(menu=menu_principal)

    # N (arriba), E(derecha), S(abajo), W(izquierda)
    boton1 = tk.Button(ventana_padecimientos, text='Enviar', command=enviar_informacion_paciente, font=font_size)
    boton1.grid(row=7, column=2, padx=40, pady=40)
    crear_menu()
    # Iniciamos la ventana (esta linea se debe ejecutar al final)
    # Si se ejecuta antes, no se muestran los cambios anteriores
    ventana_padecimientos.mainloop()