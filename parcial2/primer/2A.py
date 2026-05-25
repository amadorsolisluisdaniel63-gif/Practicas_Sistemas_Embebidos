# P2A_ticker.py — Texto que se desplaza horizontalmente (ticker)
from machine import I2C, Pin
import ssd1306
import time
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
mensaje = ' >>> TESOEM - Sistemas Embebidos - ISC 2025 <<< '
pos_x = 128 # inicio fuera de pantalla por la derecha

while True:
 oled.fill(0)
 oled.text(mensaje, pos_x, 28, 1)
 oled.show()
 pos_x -= 3 # velocidad: 3 px por frame
 # Reiniciar cuando el texto complete su recorrido
 if pos_x < -(len(mensaje) * 8):
 pos_x = 128
 time.sleep_ms(40) # ~25 f