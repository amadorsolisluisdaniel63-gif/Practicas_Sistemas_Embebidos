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

    print("Efecto de atenuación (fade) iniciado")
    print("Presiona Ctrl+C para detener\n")

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
    print("\nPrograma detenido por el usuario")

finally:
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")