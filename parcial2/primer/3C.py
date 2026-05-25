# P3C_modo_oscuro_claro.py — Alterna entre modos de visualización
from machine import I2C, Pin
import ssd1306
import time
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
def dibujar_contenido(modo_oscuro):
 fondo = 0 if modo_oscuro else 1
 texto = 1 if modo_oscuro else 0
 oled.fill(fondo)
 oled.text('Modo:', 10, 10, texto)
 etiqueta = 'Oscuro' if modo_oscuro else 'Claro'
 oled.text(etiqueta, 10, 24, texto)
 oled.text('TESOEM 2025', 10, 40, texto)
 oled.show()
modo = True
while True:
 dibujar_contenido(modo)
 time.sleep(2)
 modo = not modo