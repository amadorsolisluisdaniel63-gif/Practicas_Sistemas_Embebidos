# P1B_contador.py — Actualiza texto dinámicamente (simula sensor)
from machine import I2C, Pin
import ssd1306
import time
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
contador = 0
while True:
 oled.fill(0)
 oled.text('Contador:', 0, 0, 1)
 oled.text(str(contador), 40, 28, 1)
 oled.text('Presiona RST', 0, 50, 1)
 oled.show()
 contador += 1
 time.sleep(0.5)