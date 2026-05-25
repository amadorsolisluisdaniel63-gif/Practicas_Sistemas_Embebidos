#!/usr/bin/env python3
# practica4a_primitivas.py
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import time, math
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

def demo_lineas():
 with canvas(device) as draw:
 for i in range(0, 128, 16):
 draw.line([(i, 0), (127-i, 63)], fill=255)
 draw.line([(0, i//2), (127, 63 - i//2)], fill=255)
 time.sleep(3)
def demo_rectangulos():
 with canvas(device) as draw:
 # Anidados
 for i in range(0, 28, 6):
 draw.rectangle([(i, i//2), (127-i, 63-i//2)],
 outline=255, fill=0)
 # Relleno
 draw.rectangle([(50, 20), (78, 44)], outline=255, fill=255)
 time.sleep(3)
def demo_circulos():
 with canvas(device) as draw:
 # Círculos concéntricos
 cx, cy = 64, 32
 for r in range(5, 32, 5):
 draw.ellipse([(cx-r, cy-r), (cx+r, cy+r)],
 outline=255, fill=0)
 time.sleep(3)
def demo_reloj_analogico():
 """Mini reloj analógico usando arcos y líneas"""
 import datetime
 for _ in range(30):
 now = datetime.datetime.now()
 h_ang = (now.hour % 12) / 12 * 360 - 90
 m_ang = now.minute / 60 * 360 - 90
 s_ang = now.second / 60 * 360 - 90
 cx, cy, r = 32, 32, 28
 with canvas(device) as draw:
 draw.ellipse([(cx-r,cy-r),(cx+r,cy+r)], outline=255)
 # Manecilla hora
 hx = cx + int(15*math.cos(math.radians(h_ang)))
 hy = cy + int(15*math.sin(math.radians(h_ang)))
 draw.line([(cx,cy),(hx,hy)], fill=255, width=2)
 # Manecilla minuto
 mx = cx + int(22*math.cos(math.radians(m_ang)))
 my = cy + int(22*math.sin(math.radians(m_ang)))
 draw.line([(cx,cy),(mx,my)], fill=255, width=1)
 # Marcadores de hora (12 puntos)
 for deg in range(0, 360, 30):
 px = cx + int(26*math.cos(math.radians(deg)))
 py = cy + int(26*math.sin(math.radians(deg)))
 draw.point([(px,py)], fill=255)
 # Texto digital al lado
 draw.text((70, 10), now.strftime('%H:%M'),
 fill=255)
 draw.text((70, 24), now.strftime('%S s'),
 fill=255)
 draw.text((68, 40), 'TESOEM', fill=255)
 time.sleep(1)
# Ejecutar demostraciones
demo_lineas()
demo_rectangulos()
demo_circulos()
demo_reloj_analogico()
device.cleanup()