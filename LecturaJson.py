import json

with open("Recursos/Tabla_calorias_referencia.json", 'r') as tabla_referencia:
    datos = json.load(tabla_referencia)
    print(datos[0]['Cereal'])
    print(type(datos))


class Requerimiento_calorico(): #Clase para obtener la tabla de requerimiento calorico
    def __init__(self, require_cal: int, tipo_requirement: str):
        i = 0 #Variable auxiliar para obtener la tabla solicitada
        if require_cal < 1900: # Si el requerimiento es menor a 1900kcal usamos las tablas de 1800 kcal
            if tipo_requirement == 'LC': #Si el paciente necesita bajo en carbohidratos
                i = 0 #Tabla 1
            elif tipo_requirement == 'RR': #Si el paciente necesita una dieta regular
                i = 1 #Tabla 2
            else: #Si el paciente necesita Alto Proteico
                i = 2 # Tabla 3
        elif require_cal < 2000: # Si el requerimiento es menor a 2000 kcal usamos las tablas de 1900 kcal
            if tipo_requirement == 'RR': #Si el paciente necesita una dieta regular
                i = 3 # Tabla 4
            else: # Si el paciente necesita Bajo en carbohidratos
                i = 4 # Tabla 5
        elif require_cal < 2100: # Si el requerimiento es menor a 2100 kcal usamos las tablas de 2000 kcal
            if tipo_requirement == 'LC':#Si el paciente necesita una dieta bajo en carbohidratos
                i = 5 # Tabla 6
            else: # Si el paciente necesita Regular
                i = 6# Tabla 7
        elif require_cal < 2200: # Si el requerimiento es menor a 2200 kcal usamos las tablas de 2100 kcal
            if tipo_requirement == 'LC':#Si el paciente necesita una dieta bajo en carbohidratos
                i = 7 # Tabla 8
            else: # Si el paciente necesita Regular
                i = 8# Tabla 9
        #Apartir de este punto las dietas son hipercaloricas
        elif require_cal < 2300:# Si el requerimiento es menor a 2300 kcal usamos las tablas de 2200 kcal
            i = 9 # Tabla 10
        elif require_cal < 2400:# Si el requerimiento es menor a 2400 kcal usamos las tablas de 2300 kcal
            i = 10 # Tabla 11
        elif require_cal < 2500:# Si el requerimiento es menor a 2500 kcal usamos las tablas de 2400 kcal
            i = 11 # Tabla 12
        elif require_cal < 2600: # Si el requerimiento es menor a 2600 kcal usamos las tablas de 2500 kcal
            i = 12 # Tabla 13
        elif require_cal < 2700:# Si el requerimiento es menor a 2700 kcal usamos las tablas de 2600 kcal
            i = 13 # Tabla 14
        elif require_cal < 2800:# Si el requerimiento es menor a 2800 kcal usamos las tablas de 2700 kcal
            i = 14 # Tabla 16

        self.requerimiento = datos[i]['nombre']
        self.cereal = datos[i]['Cereal'].copy()
        self.leche = datos[i]['Leche'].copy()
        self.poa = datos[i]['POA'].copy()
        self.leguminosas = datos[i]['Leguminosas'].copy()
        self.fruta = datos[i]['Fruta'].copy()
        self.verduras = datos[i]['Verduras'].copy()
        self.grasa = datos[i]['Grasa'].copy()
        self.azucar = datos[i]['Azucares'].copy()
        self.porcien_calculado = datos[i]['%calculado'].copy()
        self.porcien_real = datos[i]['%real'].copy()

    def __str__(self):
        return (f'Requerimiento: {self.requerimiento} | Cereal: {self.cereal} | Leche: {self.leche} | POA: {self.poa}\n'
                f'Leguminosas: {self.leguminosas} | Fruta: {self.fruta} | Verduras: {self.verduras} | Grasa:{self.grasa}\n'
                f'Azucar: {self.azucar} | %Calculado: {self.porcien_calculado} | %Real: {self.porcien_real}')


requerimiento1 = Requerimiento_calorico(1800, 'AP')
print(requerimiento1)
