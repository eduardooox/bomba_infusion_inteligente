import random

# ---------------------------
# Clase: BombaInfusionInteligente
# ---------------------------
class BombaInfusionInteligente:
    def __init__(self):
        self.__velocidad = 0 # ml/h
        self.__volumenRestante = 0  # ml
        self.__tipoInfusion = ""
        self.__estado = "Detenida"
        self.__umbralMaximo = 0
        self.__umbralMinimo = 0

    # Método para configurar la infusión
    def configurarInfusion(self, tipo, velocidad, volumen, umbralMin, umbralMax):
        if velocidad <= 0 or volumen <= 0 or umbralMin < 0 or umbralMax < 0:
            print("[ERROR] Parámetros inválidos: deben ser valores positivos.")
            return
        if umbralMin >= umbralMax:
            print("[ERROR] El umbral mínimo debe ser menor que el umbral máximo.")
            return
    
    # Método para iniciar la infusión
        self.__tipoInfusion = tipo
        self.__velocidad = velocidad
        self.__volumenRestante = volumen
        self.__umbralMinimo = umbralMin
        self.__umbralMaximo = umbralMax
        self.__actualizarEstado()
        print(f"[CONFIG] Infusión '{tipo}' configurada a {velocidad} ml/h.")

    # Método para iniciar la infusión
    def iniciar(self):
        if self.__estado != "Detenida":
            print("[INFO] La bomba ya está funcionando.")
        else:
            self.__estado = "Funcionando"
            print("[INICIO] Bomba iniciada.")

    # Método para detener la infusión
    def detener(self):   
        self.__estado = "Detenida"
        print("[DETENCIÓN] Bomba detenida.")

    # Método privado para actualizar el estado
    def __actualizarEstado(self):
        if self.__velocidad < self.__umbralMinimo or self.__velocidad > self.__umbralMaximo:
            self.__estado = "Alerta"
            print("[ALERTA] Velocidad fuera de rango seguro.")
        elif self.__volumenRestante <= 0:
            self.__estado = "Vacía"
            print("[ALERTA] Volumen agotado.")
        else:
            self.__estado = "Lista"

    # Método para ajustar la velocidad
    def ajustarVelocidad(self, nuevaVelocidad):
        print(f"[AJUSTE] Intentando ajustar velocidad a {nuevaVelocidad} ml/h...")
        if self.__umbralMinimo <= nuevaVelocidad <= self.__umbralMaximo:
            self.__velocidad = nuevaVelocidad
            self.__actualizarEstado()
            print("[OK] Velocidad ajustada.")
        else:
            print("[ERROR] Fuera de límites permitidos.")
 
    # Método para obtener información general
    def obtenerInformacion(self):
        return {
            "Tipo de infusión": (self.__tipoInfusion, ""),
            "Velocidad": (self.__velocidad, "ml/h"),
            "Volumen restante": (self.__volumenRestante, "ml"),
            "Estado": (self.__estado, ""),
            "Umbral mínimo": (self.__umbralMinimo, "ml/h"),
            "Umbral máximo": (self.__umbralMaximo, "ml/h")
        }

    def getVelocidad(self):
        return self.__velocidad

# ---------------------------
# Clase: SensorBiologico (abstracta)
# ---------------------------
class SensorBiologico:
    def __init__(self, tipo, unidad):
        self._valorActual = 0
        self._unidad = unidad
        self._tipo = tipo

    def leerValor(self):
        self._valorActual = random.uniform(0, 100)
        return self._valorActual

    def esCritico(self):
        return False

    def obtenerValor(self):
        return f"{self._valorActual:.2f} {self._unidad}"

    def getTipo(self):
        return self._tipo

    def getUnidad(self):
        return self._unidad

    def getValorActual(self):
        return self._valorActual

# ---------------------------
# Subclase: SensorGlucosa
# ---------------------------
class SensorGlucosa(SensorBiologico):
    def __init__(self):
        super().__init__("Glucosa", "mg/dL")
        self.__umbralHipoglucemia = 70
        self.__umbralHiperglucemia = 180

    def leerValor(self):
        self._valorActual = random.uniform(40, 220)
        return self._valorActual

    def esCritico(self):
        return self._valorActual < self.__umbralHipoglucemia or self._valorActual > self.__umbralHiperglucemia

    def clasificarEstado(self):
        if self._valorActual < self.__umbralHipoglucemia:
            return "Hipoglucemia"
        elif self._valorActual > self.__umbralHiperglucemia:
            return "Hiperglucemia"
        else:
            return "Normal"

    def necesitaInsulina(self):
        return self._valorActual > self.__umbralHiperglucemia

# ---------------------------
# Subclase: SensorFrecuenciaCardiaca
# ---------------------------
class SensorFrecuenciaCardiaca(SensorBiologico):
    def __init__(self):
        super().__init__("Frecuencia cardíaca", "bpm")
        self.__frecuenciaReposo = 60
        self.__frecuenciaMaxima = 100

    def leerValor(self):
        self._valorActual = random.randint(40, 150)
        return self._valorActual

    def esCritico(self):
        return self._valorActual < self.__frecuenciaReposo or self._valorActual > self.__frecuenciaMaxima

    def esBradicardia(self):
        return self._valorActual < self.__frecuenciaReposo

    def esTaquicardia(self):
        return self._valorActual > self.__frecuenciaMaxima

    def clasificarRitmo(self):
        if self.esBradicardia():
            return "Bradicardia"
        elif self.esTaquicardia():
            return "Taquicardia"
        else:
            return "Normal"

# ---------------------------
# Subclase: SensorPresionArterial
# ---------------------------
class SensorPresionArterial(SensorBiologico):
    def __init__(self):
        super().__init__("Presión arterial", "mmHg")
        self.__sistolica = 0
        self.__diastolica = 0
        self.__clasificacionOMS = ""

    def leerValor(self):
        self.__sistolica = random.randint(80, 160)
        self.__diastolica = random.randint(50, min(self.__sistolica - 10, 100))
        self._valorActual = self.__sistolica  # Valor principal para compatibilidad
        return self.__sistolica

    def esCritico(self):
        return self.__sistolica < 90 or self.__sistolica > 140

    def clasificarPresion(self):
        if self.__sistolica < 90:
            self.__clasificacionOMS = "Hipotensión"
        elif self.__sistolica <= 140:
            self.__clasificacionOMS = "Normal"
        else:
            self.__clasificacionOMS = "Hipertensión"
        return self.__clasificacionOMS

    def diferencial(self):
        valor_dif = self.__sistolica - self.__diastolica
        es_critico = valor_dif < 30 or valor_dif > 70
        return valor_dif, es_critico

# ---------------------------
# Clase: ControladorDosis
# ---------------------------
class ControladorDosis:
    def __init__(self, bomba, sensores):
        self.__bomba = bomba
        self.__sensores = sensores
        self.__historial = []

    def evaluarParametros(self):
        for sensor in self.__sensores:
            valor = sensor.leerValor()
            tipo = sensor.getTipo()
            unidad = sensor.getUnidad()

            if sensor.esCritico():
                mensaje = f"{tipo} crítico detectado: {valor:.2f} {unidad}"
                self.__generarAlerta(mensaje)
                self.detenerPorEmergencia()
                return

            if isinstance(sensor, SensorPresionArterial):
                diferencial, es_critico = sensor.diferencial()
                if es_critico:
                    mensaje = f"Diferencial de presión anormal: {diferencial:.2f} mmHg"
                    self.__generarAlerta(mensaje)
                    self.detenerPorEmergencia()
                    return
                else:
                    self.__historial.append(f"Diferencial de presión normal: {diferencial:.2f} mmHg")

            self.__historial.append(f"{tipo} estable: {valor:.2f} {unidad}")

    def ajustarDosisAutomaticamente(self): # Lógica adaptativa según los valores de sensores
        for sensor in self.__sensores:
            if isinstance(sensor, SensorGlucosa):
                valor = sensor.leerValor()
                velocidad_actual = self.__bomba.getVelocidad()
                if valor > 180:
                    self.__bomba.ajustarVelocidad(velocidad_actual + 5)
                    self.__historial.append("Aumento por hiperglucemia.")
                elif valor < 70:
                    self.__bomba.ajustarVelocidad(velocidad_actual - 5)
                    self.__historial.append("Reducción por hipoglucemia.")

    def detenerPorEmergencia(self):
        self.__bomba.detener()
        self.__historial.append("Emergencia: bomba detenida.")

    # Método privado 
    def __generarAlerta(self, mensaje): 
        print(f"[ALERTA] {mensaje}")
        self.__historial.append(f"Alerta generada: {mensaje}")

    def obtenerHistorial(self):
        return self.__historial

# ---------------------------
# Clase: Paciente
# ---------------------------
class Paciente:
    def __init__(self, nombre, edad, diagnostico):
        self.__nombre = nombre
        self.__edad = edad
        self.__diagnostico = diagnostico
        self.__sensores = []

    def vincularSensor(self, sensor):
        self.__sensores.append(sensor)
        print(f"[PACIENTE] Sensor {sensor.getTipo()} vinculado a {self.__nombre}.")

    def obtenerSensores(self):
        return self.__sensores

    def obtenerDatosFisiologicos(self):
        print(f"\n📊 Datos fisiológicos de {self.__nombre}:")
        for sensor in self.__sensores:
            valor = sensor.leerValor()
            tipo = sensor.getTipo()
            if tipo == "Presión arterial":
                dif, _ = sensor.diferencial()
                print(f"- {tipo}: {valor} mmHg ({sensor.clasificarPresion()}), Diferencial: {dif:.2f} mmHg")
            elif tipo == "Glucosa":
                print(f"- {tipo}: {valor:.2f} mg/dL ({sensor.clasificarEstado()})")
            elif tipo == "Frecuencia cardíaca":
                print(f"- {tipo}: {valor} bpm ({sensor.clasificarRitmo()})")
            else:
                print(f"- {tipo}: {valor}")

# ---------------------------
# SIMULACIÓN
# ---------------------------
print("=== SIMULACIÓN DE CONTROLADOR INTELIGENTE DE INFUSIÓN INTRAVENOSA ===")

# Crear paciente y sensores
paciente = Paciente("Juan Pérez", 65, "Diabetes tipo 2")
sensor_glucosa = SensorGlucosa()
sensor_frecuencia = SensorFrecuenciaCardiaca()
sensor_presion = SensorPresionArterial()

# Vincular sensores
paciente.vincularSensor(sensor_glucosa)
paciente.vincularSensor(sensor_frecuencia)
paciente.vincularSensor(sensor_presion)

# Obtener datos fisiológicos
paciente.obtenerDatosFisiologicos()

# Crear bomba y configurarla
bomba = BombaInfusionInteligente()
bomba.configurarInfusion(tipo="Insulina", velocidad=20, volumen=100, umbralMin=10, umbralMax=50)
bomba.iniciar()

# Crear controlador
controlador = ControladorDosis(bomba, paciente.obtenerSensores())
# Evaluar y ajustar
controlador.evaluarParametros()
controlador.ajustarDosisAutomaticamente()

# Mostrar historial
print("\n📋 Historial del controlador:")
for evento in controlador.obtenerHistorial():
    print(f"- {evento}")

# Mostrar estado final de la bomba
print("\n🩺 Estado final de la bomba:")
info_bomba = bomba.obtenerInformacion()
for clave, (valor, unidad) in info_bomba.items():
    print(f"- {clave}: {valor} {unidad}")