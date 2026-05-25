P2 - Semaforo Leds

Objetivo
Simular el funcionamiento de un semáforo utilizando tres LEDs controlados por una Raspberry Pi.

Materiales
- Raspberry Pi  
- 3 LEDs  
- 3 resistencias  
- Protoboard  
- Cables jumper  

Código
```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LED_ROJO = 18
LED_AMARILLO = 23
LED_VERDE = 24

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(LED_ROJO, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED_AMARILLO, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED_VERDE, GPIO.OUT, initial=GPIO.LOW)

    while True:
        GPIO.output(LED_ROJO, GPIO.HIGH)
        GPIO.output(LED_AMARILLO, GPIO.LOW)
        GPIO.output(LED_VERDE, GPIO.LOW)
        time.sleep(60)

        GPIO.output(LED_ROJO, GPIO.LOW)
        GPIO.output(LED_AMARILLO, GPIO.HIGH)
        GPIO.output(LED_VERDE, GPIO.LOW)
        time.sleep(60)

        GPIO.output(LED_ROJO, GPIO.LOW)
        GPIO.output(LED_AMARILLO, GPIO.LOW)
        GPIO.output(LED_VERDE, GPIO.HIGH)
        time.sleep(60)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()


Explicación
El programa controla tres LEDs conectados a la Raspberry Pi. Cada LED representa un color del semáforo. Se enciende uno a la vez siguiendo la secuencia rojo, amarillo y verde. Cada estado dura 60 segundos y se repite continuamente.


Autor
Amador Solis Luis Daniel
Grupo: 8S22
