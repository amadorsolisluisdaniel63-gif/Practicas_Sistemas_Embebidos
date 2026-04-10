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

    print("Semáforo iniciado (Modo BCM)")
    print("Rojo -> Amarillo -> Verde (cada 60 segundos)")
    print("Presiona Ctrl+C para salir")

    
    while True:
        
        GPIO.output(LED_ROJO, GPIO.HIGH)
        GPIO.output(LED_AMARILLO, GPIO.LOW)
        GPIO.output(LED_VERDE, GPIO.LOW)
        print("ROJO ENCENDIDO")
        time.sleep(60)

        
        GPIO.output(LED_ROJO, GPIO.LOW)
        GPIO.output(LED_AMARILLO, GPIO.HIGH)
        GPIO.output(LED_VERDE, GPIO.LOW)
        print("AMARILLO ENCENDIDO")
        time.sleep(60)

    
        GPIO.output(LED_ROJO, GPIO.LOW)
        GPIO.output(LED_AMARILLO, GPIO.LOW)
        GPIO.output(LED_VERDE, GPIO.HIGH)
        print("VERDE ENCENDIDO")
        time.sleep(60)

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")

finally:
    
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")