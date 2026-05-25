# P1C_contraste.py — Cicla el brillo de la pantalla
from machine import I2C, Pin
import ssd1306
import time
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text('Contraste:', 16, 20, 1)
oled.show()
# Barrido de brillo: 0 (mínimo) → 255 (máximo) → 0
while True:
 for nivel in range(0, 256, 5):
 oled.contrast(nivel)
 oled.fill(0)
 oled.text('Brillo:', 16, 20, 1)
 oled.text(str(nivel), 52, 36, 1)
 oled.show()
 time.sleep_ms(30)
 for nivel in range(255, -1, -5):
 oled.contrast(nivel)
 oled.fill(0)
 oled.text('Brillo:', 16, 20, 1)
 oled.text(str(nivel), 52, 36, 1)
 oled.show()
 time.sleep_ms(30)