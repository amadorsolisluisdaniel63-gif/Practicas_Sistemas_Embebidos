# P1A_texto_basico.py — Texto estático en múltiples líneas
from machine import I2C, Pin
import ssd1306
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
# Línea 1 — título centrado (16 chars × 8px = 128px; cadena de 7 chars → inicio en
(4.5*8)=36)
oled.text('TESOEM', 36, 0, 1)
# Separador horizontal
oled.line(0, 10, 127, 10, 1)
# Información en filas
oled.text('Materia:', 0, 16, 1)
oled.text('Embebidos', 0, 26, 1)
oled.text('Alumno:', 0, 38, 1)
oled.text('Tu Nombre', 0, 48, 1)

oled.show()