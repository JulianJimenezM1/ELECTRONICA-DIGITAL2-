Monitoreo de temperatura, humedad y movimiento con ESP32
Descripción del proyecto

Este proyecto trata de un sistema de monitoreo hecho con una ESP32. La idea principal es poder medir la temperatura y la humedad del ambiente usando un sensor DHT11, y tambien detectar movimiento con el sensor MPU6050.

El sistema muestra los datos en una pagina web local que se abre con la IP de la ESP32. Tambien se uso un bot de Telegram para consultar los valores y recibir alertas cuando algo esta fuera de lo normal.

Ademas, el proyecto tiene un buzzer que suena cuando se activa una alarma y un boton de panico que permite generar una alerta manual.

Componentes utilizados

ESP32
Sensor DHT11
Sensor MPU6050
Buzzer
Pulsador
Protoboard
Jumpers
Red WiFi
Celular con Telegram
Computador

Funcionamiento del sistema

Cuando se inicia el programa, la ESP32 se conecta a la red WiFi y luego empieza a leer los sensores. El DHT11 toma los valores de temperatura y humedad, mientras que el MPU6050 revisa si hay movimiento.

Los datos se pueden ver desde una pagina web. En esa pagina aparece la temperatura, la humedad, el estado de movimiento y el estado de la alarma. Tambien se pueden consultar algunos datos desde Telegram.

Si la temperatura o la humedad salen de los limites configurados, el sistema activa una alerta. Tambien se genera alerta cuando se detecta movimiento o cuando se presiona el boton de panico.

Variables que se monitorean

Temperatura
Humedad
Movimiento
Estado de alarma
Umbrales del sistema

Alertas del sistema

El sistema puede generar alertas por temperatura, humedad, movimiento, alerta combinada y boton de panico.

La alerta de temperatura se activa cuando el valor esta por encima o por debajo del rango permitido. La alerta de humedad funciona de la misma forma. La alerta combinada aparece cuando la temperatura y la humedad estan fuera de rango al mismo tiempo.

La alerta de movimiento se activa cuando el MPU6050 detecta movimiento, y la alerta de panico se activa cuando se presiona el pulsador.

Tipos de alertas

Alertas visuales: se muestran en la pagina web.

Alertas sonoras: se generan con el buzzer.

Alertas remotas: se envian por Telegram.

Comunicación

La ESP32 se conecta por WiFi para poder usar el servidor web y enviar mensajes por Telegram.

El bot de Telegram permite consultar datos como temperatura, humedad, movimiento y estado de alarma. Tambien envia mensajes automaticamente cuando ocurre una alerta.

Servidor web

El servidor web muestra los datos principales del sistema en tiempo real. Desde el navegador se puede revisar la temperatura, humedad, movimiento, estado de alarma y los umbrales configurados.

La pagina se actualiza automaticamente cada cierto tiempo para que los datos se mantengan actualizados.

Interfaz de usuario

El usuario puede revisar el sistema desde un navegador web usando la IP de la ESP32 o desde Telegram usando el bot. Esto hace que el monitoreo sea mas facil, ya que no es necesario estar conectado directamente al computador.

Estructura del codigo

El codigo esta dividido en varias partes: conexion WiFi, lectura del sensor DHT11, lectura del sensor MPU6050, deteccion de movimiento, manejo de alertas, envio de mensajes por Telegram, servidor web, buzzer y boton de panico.
