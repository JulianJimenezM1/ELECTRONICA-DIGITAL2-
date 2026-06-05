from machine import Pin, ADC, PWM, I2C 
import dht
import time
import struct
import math

# =========================
# PINES
# =========================

PIN_DHT = 4
PIN_LUZ = 34
PIN_BOTON = 18

PIN_VENTILADOR = 13
PIN_PELTIER = 16
PIN_SERVO = 23
PIN_LED_VERDE = 25
PIN_LED_ROJO = 26
PIN_BUZZER = 27

PIN_SDA = 21
PIN_SCL = 22

# =========================
# CONFIGURACION
# =========================

# Ventilador confirmado:
# 1 = prende
# 0 = apaga
VENTILADOR_ON = 1
VENTILADOR_OFF = 0

# Peltier
PELTIER_ON = 1
PELTIER_OFF = 0

# Bebé:
# Como lo cambiamos antes:
# 1 = hay bebé
# 0 = no hay bebé
# Si queda al revés, cambia este 1 por 0.
BEBE_CUANDO_BOTON = 1

# Temperatura
TEMP_ALTA = 25
TEMP_BAJA = 22

# Humedad
HUM_MIN = 35
HUM_MAX = 75

# Luz
UMBRAL_LUZ_OSCURA = 1200

# Movimiento MPU:
# En reposo la aceleracion total suele estar cerca de 1.0
# Si se mueve bastante, sube o baja.
UMBRAL_MOVIMIENTO = 0.25

# Servo
SERVO_CENTRO = 90
SERVO_IZQUIERDA = 60
SERVO_DERECHA = 120

# =========================
# SENSORES
# =========================

sensor_dht = dht.DHT11(Pin(PIN_DHT, Pin.IN, Pin.PULL_UP))

# Luz de 3 pines:
# S / OUT -> GPIO 34
# + / VCC -> 3.3V
# - / GND -> GND
pin_luz_digital = Pin(PIN_LUZ, Pin.IN)
sensor_luz = ADC(Pin(PIN_LUZ))
sensor_luz.atten(ADC.ATTN_11DB)

try:
    sensor_luz.width(ADC.WIDTH_12BIT)
except:
    pass

boton = Pin(PIN_BOTON, Pin.IN, Pin.PULL_UP)

# =========================
# ACTUADORES
# =========================

ventilador = Pin(PIN_VENTILADOR, Pin.OUT)
peltier = Pin(PIN_PELTIER, Pin.OUT)

led_verde = Pin(PIN_LED_VERDE, Pin.OUT)
led_rojo = Pin(PIN_LED_ROJO, Pin.OUT)

servo = PWM(Pin(PIN_SERVO))
servo.freq(50)

buzzer = PWM(Pin(PIN_BUZZER))
buzzer.freq(2000)
buzzer.duty(0)

# =========================
# MPU6050
# =========================

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.ok = False

        try:
            self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')
            time.sleep_ms(100)
            self.ok = True
            print("MPU6050 conectado")
        except Exception as e:
            print("MPU6050 no detectado:", e)
            self.ok = False

    def leer_aceleracion(self):
        if not self.ok:
            return None

        try:
            data = self.i2c.readfrom_mem(self.addr, 0x3B, 14)
            ax, ay, az, temp, gx, gy, gz = struct.unpack(">hhhhhhh", data)

            ax = ax / 16384
            ay = ay / 16384
            az = az / 16384

            aceleracion_total = math.sqrt(ax * ax + ay * ay + az * az)

            return aceleracion_total

        except Exception as e:
            print("Error MPU6050:", e)
            return None


i2c = I2C(0, scl=Pin(PIN_SCL), sda=Pin(PIN_SDA), freq=400000)
mpu = MPU6050(i2c)

# =========================
# FUNCIONES ACTUADORES
# =========================

def ventilador_on():
    ventilador.value(VENTILADOR_ON)


def ventilador_off():
    ventilador.value(VENTILADOR_OFF)


def peltier_on():
    peltier.value(PELTIER_ON)


def peltier_off():
    peltier.value(PELTIER_OFF)


def buzzer_off():
    buzzer.duty(0)


def beep(cantidad=1, duracion=150):
    for i in range(cantidad):
        buzzer.duty(512)
        time.sleep_ms(duracion)
        buzzer.duty(0)
        time.sleep_ms(120)


def mover_servo(angulo):
    angulo = max(0, min(180, angulo))

    # Servo ESP32 MicroPython:
    # 0 grados aprox = duty 26
    # 180 grados aprox = duty 128
    duty = int(26 + (angulo / 180) * (128 - 26))
    servo.duty(duty)


def servo_por_movimiento():
    print("Servo moviendose por movimiento del MPU")

    mover_servo(SERVO_IZQUIERDA)
    time.sleep_ms(350)

    mover_servo(SERVO_DERECHA)
    time.sleep_ms(350)

    mover_servo(SERVO_CENTRO)
    time.sleep_ms(300)


def todo_apagado():
    ventilador_off()
    peltier_off()
    buzzer_off()
    mover_servo(SERVO_CENTRO)


def led_normal():
    led_verde.value(1)
    led_rojo.value(0)


def led_alerta():
    led_verde.value(0)
    led_rojo.value(1)


# =========================
# FUNCIONES SENSORES
# =========================

def leer_dht():
    try:
        sensor_dht.measure()
        temperatura = sensor_dht.temperature()
        humedad = sensor_dht.humidity()
        return temperatura, humedad
    except Exception as e:
        print("Error DHT11:", e)
        return None, None


def leer_luz():
    try:
        luz_analogica = sensor_luz.read()
    except:
        luz_analogica = 0

    try:
        luz_digital = pin_luz_digital.value()
    except:
        luz_digital = -1

    return luz_analogica, luz_digital


def hay_bebe():
    valor = boton.value()

    if valor == BEBE_CUANDO_BOTON:
        return True, valor
    else:
        return False, valor


def detectar_movimiento(aceleracion):
    if aceleracion is None:
        return False

    diferencia = abs(aceleracion - 1.0)

    if diferencia >= UMBRAL_MOVIMIENTO:
        return True
    else:
        return False


# =========================
# INICIO
# =========================

print("Sistema de cuna inteligente iniciado")
print("Boton bebe en GPIO 18")
print("Valor", BEBE_CUANDO_BOTON, "= hay bebe en cuna")
print("Ventilador GPIO 13: 1 prende, 0 apaga")
print("Servo GPIO 23: se mueve SOLO si hay movimiento en MPU")
print("Luz GPIO 34: lectura analogica y digital")

todo_apagado()
led_verde.off()
led_rojo.off()

# =========================
# LOOP PRINCIPAL
# =========================

while True:
    print("")
    print("===== CUNA INTELIGENTE =====")

    bebe, valor_boton = hay_bebe()
    luz_analogica, luz_digital = leer_luz()
    temperatura, humedad = leer_dht()
    aceleracion = mpu.leer_aceleracion()

    print("Valor boton:", valor_boton)

    if bebe:
        print("Hay bebe en cuna")
    else:
        print("No hay bebe en cuna")

    print("Luz analogica:", luz_analogica)
    print("Luz digital:", luz_digital)

    if luz_analogica == 0:
        print("Luz analogica en 0. Si tu sensor es de salida digital, usa Luz digital.")

    if temperatura is not None:
        print("Temperatura:", temperatura, "C")
        print("Humedad:", humedad, "%")
    else:
        print("No se pudo leer temperatura/humedad")

    if aceleracion is not None:
        print("Aceleracion MPU:", aceleracion)
        print("Diferencia movimiento:", abs(aceleracion - 1.0))
    else:
        print("No se pudo leer movimiento")

    # =========================
    # NO HAY BEBE
    # =========================

    if not bebe:
        print("Estado: cuna vacia")

        todo_apagado()
        led_alerta()

        time.sleep(1)
        continue

    # =========================
    # SI HAY BEBE
    # =========================

    print("Estado: bebe detectado")

    alarma = False
    razones = []

    # =========================
    # TEMPERATURA
    # =========================

    if temperatura is not None:
        if temperatura >= TEMP_ALTA:
            print("Temperatura alta: ventilador y peltier encendidos")
            ventilador_on()
            peltier_on()
            alarma = True
            razones.append("temperatura alta")

        elif temperatura <= TEMP_BAJA:
            print("Temperatura baja: ventilador y peltier apagados")
            ventilador_off()
            peltier_off()

        else:
            print("Temperatura normal")
            ventilador_off()
            peltier_off()

        if humedad < HUM_MIN or humedad > HUM_MAX:
            print("Humedad fuera de rango")
            alarma = True
            razones.append("humedad fuera de rango")

    else:
        ventilador_off()
        peltier_off()

    # =========================
    # LUZ
    # =========================

    # Si la analogica funciona:
    if luz_analogica > 0:
        if luz_analogica < UMBRAL_LUZ_OSCURA:
            print("Ambiente oscuro por lectura analogica")
        else:
            print("Ambiente con luz por lectura analogica")

    # Si la analogica no funciona, usamos digital:
    else:
        if luz_digital == 0:
            print("Ambiente oscuro o salida digital en 0")
        elif luz_digital == 1:
            print("Ambiente con luz o salida digital en 1")
        else:
            print("No hay lectura de luz")

    # =========================
    # MOVIMIENTO MPU + SERVO
    # =========================

    movimiento_detectado = detectar_movimiento(aceleracion)

    if movimiento_detectado:
        print("Movimiento detectado en MPU")
        alarma = True
        razones.append("movimiento detectado")

        # AQUI se mueve el servo
        servo_por_movimiento()
    else:
        print("Sin movimiento fuerte en MPU")
        mover_servo(SERVO_CENTRO)

    # =========================
    # ESTADO FINAL
    # =========================

    if alarma:
        print("ALARMA:", razones)

        led_alerta()
        beep(2, 150)

    else:
        print("Estado normal")

        led_normal()
        buzzer_off()
        mover_servo(SERVO_CENTRO)

    time.sleep(1)
