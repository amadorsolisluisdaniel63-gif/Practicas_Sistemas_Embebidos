P4_RecorridoLedVectorPWM
P4 - Recorrido Led Vector PWM

Objetivo
Implementar un efecto de encendido y apagado gradual de LEDs utilizando PWM.

Materiales
- Raspberry Pi  
- 5 LEDs  
- 5 resistencias  
- Protoboard  
- Cables jumper  

Código

#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

PINS = [17, 18, 27, 22, 23]

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pwms = []
    for pin in PINS:
        GPIO.setup(pin, GPIO.OUT)
        pwm = GPIO.PWM(pin, 200)
        pwm.start(0)
        pwms.append(pwm)

    while True:
        for i in range(len(PINS)):
            for p in pwms:
                p.ChangeDutyCycle(0)

            for duty in range(0, 101, 5):
                pwms[i].ChangeDutyCycle(duty)
                time.sleep(0.02)

            for duty in range(100, -1, -5):
                pwms[i].ChangeDutyCycle(duty)
                time.sleep(0.02)

except KeyboardInterrupt:
    pass

finally:
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup()


Explicación
El programa utiliza PWM para variar la intensidad de los LEDs. Cada LED se enciende gradualmente aumentando su intensidad y luego se apaga disminuyéndola. Este proceso crea un efecto de atenuación.


