P1 - Led Blink

Descripción
Este programa permite controlar el encendido y apagado de un LED utilizando una Raspberry Pi. El LED parpadea cada segundo mediante el uso de los pines GPIO en modo BCM.

Objetivo
Aprender a controlar un LED usando la Raspberry Pi mediante programación en Python, comprendiendo el uso de los pines GPIO y su configuración básica.

Materiales
- Raspberry Pi  
- 1 LED  
- 1 resistencia (220Ω o 330Ω)  
- Protoboard  
- Cables jumper  
- Fuente de alimentación  

Configuración del circuito
- Conectar el ánodo (pata larga) del LED al GPIO 18  
- Conectar el cátodo (pata corta) a una resistencia  
- Conectar la resistencia a GND  

Código

```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LED_PIN = 18  # GPIO 18 (pin físico 12)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

    print("Control de LED iniciado (Modo BCM)")
    print(f"Usando GPIO {LED_PIN} (Pin físico 12)")
    print("Presiona Ctrl+C para salir")

    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ENCENDIDO")
        time.sleep(1)

        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED APAGADO")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")

finally:
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")
