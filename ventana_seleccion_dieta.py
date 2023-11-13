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
extras_dieta = []
sugerencias_observaciones = ''
def ventana_seleccion_dieta(paciente_salud: Paciente_salud, requerimiento_calorico):
    global requerimiento_paciente, extras_dieta, sugerencias_observaciones

    # Creamos un objeto la clase Tk
    ventana = tk.Tk()
    # Estilos de los elementos
    font_size = Font(family='Roboto Cn', size=12)
    # Modificamos el tamaño de la ventana
    ventana.attributes("-fullscreen",True)
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
        lbl_dieta.config(text=f'Requerimiento calculado: {requerimiento_calorico} kcal\n'
                              f'Requerimiento relativo: {requerimiento_paciente.requerimiento}\n'
                              f'Puntos de equivalentes:\n'
                              f'Cereal {requerimiento_paciente.cereal[0]}\n'
                              f'Leche {requerimiento_paciente.leche[0]}\n'
                              f'POA {requerimiento_paciente.poa[0]}\n'
                              f'Leguminosas {requerimiento_paciente.leguminosas[0]}\n'
                              f'Fruta {requerimiento_paciente.fruta[0]}\n'
                              f'Verdura {requerimiento_paciente.verduras[0]}\n'
                              f'Grasa {requerimiento_paciente.grasa[0]}\n'
                              f'Azucar {requerimiento_paciente.azucar[0]}\n\n'
                              f'NOTA IMPORTANTE: EN NINGUN MOMENTO ESTE ES UN DIAGNOSTICO OFICIAL\nCONSULTE UN ESPECIALISTA PARA UN DIAGNOSTICO VALIDO')

    def command_tiroides(): #Lectura de los radio button si el paciente tiene tiroides
        global requerimiento_paciente #Variable global para especificar el requerimiento calorico
        global extras_dieta #Variable global para especificar alguna especificacion en su dieta
        lbl_dieta_header.grid(row=4, column=0, columnspan=2, pady=10, sticky='W')
        lbl_dieta.grid(row=5, column=0, columnspan=2, pady=10, sticky='W')
        if seleccion_tiroides.get() == 1: #Si el paciente selecciona hipotiroidismo necesita una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')
            extras_dieta.append('alimentos ricos en yodo,')
        else: #Si el paciente selecciona hipertiroidismo necesita una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'RR')
            extras_dieta.append('alimentos ricos en yodo,')
            extras_dieta.append('alimentos sin sal')

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
        if paciente_salud.diabetes or paciente_salud.obesidad:  # Si el paciente tiene obesidad o diabetes necesita una dieta baja en carbohidratos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')
            extras_dieta.append('revisar perfil de lipidos,')
            if paciente_salud.diabetes:
                extras_dieta.append('revisar niveles de glucosa,')
                extras_dieta.append('rico en anitoxidantes,')
            if paciente_salud.obesidad:
                extras_dieta.append('revisar presion arterial')
        if paciente_salud.hipertension or paciente_salud.enfer_renal or paciente_salud.problemas_caridacos:  # Si el paciente sufre, hipertension, enfermedades renales o problemas cardiacos
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')      # necesita una dieta baja en carbohidratos
            extras_dieta.append('alimentos sin sal,') #Como indicacion extra no debe consumir sal en sus comidas
            if paciente_salud.problemas_caridacos: # Si especificamente el paciente sufre de problemas cardiacos debe consumir alimentos ricos en colesterol
                extras_dieta.append('alimentos bajos en carbohidratos,')
                extras_dieta.append('alimentos bajos en grasas,')
            if paciente_salud.enfer_renal: # Si especificamente el paciente sufre de enfermedades renales debe consumir alimentos sin azucar
                extras_dieta.append('alimentos sin proteina animal,')
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
        if paciente_salud.anemia:
            if paciente_salud.obesidad:
                requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'LC')
                extras_dieta.append('alimentos ricos en hierro,')
                extras_dieta.append('alimentos bajos en grasas,')
            else:
                requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'RR')
                extras_dieta.append('alimentos ricos en hierro,')
                extras_dieta.append('acido folico,')
                extras_dieta.append('vitaminas,')
        if paciente_salud.cancer or paciente_salud.anorexia_bulimia: #Si el paciente sufre cancer, anorexia o bulimia necesita una dieta Alto en Proteina
            requerimiento_paciente = Requerimiento_calorico(requerimiento_calorico, 'AP')
            if paciente_salud.anorexia_bulimia: #Si el paciente sufre anorexia o bulimia necesitan tomar suplementos y vitaminas
                extras_dieta.append('suplementos y vitaminas,')
            if paciente_salud.cancer:
                extras_dieta.append('rico en proteinas,')
                extras_dieta.append('rico en anitoxidantes,')
                extras_dieta.append('alimentos sin sal,')
                extras_dieta.append('alimentos bajos en grasas,')
                extras_dieta.append('suplementos y vitaminas,')




    # Creamos un metodo evento_click
    def enviar_informacion_paciente():
        global requerimiento_paciente, sugerencias_observaciones
        sugerencias_observaciones = ''
        for sugerencia in extras_dieta:
            if not (sugerencia in sugerencias_observaciones):
                sugerencias_observaciones += sugerencia
        if paciente_salud.tiroides: #Mostramos en una etiqueta la informacion
            lbl_dieta.config(text=f'Requerimiento calculado: {requerimiento_calorico}\n'
                                  f'Requerimiento relativo: {requerimiento_paciente.requerimiento}\n'
                                  f'Puntos de equivalentes:\n'
                                  f'Cereal {requerimiento_paciente.cereal[0]}\n'
                                  f'Leche {requerimiento_paciente.leche[0]}\n'
                                  f'POA {requerimiento_paciente.poa[0]}\n'
                                  f'Leguminosas {requerimiento_paciente.leguminosas[0]}\n'
                                  f'Fruta {requerimiento_paciente.fruta[0]}\n'
                                  f'Verdura {requerimiento_paciente.verduras[0]}\n'
                                  f'Grasa {requerimiento_paciente.grasa[0]}\n'
                                  f'Azucar {requerimiento_paciente.azucar[0]}\n\n'
                                  f'Observaciones: {sugerencias_observaciones}\n\n'
                                  f'NOTA IMPORTANTE: EN NINGUN MOMENTO ESTE ES UN DIAGNOSTICO OFICIAL,\nCONSULTE UN ESPECIALISTA PARA UN DIAGNOSTICO VALIDO')
            print(extras_dieta)

    if not (paciente_salud.tiroides or paciente_salud.sano): #Mostramos en una etiqueta la informacion
        sugerencias_observaciones = ''
        for sugerencia in extras_dieta:
            if not (sugerencia in sugerencias_observaciones):
                sugerencias_observaciones += sugerencia
        lbl_dieta.config(text=f'Requerimiento calculado: {requerimiento_calorico} kcal\n'
                              f'Requerimiento relativo: {requerimiento_paciente.requerimiento}\n'
                              f'Puntos de equivalentes:\n'
                              f'Cereal {requerimiento_paciente.cereal[0]}\n'
                              f'Leche {requerimiento_paciente.leche[0]}\n'
                              f'POA {requerimiento_paciente.poa[0]}\n'
                              f'Leguminosas {requerimiento_paciente.leguminosas[0]}\n'
                              f'Fruta {requerimiento_paciente.fruta[0]}\n'
                              f'Verdura {requerimiento_paciente.verduras[0]}\n'
                              f'Grasa {requerimiento_paciente.grasa[0]}\n'
                              f'Azucar {requerimiento_paciente.azucar[0]}\n\n'
                              f'Observaciones: {sugerencias_observaciones}\n\n'
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
