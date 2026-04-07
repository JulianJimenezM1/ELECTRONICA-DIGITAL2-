# 🤖 Trabajo 2 - Grúa Robótica con ESP32

## 📌 Descripción

Este proyecto consiste en el diseño e implementación de una **grúa robótica de sobremesa** con **2 grados de libertad (GDL)**, controlada mediante un microcontrolador **ESP32**.

El sistema permite el **control manual mediante potenciómetros** y cuenta con **modos automáticos activados por interrupciones**.

---

## ⚙️ Componentes del Sistema

### 🔹 Entradas

* 2 Potenciómetros:

  * Control de rotación de la base
  * Control de elevación del brazo
* 2 Pulsadores:

  * Retorno a posición inicial
  * Activación de secuencia automática

---

### 🔹 Procesamiento

* Microcontrolador **ESP32**
* Conversión ADC:

  * Potenciómetro 1: 12 bits
  * Potenciómetro 2: 10 bits
* Generación de señal PWM para servomotores
* Manejo de interrupciones
* Uso de variables de estado (modo manual / automático)

---

### 🔹 Salidas

* 2 Servomotores:

  * Servo 1: rotación de la base
  * Servo 2: movimiento del brazo
* LED verde: indica modo manual
* LED rojo: indica modo automático
* Buzzer: alerta durante el modo automático

---

## 🔄 Funcionamiento del Sistema

### 🟢 Modo Manual

Los potenciómetros controlan directamente el movimiento de los servos.
El sistema convierte la señal analógica a valores PWM, permitiendo control en tiempo real.
El **LED verde permanece encendido**.

---

### 🔴 Modo Automático - Retorno

Se activa mediante un pulsador con interrupción.
La grúa regresa automáticamente a su posición inicial.

Durante este proceso:

* Se enciende el LED rojo
* Se activa el buzzer

Al finalizar, el sistema vuelve al modo manual.

---

### 🔁 Modo Automático - Secuencia

Se ejecuta una rutina predefinida de movimientos.
El sistema opera de forma automática y, al finalizar, retorna al modo manual.

---

## 💻 Código

El código principal del proyecto se encuentra en:

```
main.py
```

Incluye:

* Lectura ADC
* Control PWM
* Manejo de interrupciones
* Lógica de estados



🚀 Proyecto desarrollado como parte de prácticas de sistemas embebidos.

