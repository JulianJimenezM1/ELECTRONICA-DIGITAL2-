# DODGER - Juego en ESP32 con OLED SSD1306

## Descripción

Este proyecto consiste en un videojuego hecho con una ESP32 y una pantalla OLED SSD1306 usando MicroPython.

El juego trata de controlar un personaje para esquivar obstáculos que aparecen en la pantalla. También tiene sonidos con buzzer, diferentes modos de juego y aumento de dificultad mientras pasa el tiempo.

La idea del proyecto fue integrar varias cosas vistas en Electrónica Digital II como GPIO, I2C, PWM, debounce y máquinas de estado.

---

# Componentes del sistema

## Entradas

### Pulsadores

Se utilizaron 3 botones:

- Movimiento arriba
- Movimiento abajo
- Inicio / pausa del juego

---

## Procesamiento

### ESP32

La ESP32 es la encargada de controlar todo el sistema.

Funciones implementadas:

- Comunicación I2C
- Señales PWM
- Temporización en tiempo real
- Máquina de estados
- Debounce por software
- Generación aleatoria de obstáculos

---

## Salidas

### Pantalla OLED SSD1306

La pantalla muestra:

- Menú principal
- Jugador
- Obstáculos
- Disparos
- Puntaje
- Tiempo de juego

---

### Buzzer

Se utilizó un buzzer pasivo para generar sonidos usando PWM.

Se generan sonidos para:

- Navegación del menú
- Puntos
- Colisiones
- Inicio del juego

---

### LED

El LED funciona como indicador visual cuando ocurre una colisión o termina una partida.

---

# Funcionamiento del sistema

## Menú principal

El jugador puede seleccionar el modo de juego usando los botones UP y DOWN.

El botón START sirve para iniciar la partida.

---

## Modo clásico

El jugador debe sobrevivir el mayor tiempo posible esquivando obstáculos.

La dificultad aumenta poco a poco.

---

## Modo tiempo

El jugador debe sobrevivir durante 60 segundos para ganar.

---

## Modo hardcore

Es el modo más difícil.

Incluye:

- Mayor velocidad
- Más obstáculos
- Sistema de disparos

---

# Código

El código principal del proyecto está en:

main.py

El programa incluye:

- Lectura de botones
- Control PWM
- Manejo de estados
- Generación de obstáculos
- Detección de colisiones
- Renderizado gráfico en OLED

---

# Comunicación y control

## I2C

La comunicación I2C se utiliza para controlar la pantalla OLED SSD1306.

Pines utilizados:

- SDA → GPIO 21
- SCL → GPIO 22

---

## PWM

El PWM se utiliza para generar sonidos en el buzzer.

---

## Temporización

La temporización del juego fue implementada utilizando:

- ticks_ms()
- ticks_diff()
- ticks_add()

Esto permite que el juego funcione sin bloquear el programa mientras se ejecutan sonidos, movimiento y obstáculos al mismo tiempo.

---

# Librería SSD1306

Para controlar la pantalla OLED se utilizó una librería SSD1306 en MicroPython.

La librería maneja:

- Inicialización de pantalla
- Comunicación I2C
- Framebuffer
- Dibujo de texto y píxeles

También se utiliza framebuf para dibujar sprites y gráficos del juego.

---

# Resultados

Se logró implementar un videojuego funcional en ESP32 con diferentes modos de juego y control en tiempo real.

El proyecto permitió integrar correctamente:

- Entradas digitales
- Comunicación I2C
- PWM
- Temporización
- Máquina de estados
- Renderizado gráfico en OLED

Además, el sistema funcionó de forma estable usando debounce y programación no bloqueante.
