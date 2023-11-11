#Clase paciente para alamcenar los datos generales del paciente y sus medidas antropometricas
class Paciente():
    def __init__(self,peso_actual:float,talla:float,porcentaje_grasa:int,indice_cintura_cadera:float,edad:int,sexo:str,frecuencia_actividad:int):
        self.peso_actual: float = peso_actual #Peso actual del paciente en kg
        self.talla_metros: float = talla #Altura del paciente en metros
        self.talla_cm:int = int(self.talla_metros * 100) #Altura del paciente en cm
        self.porcentaje_grasa: int = porcentaje_grasa #Porcentaje de grasa corporal del paciente
        self.indice_cintura_cadera:float = indice_cintura_cadera # Ciircunferia de la cintura entre la cadera
        self.edad:int = edad #Edad del paciente
        self.imc: float = round(self.peso_actual / (self.talla_metros * self.talla_metros),1) #Calculo del imc peso /(altura * altura)
        self.sexo:str = sexo #h para hombre y m para mujer
        self.frecuencia_actividad = frecuencia_actividad # 10 poco activo a 50 atleta de alto rendimiento
    def __str__(self): #Sobreescritura del metodo str
        return f'Peso actual: {self.peso_actual}kg | Talla: {self.talla_metros}m | %Grasa: {self.porcentaje_grasa} | ICC: {self.indice_cintura_cadera} | IMC: {self.imc} | Edad: {self.edad} | Sexo {self.sexo}'

class Paciente_salud(Paciente): #Clase paciente salud, que hereda de paciente para agregar los padecimientos que este pueda tener
    def __init__(self,paciente:Paciente,diabetes:bool,hipertension:bool,obesidad:bool,enfer_renal:bool,tiroides:bool,cancer:bool,problemas_cardiacos:bool,anorexia_bulimia:bool):
        Paciente.__init__(self,paciente.peso_actual,paciente.talla_metros,paciente.porcentaje_grasa,paciente.indice_cintura_cadera,paciente.edad,paciente.sexo,paciente.frecuencia_actividad) #del objeto paciente, se inicializan los atributos en la clase padre
        self.diabetes = diabetes #True si el paciente tiene diabetes, False si no
        self.hipertension = hipertension #True si el paciente tiene hipertension, False si no
        self.obesidad = obesidad #True si el paciente tiene obesidad, False si no
        self.enfer_renal = enfer_renal #True si el paciente tiene enfermedades renales, False si no
        self.tiroides = tiroides #True si el paciente tiene padecimiento de tiroides ya sea hipertiroidismo o hipotiroidismo, False si no
        self.cancer = cancer #True si el paciente tiene cancer, False si no
        self.problemas_caridacos = problemas_cardiacos #True si el paciente tiene problemas cardiacos, False si no
        self.anorexia_bulimia = anorexia_bulimia ##True si el paciente tiene anorexia o bulimia, False si no
        self.sano = not (diabetes or hipertension or obesidad or enfer_renal or tiroides or cancer or problemas_cardiacos or anorexia_bulimia) #True si el paciente no tiene ningun padecimiento, False si cuenta con al menos uno
    def __str__(self): #Sobreescritura del metodo str
        return (f'{Paciente.__str__(self)}\nDiabetes: {self.diabetes} | Hipertension: {self.hipertension} | Obesidad: {self.obesidad} | Enfermedad renal: {self.enfer_renal} | Tiroides: {self.tiroides} | Cancer: {self.cancer} | Problemas cardiacos: {self.problemas_caridacos} | Anorexia o bulimia: {self.anorexia_bulimia}'
                f'\nSano:{self.sano}')


