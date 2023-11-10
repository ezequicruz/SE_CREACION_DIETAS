class Paciente():
    def __init__(self,peso_actual:float,talla:float,porcentaje_grasa:int,indice_cintura_cadera:float,edad:int,sexo:str,frecuencia_actividad:int):
        self.peso_actual: float = peso_actual
        self.talla_metros: float = talla
        self.talla_cm:int = int(self.talla_metros * 100)
        self.porcentaje_grasa: int = porcentaje_grasa
        self.indice_cintura_cadera:float = indice_cintura_cadera
        self.edad:int = edad
        self.imc: float = round(self.peso_actual / (self.talla_metros * self.talla_metros),1) #Calculo del imc peso /(altura * altura)
        self.sexo:str = sexo #h para hombre y m para mujer
        self.frecuencia_actividad = frecuencia_actividad # 10 poco activo a 50 atleta de alto rendimiento
    def __str__(self):
        return f'Peso actual: {self.peso_actual}kg | Talla: {self.talla_metros}m | %Grasa: {self.porcentaje_grasa} | ICC: {self.indice_cintura_cadera} | IMC: {self.imc} | Edad: {self.edad} | Sexo {self.sexo}'


class Paciente_salud(Paciente):
    def __init__(self,peso_actual:float,talla:float,porcentaje_grasa:int,indice_cintura_cadera:float,edad:int,sexo:str,frecuencia_actividad:int,diabetes:bool,hipertension:bool,obesidad:bool,enfer_renal:bool,tiroides:bool,cancer:bool,problemas_cardiacos:bool,anorexia_bulimia:bool):
        super.__init__(peso_actual,talla,porcentaje_grasa,indice_cintura_cadera,edad,sexo,frecuencia_actividad)
        self.diabetes = diabetes
        self.hipertension = hipertension
        self.obesidad = obesidad
        self.enfer_renal = enfer_renal
        self.tiroides = tiroides
        self.cancer = cancer
        self.problemas_caridacos = problemas_cardiacos
        self.anorexia_bulimia = anorexia_bulimia
    def __str__(self):
        return f'{super.__str__(self)} | Diabetes: {self.diabetes} | Hipertension: {self.hipertension} | Obesidad: {self.obesidad} | Enfermedad renal: {self.enfer_renal} | Tiroides: {self.tiroides} | Cancer: {self.cancer} | Problemas cardiacos: {self.problemas_caridacos} | Anorexia o bulimia: {self.anorexia_bulimia}'


