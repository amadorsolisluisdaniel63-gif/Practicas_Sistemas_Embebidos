#!/usr/bin/env python3
# practica2c_scroll_hardware.py
# Utiliza comandos de hardware del SSD1306 para scrolling
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()
# Primero dibujamos el contenido estático
with canvas(device) as draw:
 draw.text((10, 10), 'TESOEM', font=font, fill=255)
 draw.text((10, 25), 'Scroll HW', font=font, fill=255)
 draw.text((10, 40), 'SSD1306 cmd', font=font, fill=255)
# Activar scrolling horizontal por hardware hacia la derecha
# Comando 0x26 = scroll derecha, 0x27 = scroll izquierda
# Parámetros: dummy, start_page, interval, end_page, dummy, dummy
device.serial.data([
 0x26, # Scroll horizontal a la derecha
 0x00, # Byte dummy
 0x00, # Página inicial: 0
 0x00, # Intervalo: 5 frames
 0x07, # Página final: 7 (todas las páginas)
 0x00, # Byte dummy
 0xFF, # Byte dummy
 0x2F, # Activar scroll
])
print('Scroll hardware activo. Ctrl+C para detener.')
try:
 time.sleep(15)
except KeyboardInterrupt:
 # Detener scroll con comando 0x2E
 device.serial.data([0x2E])
 device.cleanup()
 print('Scroll hardware detenido.')