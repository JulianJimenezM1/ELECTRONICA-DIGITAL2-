# DODGER - Juego en ESP32 con OLED SSD1306

## Descripción

Proyecto de videojuego desarrollado en una ESP32 utilizando una pantalla OLED SSD1306 y MicroPython.

El jugador controla un personaje que debe esquivar obstáculos mientras la dificultad aumenta con el tiempo. El juego también incluye sonidos con buzzer, distintos modos de juego y control en tiempo real.

Este proyecto integra conceptos vistos en Electrónica Digital II como:

- GPIO
- I2C
- PWM
- Debounce
- Máquina de estados
- Temporización no bloqueante

---

## Hardware utilizado

- ESP32
- Pantalla OLED SSD1306 (128x64)
- 3 Pulsadores
- Buzzer pasivo
- LED
- Resistencias y protoboard

---

## Controles

- UP → mover arriba
- DOWN → mover abajo
- START → iniciar o pausar el juego

---

## Modos de juego

### Clásico

Sobrevive el mayor tiempo posible evitando obstáculos.

### Tiempo

El jugador debe sobrevivir durante 60 segundos.

### Hardcore

- Mayor velocidad
- Más obstáculos
- Sistema de disparos

---

## Tecnologías utilizadas

### I2C

Comunicación utilizada para controlar la pantalla OLED.

Pines utilizados:

- SDA → GPIO 21
- SCL → GPIO 22

### PWM

Utilizado para generar sonidos en el buzzer.

### Temporización

Se utilizaron:

- ticks_ms()
- ticks_diff()
- ticks_add()

Esto permite ejecutar múltiples tareas sin bloquear el programa.

---

## Elementos mostrados en pantalla

- Menú principal
- Jugador
- Obstáculos
- Disparos
- Puntaje
- Tiempo de juego

---

## Archivos principales

- main.py
- ssd1306.py

---

## Características implementadas

- Lectura de botones
- Debounce por software
- Máquina de estados
- Generación aleatoria de obstáculos
- Detección de colisiones
- Renderizado gráfico en OLED
- Sonidos con PWM
- Programación no bloqueante

---

## Resultados

Se logró implementar un videojuego funcional en ESP32 con diferentes modos de juego y control en tiempo real.

El proyecto permitió integrar correctamente:

- Entradas digitales
- Comunicación I2C
- PWM
- Temporización
- Máquina de estados
- Renderizado gráfico en OLED

Además, el sistema funcionó de forma estable utilizando debounce y programación no bloqueante.
