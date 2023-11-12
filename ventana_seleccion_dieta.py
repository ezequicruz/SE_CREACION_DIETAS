# UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO
# FACULTAD DE ESTUDIOS SUPERIORES ARAGON
# INGENIERIA EN COMPUTACION
# CRUZ JUAREZ EZEQUIEL AMADO
# SISTEMAS EXPERTOS
import sys
# GUI
# Importacion del modulo y componentes de tkinter
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from tkinter.font import Font
from Paciente import Paciente, Paciente_salud
from tkinter import *
from LecturaJson import Requerimiento_calorico

requerimiento_paciente = None
def ventana_seleccion_dieta(paciente_salud: Paciente_salud, requerimiento_calorico):
    global requerimiento_paciente, extras_dieta

    # Creamos un objeto la clase Tk
    ventana = tk.Tk()
    # Estilos de los elementos
    font_size = Font(family='Roboto Cn', size=12)
    # Modificamos el tamaño de la ventana
    ventana.geometry('800x600')
    # Cambiamos el nombre de la ventana
    ventana.title('SELECCION DE DIETA')
    # Configuramos el icono de la ventana
    ventana.iconbitmap('../eze_icon.ico')
    # Configuramos el grid
    lbl_dieta_header = tk.Label(ventana, text='El tipo de dieta sugerido es:', font=font_size, justify=tk.LEFT)
    lbl_dieta = tk.Label(ventana, text='', font=font_size, justify=tk.LEFT)

    def command_sano(): #Lectura de los radio button si el paciente es sano
        lbl_dieta_header.grid(row=4, column=0, columnspan=2, pady=10, sticky='W')
        lbl_dieta.grid(row=5, column=0, columnspan=2, pady=10, sticky='W')
        global requerimiento_paciente #Variable global para especificar el requerimiento calorico
        if seleccion_sano.get() == 1: # Si el paciente selecciona bajar de peso tendra una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')
        else: # Si el paciente selecciona mantener peso tendra una dieta regular
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'RR')
        lbl_dieta.config(text=f'Requerimiento calculado: {requerimiento_calorico}\n'
                              f'Requerimiento relativo: {requerimiento_paciente.requerimiento}\n'
                              f'NOTA IMPORTANTE: EN NINGUN MOMENTO ESTE ES UN DIAGNOSTICO OFICIAL\nCONSULTE UN ESPECIALISTA PARA UN DIAGNOSTICO VALIDO')

    def command_tiroides(): #Lectura de los radio button si el paciente tiene tiroides
        global requerimiento_paciente #Variable global para especificar el requerimiento calorico
        global extras_dieta #Variable global para especificar alguna especificacion en su dieta
        lbl_dieta_header.grid(row=4, column=0, columnspan=2, pady=10, sticky='W')
        lbl_dieta.grid(row=5, column=0, columnspan=2, pady=10, sticky='W')
        if seleccion_tiroides.get() == 1: #Si el paciente selecciona hipotiroidismo necesita una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')
            extras_dieta = 'ricos en yodo,'
        else: #Si el paciente selecciona hipertiroidismo necesita una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'RR')
            extras_dieta = 'ricos en yodo,sin sal,'

    if paciente_salud.sano: # Si el paciente sano pregunta cual es su objetivo
        lbl_sano = tk.Label(ventana, text='Seleccione su objetivo', justify=tk.LEFT)
        lbl_sano.grid(row=0, column=0, sticky='W')
        seleccion_sano = IntVar()
        rbnBajar_peso = ttk.Radiobutton(ventana, text='Bajar peso', variable=seleccion_sano, command=command_sano,
                                        value=1)
        rbnBajar_peso.grid(row=1, column=1, sticky='W')
        rbnBajar_mantener = ttk.Radiobutton(ventana, text='Mantener peso', variable=seleccion_sano,
                                            command=command_sano, value=2)
        rbnBajar_mantener.grid(row=2, column=1, sticky='W')
    else: #Si el paciente no esta sano revisa que enfermedades tiene
        extras_dieta = ""
        if paciente_salud.diabetes or paciente_salud.obesidad:  # Si el paciente tiene obesidad o diabetes necesita una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')
        if paciente_salud.hipertension or paciente_salud.enfer_renal or paciente_salud.problemas_caridacos:  # Si el paciente sufre, hipertension, enfermedades renales o problemas cardiacos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')      # necesita una dieta baja en carbohidratos
            extras_dieta += 'sin sal,' #Como indicacion extra no debe consumir sal en sus comidas
            if paciente_salud.problemas_caridacos: # Si especificamente el paciente sufre de problemas cardiacos debe consumir alimentos ricos en colesterol
                extras_dieta += 'ricos en colesterol,'
            if paciente_salud.enfer_renal: # Si especificamente el paciente sufre de enfermedades renales debe consumir alimentos sin azucar
                extras_dieta += 'sin azucar,'
        if paciente_salud.tiroides:# Si el paciente sufre problemas de tiroides se le pregunta si es hipertiroidismo o hipotiroidismo
            lbl_tiroides = tk.Label(ventana, text='Seleccione el tipo de problemas de tiroides que tiene:',
                                    justify=tk.LEFT)
            lbl_tiroides.grid(row=0, column=0, sticky='W')
            seleccion_tiroides = IntVar()
            rbnHipotiroidismo = ttk.Radiobutton(ventana, text='Hipotiroidismo', variable=seleccion_tiroides,
                                                command=command_tiroides,
                                                value=1)
            rbnHipotiroidismo.grid(row=1, column=1, sticky='W')
            rbnHipertiroidismo = ttk.Radiobutton(ventana, text='Hipertiroidismo', variable=seleccion_tiroides,
                                                 command=command_tiroides, value=2)
            rbnHipertiroidismo.grid(row=2, column=1, sticky='W')
        if paciente_salud.cancer or paciente_salud.anorexia_bulimia: #Si el paciente sufre cancer, anorexia o bulimia necesita una dieta Alto en Proteina
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'AP')
            if paciente_salud.anorexia_bulimia: #Si el paciente sufre anorexia o bulimia necesitan tomar suplementos y vitaminas
                extras_dieta += 'Suplementos y vitaminas,'

    # Creamos un metodo evento_click
    def enviar_informacion_paciente():
        global requerimiento_paciente
        if paciente_salud.tiroides: #Mostramos en una etiqueta la informacion
            lbl_dieta.config(text=f'Requerimiento calculado: {requerimiento_calorico}\n'
                                  f'Requerimiento relativo: {requerimiento_paciente.requerimiento}\n'
                                  f'Recomendaciones: {extras_dieta}\n'
                                  f'NOTA IMPORTANTE: EN NINGUN MOMENTO ESTE ES UN DIAGNOSTICO OFICIAL,\nCONSULTE UN ESPECIALISTA PARA UN DIAGNOSTICO VALIDO')
            print(extras_dieta)

    if not (paciente_salud.tiroides or paciente_salud.sano): #Mostramos en una etiqueta la informacion
        lbl_dieta.config(text=f'Requerimiento calculado: {requerimiento_calorico} kcal\n'
                              f'Requerimiento relativo: {requerimiento_paciente.requerimiento}\n'
                              f'Recomendaciones: {extras_dieta}\n'
                              f'NOTA IMPORTANTE: EN NINGUN MOMENTO ESTE ES UN DIAGNOSTICO OFICIAL,\nCONSULTE UN ESPECIALISTA PARA UN DIAGNOSTICO VALIDO')

    # Funcion para cerrar la ventana
    def salir():
        ventana.quit()  # Cerramos la ventana
        ventana.destroy()  # Destruimos el objeto
        print('Salimos...')
        sys.exit()  # Cerramos desde el sistema la ventana

    def crear_menu():
        # Configurar el menu principal
        menu_principal = Menu(ventana)
        menu_principal.add_command(label='Salir', command=salir)
        # Mostramos el menu en la ventana principal
        ventana.config(menu=menu_principal)

    if paciente_salud.tiroides:
        # N (arriba), E(derecha), S(abajo), W(izquierda)
        boton1 = tk.Button(ventana, text='Enviar', command=enviar_informacion_paciente, font=font_size)
        boton1.grid(row=3, column=1, padx=40, pady=40)
    else:
        lbl_dieta_header.grid(row=3, column=0, pady=10, sticky='W')
        lbl_dieta.grid(row=4, column=0, columnspan=2, pady=10, sticky='W')
    crear_menu()
    # Iniciamos la ventana (esta linea se debe ejecutar al final)
    # Si se ejecuta antes, no se muestran los cambios anteriores
    ventana.mainloop()
