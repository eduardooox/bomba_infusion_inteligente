# 💉 Diseño POO de Controlador Inteligente de Infusión Intravenosa

Este proyecto simula una **bomba de infusión intravenosa inteligente**, capaz de adaptarse automáticamente a las condiciones fisiológicas de un paciente virtual. Utiliza sensores para medir glucosa, frecuencia cardíaca y presión arterial, y regula la administración de medicamentos en consecuencia.

---

## 📌 Descripción del problema

Se busca desarrollar un **sistema inteligente de infusión intravenosa** que controle en tiempo real la administración de medicamentos, adaptándose a parámetros fisiológicos del paciente obtenidos mediante sensores.

El sistema debe:
- Detectar valores fisiológicos críticos.
- Ajustar automáticamente la velocidad de infusión.
- Detener la bomba ante emergencias médicas.
- Mantener un historial de eventos.

---

## 🧠 Diseño basado en Programación Orientada a Objetos (POO)

Este proyecto está estructurado usando los cuatro pilares de la POO:

### 🔷 1. **Abstracción**
Se identificaron entidades clave del sistema:
- `Paciente`
- `SensorBiologico` (y sus subclases)
- `BombaInfusionInteligente`
- `ControladorDosis`

Cada clase contiene únicamente atributos y métodos esenciales para su funcionamiento, facilitando la comprensión del sistema.

---

### 🔷 2. **Encapsulamiento**

- **Atributos protegidos o privados** en todas las clases, evitando acceso directo desde fuera del objeto.
- Uso de métodos `getters` y `setters` solo donde es necesario para proteger la integridad de los datos.

#### ✅ Atributos encapsulados:
- Bomba: velocidad, volumen, estado, umbrales
- Sensores: tipo, unidad, valor
- Controlador: bomba, sensores, historial

#### ✅ Métodos encapsulados:
- `__actualizarEstado()` en `BombaInfusionInteligente`
- `__generarAlerta()` en `ControladorDosis`

---

### 🔷 3. **Herencia**

La clase abstracta `SensorBiologico` es la base de tres sensores especializados:

#### 🩸 `SensorGlucosa`
- **Nuevos atributos:** umbralHipoglucemia, umbralHiperglucemia
- **Nuevos métodos:** `clasificarEstado()`, `necesitaInsulina()`

#### ❤️ `SensorFrecuenciaCardiaca`
- **Nuevos atributos:** frecuenciaReposo, frecuenciaMaxima
- **Nuevos métodos:** `esBradicardia()`, `esTaquicardia()`, `clasificarRitmo()`

#### 💓 `SensorPresionArterial`
- **Nuevos atributos:** sistolica, diastolica, clasificacionOMS
- **Nuevos métodos:** `clasificarPresion()`, `diferencial()`

---

### 🔷 4. **Polimorfismo**

Se sobrescriben métodos de la clase base en cada sensor:

#### 🔄 `leerValor()`
- Genera datos fisiológicos distintos por sensor.
  - Glucosa: 40–220 mg/dL
  - Frecuencia cardíaca: 40–150 bpm
  - Presión arterial: sistólica y diastólica aleatoria

#### 🔄 `esCritico()`
- Lógica de evaluación crítica según cada tipo:
  - Glucosa: <70 o >180 mg/dL
  - Frecuencia cardíaca: <60 o >100 bpm
  - Presión sistólica: <90 o >140 mmHg

---

## 🧪 Simulación

Se realiza una prueba completa del sistema:
1. Se crea un paciente con tres sensores conectados.
2. Se obtienen sus datos fisiológicos.
3. Se configura e inicia la bomba.
4. El controlador analiza los datos y ajusta la infusión si es necesario.
5. Se muestra el historial de eventos y el estado final de la bomba.

---

## ⚙️ Estructura del sistema

```plaintext
📦 Proyecto
├── BombaInfusionInteligente
├── SensorBiologico (abstracta)
│   ├── SensorGlucosa
│   ├── SensorFrecuenciaCardiaca
│   └── SensorPresionArterial
├── ControladorDosis
└── Paciente