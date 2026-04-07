🤖 Trabajo 2 - Grúa Robótica con ESP32
📌 Descripción

Este proyecto consiste en el diseño e implementación de una grúa robótica de sobremesa con 2 grados de libertad (GDL), controlada mediante un microcontrolador ESP32.

El sistema permite el control manual a través de potenciómetros, así como la ejecución de modos automáticos mediante interrupciones, garantizando precisión, control y facilidad de uso.

⚙️ Componentes del Sistema
🔹 Entradas
2 Potenciómetros lineales:
Control de rotación de la base
Control de elevación del brazo
2 Pulsadores con interrupción:
Retorno automático a posición inicial
Activación de secuencia automática
🔹 Procesamiento
Microcontrolador ESP32
Conversión ADC:
Potenciómetro 1: resolución de 12 bits
Potenciómetro 2: resolución de 10 bits
Procesamiento de señales:
Escalamiento de valores analógicos a PWM
Generación de señales PWM para servomotores
Control del sistema:
Manejo de interrupciones
Implementación de lógica de estados (modo manual / automático)
🔹 Salidas
2 Servomotores:
Servo 1: rotación de la base
Servo 2: movimiento del brazo
Indicadores:
LED verde → modo manual
LED rojo → modo automático
Actuador sonoro:
Buzzer → alerta durante modos automáticos
🔄 Funcionamiento del Sistema
🟢 Modo Manual
Los potenciómetros generan señales analógicas proporcionales a su posición.
El ESP32 lee estos valores mediante el ADC.
Los datos se convierten a señales PWM que controlan los servos.
Se permite el control en tiempo real del sistema.

🔹 Indicador: LED verde encendido

🔴 Modo Automático – Retorno
Activado mediante un pulsador (interrupción).
El sistema:
Desactiva el control manual
Lleva los servos a su posición inicial de forma gradual

Durante este proceso:

LED rojo encendido
Buzzer activo

Al finalizar:

Regresa automáticamente al modo manual
🔁 Modo Automático – Secuencia
Se activa mediante un segundo pulsador.
Ejecuta una rutina preprogramada de movimientos de la grúa.

Durante la ejecución:

LED rojo encendido
Buzzer activo

Al finalizar:

El sistema vuelve al modo manual
💻 Código

El programa principal se encuentra en:

📄 main.py

Incluye:

Lectura de señales ADC
Generación de PWM
Manejo de interrupciones
Control de estados del sistema
🚀 Conclusión

Este proyecto permite integrar conceptos clave de sistemas embebidos como:

Conversión analógica-digital
Control de actuadores
Manejo de interrupciones
Diseño de sistemas en tiempo real

Logrando un sistema funcional, intuitivo y con aplicaciones en automatización básica.
