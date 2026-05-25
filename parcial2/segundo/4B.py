#!/usr/bin/env python3
# practica4b_carga_imagen.py
# Carga una imagen desde disco y la muestra en el OLED
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image
import time, os
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
def cargar_y_mostrar(ruta_imagen):
 """
 Carga una imagen, la redimensiona a 128x64 y la convierte
 al formato monocromático requerido por el SSD1306.
 """
 if not os.path.exists(ruta_imagen):
 print(f'ERROR: No se encontró {ruta_imagen}')
 return
 # 1. Cargar imagen original
 img_original = Image.open(ruta_imagen)
 print(f'Imagen cargada: {img_original.size} modo={img_original.mode}')
 # 2. Redimensionar manteniendo proporción
 img_resized = img_original.resize(
 (device.width, device.height),
 Image.Resampling.LANCZOS # Filtro de alta calidad
 )
 # 3. Convertir a escala de grises
 img_gray = img_resized.convert('L')
 # 4. Umbralización (threshold): píxeles > 128 = blanco, resto = negro
 img_mono = img_gray.point(lambda x: 255 if x > 128 else 0, '1')
 # 5. Mostrar en el display
 device.display(img_mono)
 print('Imagen mostrada en pantalla OLED.')
def generar_imagen_prueba():
 """Genera una imagen de prueba si no hay archivo disponible"""
 from PIL import ImageDraw
 img = Image.new('L', (128, 64), 0) # Fondo negro
 draw = ImageDraw.Draw(img)
 # Patrón de tablero de ajedrez
 for y in range(0, 64, 8):
 for x in range(0, 128, 8):
 if (x//8 + y//8) % 2 == 0:
 draw.rectangle([(x,y),(x+7,y+7)], fill=200)
 # Logo 'T' al centro
 draw.rectangle([(50,10),(78,20)], fill=255)
 draw.rectangle([(60,10),(68,55)], fill=255)
 img.save('/tmp/prueba_oled.png')

 return '/tmp/prueba_oled.png'
# Ruta a la imagen (cambiar por su archivo)
ruta = '/tmp/mi_imagen.png'
if not os.path.exists(ruta):
 print('Archivo no encontrado. Generando imagen de prueba...')
 ruta = generar_imagen_prueba()
cargar_y_mostrar(ruta)
time.sleep(10)
device.cleanup()