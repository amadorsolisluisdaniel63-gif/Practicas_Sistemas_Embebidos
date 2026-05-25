# P4B_dashboard.py — Panel de información con gráficos
from machine import I2C, Pin
import ssd1306
import time
import random
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
def barra(x, y, w, h, porcentaje, label):
 oled.text(label, x, y, 1)
 oled.rect(x, y+10, w, h, 1)
 relleno = int(w * porcentaje / 100)
 if relleno > 0:
 oled.fill_rect(x+1, y+11, relleno-1, h-2, 1)
 oled.text(str(porcentaje)+'%', x+w+2, y+10, 1)
 # Simular valores de sensores
for _ in range(20):
 temp = random.randint(18, 40)
 hum = random.randint(30, 90)
 cpu = random.randint(10, 95)
 oled.fill(0)
 # Título
 oled.fill_rect(0, 0, 128, 11, 1)
 oled.text('DASHBOARD', 24, 2, 0)
 # Barras de información
 barra(0, 14, 90, 10, temp, 'T')
 barra(0, 30, 90, 10, hum, 'H')
 barra(0, 46, 90, 10, cpu, 'C')
 oled.show()
 time.sleep(1)