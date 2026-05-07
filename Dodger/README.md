DODGER - Juego en ESP32 con OLED SSD1306
Descripción

Proyecto de videojuego desarrollado en ESP32 utilizando una pantalla OLED SSD1306 y programado en MicroPython.

El jugador controla un personaje que debe esquivar obstáculos mientras aumenta la dificultad del juego. También incluye sonidos con buzzer, distintos modos de juego y control en tiempo real.

El proyecto integra conceptos de Electrónica Digital II como:

GPIO
I2C
PWM
Debounce
Máquina de estados
Temporización no bloqueante
Hardware utilizado
ESP32
Pantalla OLED SSD1306 (128x64)
3 Pulsadores
Buzzer pasivo
LED
Resistencias y protoboard
Funciones del juego
Controles
Botón UP → mover arriba
Botón DOWN → mover abajo
Botón START → iniciar/pausar juego
Modos de juego
Clásico

Sobrevive el mayor tiempo posible evitando obstáculos.

Tiempo

Debes sobrevivir durante 60 segundos.

Hardcore

Modo difícil con:

Mayor velocidad
Más obstáculos
Sistema de disparos
Tecnologías utilizadas
I2C

Se utiliza para controlar la pantalla OLED.

Pines utilizados
SDA → GPIO 21
SCL → GPIO 22
PWM

Utilizado para generar sonidos en el buzzer.

Temporización

El juego utiliza:

ticks_ms()
ticks_diff()
ticks_add()

Esto permite ejecutar varias tareas al mismo tiempo sin bloquear el programa.

Elementos mostrados en pantalla
Menú principal
Jugador
Obstáculos
Disparos
Puntaje
Tiempo
Archivos principales
main.py
ssd1306.py
Características implementadas
Lectura de botones
Debounce por software
Máquina de estados
Generación aleatoria de obstáculos
Detección de colisiones
Renderizado gráfico en OLED
Sonidos con PWM
Programación no bloqueante
Resultados

Se logró implementar un videojuego funcional en ESP32 con:

Control en tiempo real
Diferentes modos de juego
Sistema estable usando debounce
Integración de periféricos y comunicación I2C
Renderizado gráfico fluido en pantalla OLED
