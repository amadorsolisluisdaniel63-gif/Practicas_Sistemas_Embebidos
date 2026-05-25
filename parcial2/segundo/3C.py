#!/usr/bin/env python3
# practica3c_tarjeta_presentacion.py
# Diseño de layout complejo con zonas diferenciadas
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
font = ImageFont.load_default()
with canvas(device) as draw:
 # ── Header: banda superior rellena ──
 draw.rectangle([(0,0),(127,13)], outline=255, fill=255)
 draw.text((15, 2), '[ TESOEM 2025 ]', font=font, fill=0)
 # ── Contenido central ──
 draw.text((2, 16), 'Nombre: _______________', font=font, fill=255)
 draw.text((2, 27), 'No. Ctrl: _____________', font=font, fill=255)
 draw.text((2, 38), 'Carrera: ISC', font=font, fill=255)
 # ── Footer: banda inferior rellena ──
 draw.rectangle([(0,51),(127,63)], outline=255, fill=255)
 draw.text((10, 53), 'Embebidos Aplicados', font=font, fill=0)
time.sleep(15)
device.cleanup()