# Cuna Multifuncional Inteligente con ESP32

## Descripción

En este proyecto se realizó una Cuna Multifuncional Inteligente utilizando un ESP32, sensores y actuadores para poder monitorear algunas condiciones del ambiente y también el estado del bebé.

El sistema permite revisar temperatura, humedad, luz, presencia del bebé y movimiento de la cuna. También cuenta con alarmas y algunos actuadores como ventilador, módulo Peltier y servo motor para ayudar a mantener mejores condiciones dentro de la cuna.

---

## Componentes del Sistema

### Entradas

* Sensor DHT11 para temperatura y humedad
* Sensor de luz
* Sensor MPU6050 para detectar movimiento
* Botón de presencia del bebé

### Procesamiento

* ESP32
* Lectura de sensores
* Revisión de temperatura y humedad
* Detección de luz
* Detección de movimiento
* Verificación de presencia
* Activación de alarmas
* Control de actuadores

### Salidas

* Ventilador
* Módulo Peltier
* Servo motor
* LED verde
* LED rojo
* Buzzer

---

## Funcionamiento del Sistema

### Presencia del Bebé

El sistema primero verifica si hay presencia del bebé en la cuna mediante un botón.

Cuando no hay presencia:

* Se apagan los actuadores.
* El sistema queda en espera.
* No se activan alarmas ni controles.

Cuando sí hay presencia:

* Se empieza a leer los sensores.
* Se revisan las condiciones del ambiente.
* Se activan las funciones de monitoreo.

---

### Temperatura y Humedad

El sensor DHT11 mide la temperatura y la humedad constantemente.

Si la temperatura está muy alta:

* Se prende el ventilador.
* Se activa el módulo Peltier.
* Se genera una alarma.

Si la humedad está fuera del rango normal:

* Se genera una alerta.
* El sistema indica que el ambiente no está en buenas condiciones.

---

### Iluminación

El sensor de luz permite saber si el ambiente está claro u oscuro.

El sistema puede detectar:

* Ambiente con luz.
* Ambiente oscuro.
* Cambios en la iluminación.

Esto sirve para saber si el espacio donde está el bebé es adecuado para descansar.

---

### Movimiento

El sensor MPU6050 detecta el movimiento de la cuna.

El sistema puede identificar:

* Cuna en reposo.
* Movimiento normal.
* Movimiento fuerte o brusco.

Cuando el movimiento supera el límite establecido:

* Se activa una alarma.
* Se prende el LED rojo.
* Suena el buzzer.
* El servo motor puede hacer un movimiento de balanceo.

---

## Sistema de Alarmas

Las alarmas se pueden generar por varias razones como:

* Temperatura alta.
* Humedad fuera del rango.
* Movimiento brusco.
* Cambios en la presencia del bebé.
* Varias condiciones al mismo tiempo.

Cuando hay una alarma:

* Se enciende el LED rojo.
* Se activa el buzzer.
* El sistema realiza la acción correspondiente.

---

## Indicadores Visuales

### LED Verde

El LED verde indica que el sistema está funcionando normal y que no hay ninguna alerta.

### LED Rojo

El LED rojo indica que existe una alarma o alguna condición que necesita atención.

---

## Actuadores

### Ventilador

Se activa cuando la temperatura sube para ayudar a ventilar la cuna.

### Módulo Peltier

Ayuda a bajar la temperatura cuando el ambiente está muy caliente.

### Servo Motor

Realiza un movimiento de balanceo cuando el sistema lo necesita.

### Buzzer

Emite un sonido cuando se presenta una alarma.

---

## Código

El código principal del proyecto se encuentra en:

```text
main.py
```

Incluye:

* Lectura del sensor DHT11.
* Lectura del sensor de luz.
* Lectura del MPU6050.
* Detección de presencia.
* Control del ventilador.
* Control del módulo Peltier.
* Control del servo motor.
* Activación de LEDs.
* Activación del buzzer.
* Sistema de alarmas.

---

## Evidencias

Las evidencias del proyecto se pueden guardar en una carpeta del repositorio.

Estas pueden incluir:

* Fotos del montaje.
* Videos del funcionamiento.
* Pruebas de sensores.
* Pruebas de actuadores.
* Capturas del código.

---

## Documentación

La documentación del proyecto incluye:

* Diagrama de bloques.
* Lista de materiales.
* Código del programa.
* Explicación del funcionamiento.
* Evidencias del proyecto.

---

## Resultados

Se logró desarrollar una Cuna Multifuncional Inteligente con ESP32.

El sistema puede monitorear temperatura, humedad, iluminación, presencia y movimiento. También puede activar alarmas y actuadores cuando detecta condiciones fuera de lo normal.

Este proyecto muestra cómo se pueden usar sensores, actuadores y un microcontrolador para crear un sistema de apoyo al cuidado del bebé.
