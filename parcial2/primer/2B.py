# P2B_scroll_vertical.py — Lista de items que sube como créditos de película
from machine import I2C, Pin
import ssd1306
import time
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
noticias = [
 'Temp: 23 C',
 'Humedad: 65%',
 'Presion: 1013mb',
 'Velocidad: 12km/h',
 'Calidad aire: Buena',
 'UV Index: 3',
]
# Construir una 'pantalla larga' concatenando todas las noticias
ALTURA_TOTAL = len(noticias) * 10 + 64 # margen extra abajo
for offset in range(ALTURA_TOTAL):
 oled.fill(0)
 for i, texto in enumerate(noticias):
 y = i * 10 - offset + 64 # empieza abajo, sube
 if -8 < y < 64: # solo dibujar si es visible
 oled.text(texto, 2, y, 1)
 oled.show()
 time.sleep_ms(50)

 