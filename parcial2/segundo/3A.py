#!/usr/bin/env python3
# practica3a_estilos_texto.py
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont, Image, ImageDraw
import time
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
font_b = ImageFont.load_default()
# ── Sección 1: texto normal (blanco sobre negro) ──
with canvas(device) as draw:
 draw.text((2, 2), 'Texto Normal', font=font_b, fill=255)
 # Rectángulo relleno (fondo blanco) para texto invertido
 draw.rectangle([(2, 16), (125, 30)], outline=255, fill=255)
 draw.text((4, 18), 'Texto Invertido', font=font_b, fill=0)
 # Rectángulo sin relleno (solo borde)
 draw.rectangle([(2, 34), (125, 48)], outline=255, fill=0)
 draw.text((10, 36), 'Texto con Borde', font=font_b, fill=255)
 # Texto con sombra (doble dibujo desplazado)
 draw.text((3, 52), 'Con Sombra!', font=font_b, fill=128)
 draw.text((2, 51), 'Con Sombra!', font=font_b, fill=255)
 time.sleep(5)

 