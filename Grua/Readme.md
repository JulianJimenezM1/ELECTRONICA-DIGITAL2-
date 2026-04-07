# 🤖 Trabajo 2 - Grúa Robótica con ESP32

## 📌 Descripción
Este proyecto consiste en el diseño e implementación de una **grúa robótica de sobremesa con 2 grados de libertad (GDL)**, controlada mediante un microcontrolador **ESP32**.

El sistema permite el control manual mediante potenciómetros y la ejecución de **modos automáticos mediante interrupciones**, proporcionando un control preciso y en tiempo real.

---

## ⚙️ Componentes del Sistema

### 🔹 Entradas
- 🎛️ **2 Potenciómetros lineales:**
  - Rotación de la base  
  - Elevación del brazo  

- 🔘 **2 Pulsadores (con interrupciones):**
  - Retorno a posición inicial  
  - Activación de secuencia automática  

---

### 🔹 Procesamiento
- 🧠 **Microcontrolador:** ESP32  

- 📊 **Conversión ADC:**
  - Potenciómetro 1 → 12 bits  
  - Potenciómetro 2 → 10 bits  

- ⚡ **Procesamiento de señales:**
  - Escalamiento de valores analógicos  
  - Generación de PWM para servos  

- 🔄 **Control del sistema:**
  - Manejo de interrupciones  
  - Lógica de estados (manual / automático)  

---

### 🔹 Salidas
- ⚙️ **2 Servomotores:**
  - Servo 1 → Rotación de la base  
  - Servo 2 → Movimiento del brazo  

- 💡 **Indicadores:**
  - LED verde → Modo manual  
  - LED rojo → Modo automático  

- 🔊 **Buzzer:**
  - Alerta durante modo automático  

---

## 🔄 Funcionamiento del Sistema

### 🟢 Modo Manual
- Los potenciómetros generan señales analógicas proporcionales.  
- El ESP32 lee estas señales mediante el ADC.  
- Los valores se convierten a PWM para controlar los servos.  
- Permite control en tiempo real de la grúa.  

💡 **Indicador:** LED verde encendido  

---

### 🔴 Modo Automático – Retorno
- Se activa mediante un pulsador (interrupción).  
- El sistema:
  - Desactiva el control manual  
  - Lleva los servos a su posición inicial  

Durante este proceso:
- 🔴 LED rojo encendido  
- 🔊 Buzzer activo  

Al finalizar:
- Retorna al modo manual  

---

### 🔁 Modo Automático – Secuencia
- Activado mediante un segundo pulsador.  
- Ejecuta una rutina predefinida de movimientos.  

Durante la ejecución:
- 🔴 LED rojo encendido  
- 🔊 Buzzer activo  

Al finalizar:
- Vuelve automáticamente al modo manual  

---

## 💻 Código

El archivo principal del proyecto es:

```bash
main.py
