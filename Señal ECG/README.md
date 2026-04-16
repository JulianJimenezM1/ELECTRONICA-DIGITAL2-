Proyecto Actual

Sistema avanzado de adquisición y procesamiento de señal ECG

Implementación en ESP32 de un sistema capaz de capturar, procesar y analizar señales biomédicas en tiempo real, permitiendo mejorar la calidad de la señal mediante filtros digitales y visualizar su comportamiento para análisis posterior.

⚙️ Características principales
Adquisición de señal ECG en tiempo real mediante sensor analógico
Conversión analógica-digital (ADC) a 12 bits (0–4095)
Control de frecuencia de muestreo mediante Timer hardware
Implementación de filtros digitales:
Promedio móvil
Mediana
Exponencial (IIR)
Aplicación de filtros de forma individual o en cascada
Detección básica de latidos mediante umbral
Visualización de la señal en tiempo real (Serial Plotter)
Almacenamiento de datos en archivo .txt en la memoria del ESP32
Verificación de conexión de electrodos
Interfaz por consola para selección de filtros
