#!/usr/bin/env python3
# practica4c_slideshow.py
# Crea un slideshow con múltiples frames generados dinámicamente
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time, math
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
font = ImageFont.load_default()
def pantalla_bienvenida():
 with canvas(device) as draw:
 draw.rectangle([(0,0),(127,63)], outline=255)
 draw.text((15, 5), 'BIENVENIDO', font=font, fill=255)
 draw.line([(10,17),(118,17)], fill=255)
 draw.text((5, 22), 'Practica 4:', font=font, fill=255)
 draw.text((5, 34), 'Graficos OLED',font=font, fill=255)
 draw.text((5, 48), 'SSD1306', font=font, fill=255)
 time.sleep(4)
def pantalla_ondas():
 """Efecto de onda sinusoidal animada"""
 for frame in range(60):
 with canvas(device) as draw:
 for x in range(128):
 y = 32 + int(20 * math.sin(
 (x + frame * 4) * math.pi / 20
 ))
 if 0 <= y < 64:
 draw.point([(x, y)], fill=255)
 draw.point([(x, y+1)], fill=255)
 time.sleep(0.04)
def pantalla_barras():
 """Ecualizador de barras animado"""
 import random
 alturas = [random.randint(10, 60) for _ in range(8)]
 for _ in range(40):
 # Suavizar transición de alturas
 alturas = [min(60, max(10,
 h + random.randint(-8, 8)))

 for h in alturas]
 with canvas(device) as draw:
 draw.text((0, 0), 'Ecualizador', font=font, fill=255)
 for i, h in enumerate(alturas):
 x0 = 5 + i * 15
 draw.rectangle(
 [(x0, 63-h), (x0+11, 63)],
 outline=255, fill=255
 )
 time.sleep(0.1)
# Secuencia de presentación
pantalla_bienvenida()
pantalla_ondas()
pantalla_barras()
device.cleanup()