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

    print("Efecto de corrida con 5 LEDs iniciado (PWM)")
    print("Presiona Ctrl+C para detener\n")

    while True:
        
        for i in range(len(PINS)):
            
            for p in pwms:
                p.ChangeDutyCycle(0)
            
            pwms[i].ChangeDutyCycle(100)
            time.sleep(0.25)   

        
        for i in range(len(PINS)-1, -1, -1):
            for p in pwms:
                p.ChangeDutyCycle(0)
            pwms[i].ChangeDutyCycle(100)
            time.sleep(0.25)

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario")

finally:
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")