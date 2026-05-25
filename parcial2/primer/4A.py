# P4A_graficos.py — Demostración de primitivas de dibujo
from machine import I2C, Pin
import ssd1306
import time
import math
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
def demo_lineas():
 oled.fill(0)
 oled.text('Lineas', 40, 0, 1)
 for i in range(0, 128, 16):
 oled.line(0, 64, i, 10, 1) # abanico de líneas
 oled.show()
 time.sleep(2)
def demo_rectangulos():
 oled.fill(0)
 oled.text('Rectang.', 28, 0, 1)
 oled.rect(5, 12, 50, 40, 1) # contorno
 oled.fill_rect(70, 12, 50, 40, 1) # sólido
 # Texto encima del rectángulo sólido
 oled.text('OK', 82, 28, 0) # texto negro
 oled.show()
 time.sleep(2)
def demo_elipses():
 oled.fill(0)
 oled.text('Elipses', 32, 0, 1)
 oled.ellipse(32, 40, 28, 20, 1) # elipse contorno
 oled.ellipse(96, 40, 28, 20, 1, True) # elipse sólida
 oled.show()
 time.sleep(2)
def demo_circulo_manual(cx, cy, r):
 # Dibujar círculo con algoritmo de punto medio
 x, y = r, 0
 while x >= y:
 for px, py in [(cx+x,cy+y),(cx-x,cy+y),(cx+x,cy-y),(cx-x,cy-y),
 (cx+y,cy+x),(cx-y,cy+x),(cx+y,cy-x),(cx-y,cy-x)]:
 oled.pixel(px, py, 1)
 y += 1
 x = int((r*r - y*y)**0.5)
def demo_circulos():
 oled.fill(0)
 oled.text('Circulos', 28, 0, 1)
 for radio in range(5, 30, 5):
 demo_circulo_manual(64, 38, radio)
 oled.show()
 time.sleep(2)
# Ejecutar demos en secuencia
demo_lineas()
demo_rectangulos()
demo_elipses()
demo_circulos()