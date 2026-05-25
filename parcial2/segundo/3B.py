#!/usr/bin/env python3
# practica3b_contraste.py
# Demuestra el control del registro de contraste del SSD1306
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
font = ImageFont.load_default()
print('Demostracion de control de contraste.')
# Dibujar contenido fijo
with canvas(device) as draw:
 draw.text((5, 20), 'Contraste:', font=font, fill=255)
 draw.rectangle([(5,35),(120,50)], outline=255)
# Ciclo de contraste ascendente y descendente
for _ in range(2):
 # Aumentar contraste gradualmente
 for nivel in range(0, 256, 16):
 device.contrast(nivel)
 with canvas(device) as draw:
 draw.text((5, 2), f'Contraste: {nivel}/255', font=font, fill=255)
 draw.rectangle([(5,14),(5 + int(nivel/2),25)],
 outline=255, fill=255)
 draw.text((5, 30), 'Min ------- Max', font=font, fill=255)
 barra_x = 5 + int(nivel * 110/255)
 draw.rectangle([(barra_x-2, 40),(barra_x+2, 55)],
 outline=255, fill=255)
 time.sleep(0.1)
 # Disminuir contraste
 for nivel in range(255, -1, -16):
 device.contrast(nivel)
 time.sleep(0.05)
device.contrast(128) # Restablecer contraste medio
device.cleanup()