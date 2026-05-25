PRÁCTICA 1: TEXTO EN PANTALLA
Objetivo de la Práctica
Desarrollar programas Python que desplieguen texto estático en la pantalla OLED SSD1306,
controlando la posición, tamaño, fuente tipográfica y estilo del texto, comprendiendo el sistema
de coordenadas del display y el modelo de color monocromático.
Fundamento Teórico Específico
El sistema de coordenadas del SSD1306 tiene su origen (0,0) en la esquina superior izquierda. El
eje X aumenta hacia la derecha (0 a 127) y el eje Y aumenta hacia abajo (0 a 63). El modo de
color '1' de Pillow representa píxeles con un valor de 0 (apagado/negro) o 255
(encendido/blanco).
Las fuentes en luma.oled/Pillow pueden ser: fuente bitmap por defecto (load_default()), o fuentes
TrueType (.ttf) de sistema. Para proyectos profesionales se recomienda usar fuentes TrueType
para mayor legibilidad.

1A.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse con Python 3 en sistemas Linux o Raspberry Pi.

# practica1a_texto_basico.py
Es un comentario con el nombre del archivo del programa.

# Muestra texto estático en distintas posiciones
Describe que el programa mostrará texto fijo en la pantalla OLED.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectarse con la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas, que permite dibujar texto y figuras en la pantalla.

from PIL import ImageFont
Importa las fuentes de texto para escribir caracteres en la pantalla.

import time
Importa funciones de tiempo, como pausas con sleep().

# Inicialización del dispositivo
Comentario que indica el inicio de la configuración de la pantalla.

serial = i2c(port=1, address=0x3C)
Configura la comunicación I2C usando el puerto 1 y la dirección hexadecimal 0x3C de la pantalla OLED.

device = ssd1306(serial)
Crea el objeto de la pantalla OLED usando la conexión I2C configurada.

# Fuente por defecto (bitmap 6x8 px)
Comentario que indica que se utilizará la fuente básica de 6x8 píxeles.

font_default = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

# Usar canvas como context manager (limpia automáticamente)
Comentario que explica que canvas limpia la pantalla automáticamente al iniciar.

with canvas(device) as draw:
Abre un área de dibujo para escribir y dibujar en la pantalla OLED.

draw.text((10, 0), 'TESOEM - OLED', font=font_default, fill=255)
Muestra el texto "TESOEM - OLED" en la posición X=10, Y=0 usando la fuente cargada y color blanco.

draw.line([(0, 12), (127, 12)], fill=255, width=1)
Dibuja una línea horizontal desde la coordenada (0,12) hasta (127,12) con grosor de 1 píxel.

draw.text((0, 16), 'Alumno:', font=font_default, fill=255)
Muestra la palabra "Alumno:" en la posición (0,16).

draw.text((50, 16), '________________', font=font_default, fill=255)
Muestra una línea para escribir el nombre del alumno.

draw.text((0, 28), 'Grupo: ', font=font_default, fill=255)
Muestra la palabra "Grupo:" en la posición (0,28).

draw.text((50, 28), '________', font=font_default, fill=255)
Muestra una línea para escribir el grupo.

draw.text((0, 40), 'Materia:', font=font_default, fill=255)
Muestra la palabra "Materia:".

draw.text((50, 40), 'Embebidos', font=font_default, fill=255)
Muestra el texto "Embebidos" como nombre de la materia.

draw.text((0, 52), 'Status: ', font=font_default, fill=255)
Muestra la palabra "Status:".

draw.text((50, 52), '[ OK ] ', font=font_default, fill=255)
Muestra el mensaje [ OK ] indicando que el sistema funciona correctamente.

time.sleep(10)
Mantiene el contenido visible en la pantalla durante 10 segundos antes de terminar el programa.

1B.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3 en Linux o Raspberry Pi.

# practica1b_texto_fuentes.py
Comentario con el nombre del archivo del programa.

# Uso de fuentes TrueType para texto con diferentes tamaños
Describe que el programa utiliza fuentes TrueType con distintos tamaños de letra.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas, que permite dibujar texto y gráficos en la pantalla.

from PIL import ImageFont
Importa las funciones para cargar y usar diferentes fuentes de texto.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la comunicación I2C usando el puerto 1 y la dirección 0x3C de la pantalla OLED.

device = ssd1306(serial)
Crea el objeto de la pantalla OLED usando la conexión configurada.

# Cargar fuentes TrueType del sistema
Comentario que indica que se cargarán fuentes TTF del sistema operativo.

# Nota: Las siguientes rutas son estándar en Raspberry Pi OS
Explica que las rutas de las fuentes son las normales en Raspberry Pi OS.

try:
Inicia un bloque de prueba para intentar cargar las fuentes.

font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
Carga la fuente DejaVuSans con tamaño de 10 puntos para texto pequeño.

font_medium = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
Carga la fuente DejaVuSans con tamaño de 14 puntos para texto mediano.

font_large = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
Carga la fuente DejaVuSans en negritas con tamaño de 20 puntos para texto grande.

except IOError:
Se ejecuta si ocurre un error al cargar las fuentes TrueType.

# Fallback a fuente por defecto si no se encuentran TTF
Comentario que explica que se usará la fuente básica si las fuentes TTF no existen.

font_small = font_medium = font_large = ImageFont.load_default()
Asigna la fuente predeterminada a todas las variables de fuente.

with canvas(device) as draw:
Abre un área de dibujo para escribir en la pantalla OLED.

draw.text((2, 0), 'Texto Grande', font=font_large, fill=255)
Muestra el texto "Texto Grande" usando la fuente grande en la posición (2,0).

draw.text((2, 22), 'Texto Mediano', font=font_medium, fill=255)
Muestra el texto "Texto Mediano" usando la fuente mediana en la posición (2,22).

draw.text((2, 40), 'Texto pequeño - 10pt', font=font_small, fill=255)
Muestra el texto "Texto pequeño - 10pt" usando la fuente pequeña en la posición (2,40).

draw.text((2, 52), 'Default font (bitmap)', font=ImageFont.load_default(), fill=255)
Muestra texto usando la fuente predeterminada tipo bitmap.

time.sleep(10)
Mantiene la información visible en la pantalla durante 10 segundos antes de finalizar el programa.

1C.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse con Python 3.

# practica1c_info_dinamica.py
Comentario con el nombre del archivo del programa.

# Muestra información del sistema en tiempo real
Describe que el programa mostrará datos actualizados del sistema en la pantalla OLED.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y figuras en la pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time, datetime, subprocess
Importa módulos para manejar tiempo, fechas y ejecutar comandos del sistema.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED usando la conexión configurada.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

def get_cpu_temp():
Define una función para obtener la temperatura del procesador de la Raspberry Pi.

"""Lee temperatura del CPU de Raspberry Pi"""
Comentario interno que describe la función.

result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
Ejecuta el comando vcgencmd measure_temp para leer la temperatura del CPU.

return result.stdout.strip().replace('temp=', '')
Limpia el resultado y elimina la palabra temp= para mostrar solo la temperatura.

def get_ip_address():
Define una función para obtener la dirección IP del dispositivo.

"""Obtiene la dirección IP de la interfaz wlan0"""
Comentario que explica la función.

result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
Ejecuta el comando hostname -I para obtener la IP del sistema.

return result.stdout.split()[0] if result.stdout else 'N/A'
Devuelve la primera dirección IP encontrada o N/A si no existe.

print('Mostrando info del sistema. Ctrl+C para salir.')
Muestra un mensaje en la terminal indicando que el programa está funcionando.

try:
Inicia un bloque de control de errores.

while True:
Crea un ciclo infinito para actualizar continuamente la información.

now = datetime.datetime.now().strftime('%H:%M:%S')
Obtiene la hora actual con formato horas:minutos:segundos.

temp = get_cpu_temp()
Llama la función para obtener la temperatura del CPU.

ip = get_ip_address()
Llama la función para obtener la dirección IP.

with canvas(device) as draw:
Abre un área de dibujo en la pantalla OLED.

draw.text((0, 0), 'Raspberry Pi 3', font=font, fill=255)
Muestra el texto "Raspberry Pi 3" en la parte superior.

draw.line([(0,10),(127,10)], fill=255)
Dibuja una línea horizontal como separador.

draw.text((0, 14), f'Hora: {now}', font=font, fill=255)
Muestra la hora actual en pantalla.

draw.text((0, 26), f'Temp: {temp}', font=font, fill=255)
Muestra la temperatura del procesador.

draw.text((0, 38), f'IP: {ip}', font=font, fill=255)
Muestra la dirección IP del dispositivo.

draw.text((0, 50), 'TESOEM - 2025', font=font, fill=255)
Muestra un texto informativo en la parte inferior.

time.sleep(1)
Espera 1 segundo antes de actualizar nuevamente la información.

except KeyboardInterrupt:
Detecta cuando el usuario presiona Ctrl+C para detener el programa.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

print('Display apagado correctamente.')
Muestra un mensaje indicando que la pantalla se apagó correctamente.


PRÁCTICA 2: TEXTO SCROLLING (ANIMACIÓN DE TEXTO) 
Objetivo de la Práctica Implementar diferentes técnicas de animación de texto en la pantalla OLED, incluyendo scrolling horizontal, vertical y efectos de entrada/salida, comprendiendo los conceptos de buffer de frame, framerate y optimización de rendimiento. Fundamento Teórico Específico El scrolling de texto se implementa mediante el desplazamiento iterativo del punto de origen del texto en cada frame. 
La técnica consiste en: (1) calcular el offset de desplazamiento actual, (2) dibujar el texto en la posición desplazada, (3) mostrar el frame, (4) incrementar el offset y repetir. El SSD1306 también soporta scrolling por hardware mediante comandos específicos (0x26, 0x27, 0x29, 0x2A), aunque el scrolling por software ofrece mayor flexibilidad. 

2A.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica2a_scroll_horizontal.py
Comentario con el nombre del archivo del programa.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y gráficos en la pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

mensaje = ' >>> TESOEM - Sistemas Embebidos 2025 <<< '
Guarda el mensaje que se desplazará horizontalmente en la pantalla.

# Calcular ancho del texto en píxeles
Comentario que indica que se calculará el tamaño del texto.

# Fuente default: 6px por carácter aprox.
Explica que cada carácter ocupa aproximadamente 6 píxeles de ancho.

ancho_texto = len(mensaje) * 6
Calcula el ancho aproximado del texto multiplicando la cantidad de caracteres por 6 píxeles.

print('Scrolling horizontal. Ctrl+C para salir.')
Muestra un mensaje en la terminal indicando que el scroll está funcionando.

pos_x = device.width
Define la posición inicial del texto usando el ancho de la pantalla para comenzar fuera del borde derecho.

# Iniciar fuera del borde derecho
Comentario que explica la posición inicial del texto.

try:
Inicia un bloque para manejar errores o interrupciones.

while True:
Crea un ciclo infinito para mantener la animación del scroll.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

draw.text((pos_x, 28), mensaje, font=font, fill=255)
Dibuja el mensaje en la posición horizontal pos_x y vertical 28.

pos_x -= 3
Mueve el texto 3 píxeles hacia la izquierda en cada actualización.

# Velocidad: 3 px por frame
Comentario que explica la velocidad del desplazamiento.

# Reiniciar posición cuando el texto salga completamente
Comentario que indica cuándo reiniciar el movimiento.

if pos_x < -ancho_texto:
Verifica si todo el texto ya salió por el lado izquierdo de la pantalla.

pos_x = device.width
Reinicia la posición del texto al borde derecho para repetir el scroll.

time.sleep(0.03)
Espera 0.03 segundos entre cada actualización para controlar la velocidad de la animación.

# ~33 fps
Comentario que indica que la animación funciona aproximadamente a 33 cuadros por segundo.

except KeyboardInterrupt:
Detecta cuando el usuario presiona Ctrl+C para detener el programa.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

2B.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica2b_scroll_vertical.py
Comentario con el nombre del archivo del programa.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y gráficos en la pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

# Lista de líneas que se desplazan hacia arriba
Comentario que indica que habrá varias líneas moviéndose verticalmente.

lineas = [
Crea una lista con los textos que aparecerán en pantalla.

'Ingenieria en',
Primera línea de texto.

'Sistemas Comput.',
Segunda línea de texto.

'--- TESOEM ---',
Tercera línea de texto.

'Sistemas Embebidos',
Cuarta línea de texto.

'Aplicados a Moviles',
Quinta línea de texto.

'Alumno: __________',
Sexta línea de texto para el nombre del alumno.

'Grupo: __________',
Séptima línea de texto para el grupo.

'Practica 2 - Scroll',
Octava línea de texto.

]
Finaliza la lista de líneas.

LINE_HEIGHT = 12
Define que cada línea ocupará 12 píxeles de altura.

# Altura en px por línea
Comentario que explica el tamaño vertical de cada línea.

total_px = len(lineas) * LINE_HEIGHT
Calcula el tamaño total del bloque de texto multiplicando el número de líneas por la altura de cada una.

offset = 0
Variable que controla el desplazamiento vertical del texto.

print('Scrolling vertical. Ctrl+C para salir.')
Muestra un mensaje en la terminal indicando que el scroll vertical está funcionando.

try:
Inicia un bloque para manejar errores o interrupciones.

while True:
Crea un ciclo infinito para mantener la animación.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

for i, linea in enumerate(lineas):
Recorre cada línea de texto junto con su posición en la lista.

y = i * LINE_HEIGHT - offset
Calcula la posición vertical de cada línea según el desplazamiento actual.

# Solo dibujar si está dentro del área visible
Comentario que explica que solo se mostrarán líneas visibles en pantalla.

if -LINE_HEIGHT < y < device.height:
Verifica si la línea está dentro de la zona visible de la pantalla OLED.

draw.text((2, y), linea, font=font, fill=255)
Dibuja la línea de texto en la posición (2,y).

offset += 1
Mueve el texto 1 píxel hacia arriba en cada actualización.

if offset >= total_px:
Verifica si todo el texto ya salió de la pantalla.

offset = 0
Reinicia el desplazamiento para repetir el scroll desde el inicio.

time.sleep(0.05)
Espera 0.05 segundos entre cada actualización para controlar la velocidad del movimiento.

except KeyboardInterrupt:
Detecta cuando el usuario presiona Ctrl+C para detener el programa.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

2C.py
#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica2c_scroll_hardware.py
Comentario con el nombre del archivo del programa.

# Utiliza comandos de hardware del SSD1306 para scrolling
Describe que el scroll se realiza usando comandos internos del controlador SSD1306.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y gráficos en la pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED usando la conexión configurada.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

# Primero dibujamos el contenido estático
Comentario que indica que primero se mostrará texto fijo en pantalla.

with canvas(device) as draw:
Abre un área de dibujo para escribir en la pantalla OLED.

draw.text((10, 10), 'TESOEM', font=font, fill=255)
Muestra el texto "TESOEM" en la posición (10,10).

draw.text((10, 25), 'Scroll HW', font=font, fill=255)
Muestra el texto "Scroll HW" en la posición (10,25).

draw.text((10, 40), 'SSD1306 cmd', font=font, fill=255)
Muestra el texto "SSD1306 cmd" en la posición (10,40).

# Activar scrolling horizontal por hardware hacia la derecha
Comentario que indica que se activará el desplazamiento horizontal usando hardware.

# Comando 0x26 = scroll derecha, 0x27 = scroll izquierda
Explica que el comando hexadecimal 0x26 activa scroll a la derecha y 0x27 a la izquierda.

# Parámetros: dummy, start_page, interval, end_page, dummy, dummy
Describe los parámetros necesarios para configurar el scroll.

device.serial.data([
Envía una lista de comandos directamente al controlador SSD1306.

0x26,
Comando hexadecimal para activar scroll horizontal hacia la derecha.

0x00,
Byte de relleno o dummy requerido por el controlador.

0x00,
Define la página inicial del scroll, en este caso la página 0.

0x00,
Define el intervalo de velocidad del scroll.

0x07,
Define la página final del scroll, en este caso la página 7.

0x00,
Byte dummy requerido por el controlador.

0xFF,
Byte dummy requerido por el controlador.

0x2F,
Comando para activar el scroll configurado.

])
Finaliza la lista de comandos enviados al SSD1306.

print('Scroll hardware activo. Ctrl+C para detener.')
Muestra un mensaje en la terminal indicando que el scroll está funcionando.

try:
Inicia un bloque para controlar interrupciones.

time.sleep(15)
Mantiene el scroll activo durante 15 segundos.

except KeyboardInterrupt:
Detecta cuando el usuario presiona Ctrl+C.

# Detener scroll con comando 0x2E
Comentario que indica el comando para detener el scroll.

device.serial.data([0x2E])
Envía el comando hexadecimal 0x2E para desactivar el scroll del SSD1306.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

print('Scroll hardware detenido.')
Muestra un mensaje indicando que el scroll fue detenido correctamente.


PRÁCTICA 3: TEXTO Y MANEJO DE ESTILOS VISUALES
Objetivo de la Práctica Aplicar técnicas avanzadas de presentación visual en la pantalla monocromática OLED, explorando el uso de inversión de color, contornos, áreas de fondo, texto resaltado y efectos visuales que simulan 'colores' a través del contraste blanco-negro. 
Fundamento Teórico Específico Aunque el SSD1306 es monocromático (1 bit por píxel), existen técnicas visuales que enriquecen la interfaz: inversión de pantalla completa (swap 0↔1 en todos los píxeles), texto sobre fondo negro (normal), texto negro sobre fondo blanco (invertido por región), outline/borde de texto, y el uso del contraste del controlador (registro 0x81) para ajustar la intensidad luminosa. La inversión de color se puede aplicar: a nivel de dispositivo (device.contrast(0) oscurece, device.contrast(255) maximiza brillo) o a nivel de imagen (ImageOps.invert() de Pillow invierte el buffer). 

3A.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica3a_estilos_texto.py
Comentario con el nombre del archivo del programa.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y gráficos en la pantalla.

from PIL import ImageFont, Image, ImageDraw
Importa herramientas de PIL para manejar fuentes, imágenes y dibujo.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

font_b = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

# ── Sección 1: texto normal (blanco sobre negro) ──
Comentario que indica la primera sección de estilos de texto.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

draw.text((2, 2), 'Texto Normal', font=font_b, fill=255)
Muestra texto normal en color blanco sobre fondo negro en la posición (2,2).

# Rectángulo relleno (fondo blanco) para texto invertido
Comentario que explica que se creará un fondo blanco para invertir colores.

draw.rectangle([(2, 16), (125, 30)], outline=255, fill=255)
Dibuja un rectángulo blanco relleno desde la coordenada (2,16) hasta (125,30).

draw.text((4, 18), 'Texto Invertido', font=font_b, fill=0)
Muestra texto negro sobre el rectángulo blanco, creando un efecto invertido.

# Rectángulo sin relleno (solo borde)
Comentario que indica que se dibujará un rectángulo únicamente con borde.

draw.rectangle([(2, 34), (125, 48)], outline=255, fill=0)
Dibuja un rectángulo con borde blanco y fondo negro.

draw.text((10, 36), 'Texto con Borde', font=font_b, fill=255)
Muestra texto blanco dentro del rectángulo con borde.

# Texto con sombra (doble dibujo desplazado)
Comentario que explica que el efecto sombra se crea dibujando el texto dos veces.

draw.text((3, 52), 'Con Sombra!', font=font_b, fill=128)
Dibuja el texto ligeramente desplazado para simular una sombra.

draw.text((2, 51), 'Con Sombra!', font=font_b, fill=255)
Dibuja el texto principal encima de la sombra.

time.sleep(5)
Mantiene el contenido visible en la pantalla durante 5 segundos.

3B.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica3b_contraste.py
Comentario con el nombre del archivo del programa.

# Demuestra el control del registro de contraste del SSD1306
Describe que el programa controla el nivel de brillo o contraste de la pantalla OLED.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y gráficos en la pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

print('Demostracion de control de contraste.')
Muestra un mensaje en la terminal indicando que inicia la demostración de contraste.

# Dibujar contenido fijo
Comentario que indica que se mostrará contenido estático en la pantalla.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

draw.text((5, 20), 'Contraste:', font=font, fill=255)
Muestra el texto "Contraste:" en la pantalla.

draw.rectangle([(5,35),(120,50)], outline=255)
Dibuja un rectángulo que funcionará como barra visual del contraste.

# Ciclo de contraste ascendente y descendente
Comentario que explica que el contraste aumentará y disminuirá automáticamente.

for _ in range(2):
Repite el ciclo completo dos veces.

# Aumentar contraste gradualmente
Comentario que indica el inicio del aumento de contraste.

for nivel in range(0, 256, 16):
Genera valores de contraste desde 0 hasta 255 avanzando de 16 en 16.

device.contrast(nivel)
Cambia el nivel de contraste de la pantalla OLED.

with canvas(device) as draw:
Abre nuevamente el área de dibujo para actualizar la información visual.

draw.text((5, 2), f'Contraste: {nivel}/255', font=font, fill=255)
Muestra el valor actual de contraste.

draw.rectangle([(5,14),(5 + int(nivel/2),25)], outline=255, fill=255)
Dibuja una barra rellena proporcional al nivel de contraste.

draw.text((5, 30), 'Min ------- Max', font=font, fill=255)
Muestra una escala visual de mínimo a máximo.

barra_x = 5 + int(nivel * 110/255)
Calcula la posición horizontal de un indicador móvil según el contraste actual.

draw.rectangle([(barra_x-2, 40),(barra_x+2, 55)], outline=255, fill=255)
Dibuja un pequeño rectángulo que indica visualmente el nivel de contraste.

time.sleep(0.1)
Espera 0.1 segundos entre cada cambio de contraste.

# Disminuir contraste
Comentario que indica el inicio de la reducción de contraste.

for nivel in range(255, -1, -16):
Genera valores desde 255 hasta 0 disminuyendo de 16 en 16.

device.contrast(nivel)
Reduce gradualmente el contraste de la pantalla.

time.sleep(0.05)
Espera 0.05 segundos entre cada disminución de contraste.

device.contrast(128)
Restablece el contraste a un nivel medio.

# Restablecer contraste medio
Comentario que indica que el contraste vuelve a un valor normal.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

3C.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica3c_tarjeta_presentacion.py
Comentario con el nombre del archivo del programa.

# Diseño de layout complejo con zonas diferenciadas
Describe que el programa crea una interfaz organizada en diferentes secciones de la pantalla.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar texto y gráficos en la pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time
Importa funciones relacionadas con el tiempo.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

# ── Header: banda superior rellena ──
Comentario que indica la creación de la parte superior de la interfaz.

draw.rectangle([(0,0),(127,13)], outline=255, fill=255)
Dibuja un rectángulo blanco relleno en la parte superior de la pantalla.

draw.text((15, 2), '[ TESOEM 2025 ]', font=font, fill=0)
Muestra el texto "TESOEM 2025" en color negro sobre el fondo blanco.

# ── Contenido central ──
Comentario que indica el área principal de información.

draw.text((2, 16), 'Nombre: _______________', font=font, fill=255)
Muestra un espacio para escribir el nombre.

draw.text((2, 27), 'No. Ctrl: _____________', font=font, fill=255)
Muestra un espacio para escribir el número de control.

draw.text((2, 38), 'Carrera: ISC', font=font, fill=255)
Muestra el nombre de la carrera.

# ── Footer: banda inferior rellena ──
Comentario que indica la creación de la parte inferior de la interfaz.

draw.rectangle([(0,51),(127,63)], outline=255, fill=255)
Dibuja un rectángulo blanco relleno en la parte inferior de la pantalla.

draw.text((10, 53), 'Embebidos Aplicados', font=font, fill=0)
Muestra el texto "Embebidos Aplicados" en negro sobre el fondo blanco.

time.sleep(15)
Mantiene la información visible en pantalla durante 15 segundos.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

PRÁCTICA 4: GRÁFICOS Y CARGA DE IMÁGENES 
Objetivo de la Práctica Implementar el dibujo de primitivas gráficas vectoriales (líneas, rectángulos, círculos, polígonos, arcos) y la carga, conversión y visualización de imágenes externas en la pantalla OLED SSD1306, comprendiendo el proceso de conversión de imágenes a modo monocromático 1-bit. 
Fundamento Teórico Específico El objeto ImageDraw de Pillow proporciona métodos de dibujo vectorial cuyas coordenadas son especificadas en píxeles. Para imágenes externas, el proceso de conversión es crítico: las imágenes RGB/RGBA deben convertirse al modo '1' (1 bit por píxel) mediante conversión a escala de grises y posterior umbralización (thresholding). La calidad del resultado depende del contraste de la imagen original y del valor del umbral seleccionado. 

4A.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica4a_primitivas.py
Comentario con el nombre del archivo del programa.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar gráficos y texto en la pantalla.

import time, math
Importa funciones de tiempo y matemáticas.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

def demo_lineas():
Define una función para mostrar líneas en diferentes posiciones.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

for i in range(0, 128, 16):
Genera valores desde 0 hasta 127 avanzando de 16 en 16.

draw.line([(i, 0), (127-i, 63)], fill=255)
Dibuja líneas diagonales desde la parte superior hacia la inferior.

draw.line([(0, i//2), (127, 63 - i//2)], fill=255)
Dibuja líneas diagonales adicionales usando divisiones enteras.

time.sleep(3)
Mantiene la demostración visible durante 3 segundos.

def demo_rectangulos():
Define una función para mostrar rectángulos.

with canvas(device) as draw:
Abre el área de dibujo.

# Anidados
Comentario que indica que se crearán rectángulos uno dentro de otro.

for i in range(0, 28, 6):
Genera valores de 0 a 27 avanzando de 6 en 6.

draw.rectangle([(i, i//2), (127-i, 63-i//2)], outline=255, fill=0)
Dibuja rectángulos anidados con borde blanco y fondo negro.

# Relleno
Comentario que indica la creación de un rectángulo relleno.

draw.rectangle([(50, 20), (78, 44)], outline=255, fill=255)
Dibuja un rectángulo blanco relleno en el centro.

time.sleep(3)
Mantiene la demostración visible durante 3 segundos.

def demo_circulos():
Define una función para mostrar círculos.

with canvas(device) as draw:
Abre el área de dibujo.

# Círculos concéntricos
Comentario que indica que los círculos compartirán el mismo centro.

cx, cy = 64, 32
Define el centro de los círculos en la pantalla.

for r in range(5, 32, 5):
Genera radios desde 5 hasta 31 avanzando de 5 en 5.

draw.ellipse([(cx-r, cy-r), (cx+r, cy+r)], outline=255, fill=0)
Dibuja círculos usando elipses con borde blanco y sin relleno.

time.sleep(3)
Mantiene la demostración visible durante 3 segundos.

def demo_reloj_analogico():
Define una función para mostrar un reloj analógico.

"""Mini reloj analógico usando arcos y líneas"""
Comentario interno que describe la función.

import datetime
Importa herramientas para manejar fecha y hora.

for _ in range(30):
Repite la actualización del reloj durante 30 ciclos.

now = datetime.datetime.now()
Obtiene la fecha y hora actual.

h_ang = (now.hour % 12) / 12 * 360 - 90
Calcula el ángulo de la manecilla de horas.

m_ang = now.minute / 60 * 360 - 90
Calcula el ángulo de la manecilla de minutos.

s_ang = now.second / 60 * 360 - 90
Calcula el ángulo de la manecilla de segundos.

cx, cy, r = 32, 32, 28
Define el centro y radio del reloj.

with canvas(device) as draw:
Abre el área de dibujo.

draw.ellipse([(cx-r,cy-r),(cx+r,cy+r)], outline=255)
Dibuja el círculo principal del reloj.

# Manecilla hora
Comentario que indica la creación de la manecilla de horas.

hx = cx + int(15*math.cos(math.radians(h_ang)))
Calcula la coordenada X de la manecilla de horas.

hy = cy + int(15*math.sin(math.radians(h_ang)))
Calcula la coordenada Y de la manecilla de horas.

draw.line([(cx,cy),(hx,hy)], fill=255, width=2)
Dibuja la manecilla de horas.

# Manecilla minuto
Comentario que indica la creación de la manecilla de minutos.

mx = cx + int(22*math.cos(math.radians(m_ang)))
Calcula la coordenada X de la manecilla de minutos.

my = cy + int(22*math.sin(math.radians(m_ang)))
Calcula la coordenada Y de la manecilla de minutos.

draw.line([(cx,cy),(mx,my)], fill=255, width=1)
Dibuja la manecilla de minutos.

# Marcadores de hora (12 puntos)
Comentario que indica la creación de los marcadores del reloj.

for deg in range(0, 360, 30):
Genera ángulos cada 30 grados para las 12 horas.

px = cx + int(26*math.cos(math.radians(deg)))
Calcula la posición X de cada marcador.

py = cy + int(26*math.sin(math.radians(deg)))
Calcula la posición Y de cada marcador.

draw.point([(px,py)], fill=255)
Dibuja un punto como marcador de hora.

# Texto digital al lado
Comentario que indica que se mostrará información digital adicional.

draw.text((70, 10), now.strftime('%H:%M'), fill=255)
Muestra la hora digital en formato horas:minutos.

draw.text((70, 24), now.strftime('%S s'), fill=255)
Muestra los segundos actuales.

draw.text((68, 40), 'TESOEM', fill=255)
Muestra el texto "TESOEM" al lado del reloj.

time.sleep(1)
Actualiza el reloj cada segundo.

# Ejecutar demostraciones
Comentario que indica la ejecución de todas las funciones.

demo_lineas()
Ejecuta la demostración de líneas.

demo_rectangulos()
Ejecuta la demostración de rectángulos.

demo_circulos()
Ejecuta la demostración de círculos.

demo_reloj_analogico()
Ejecuta la demostración del reloj analógico.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

4B.py

#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica4b_carga_imagen.py
Comentario con el nombre del archivo del programa.

# Carga una imagen desde disco y la muestra en el OLED
Describe que el programa carga una imagen y la muestra en la pantalla OLED.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from PIL import Image
Importa herramientas para trabajar con imágenes.

import time, os
Importa funciones de tiempo y manejo de archivos del sistema.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

def cargar_y_mostrar(ruta_imagen):
Define una función para cargar y mostrar una imagen.

"""
Inicio del comentario interno de la función.

Carga una imagen, la redimensiona a 128x64 y la convierte al formato monocromático requerido por el SSD1306.
Explica que la imagen será ajustada al tamaño y formato compatible con la pantalla OLED.

"""
Fin del comentario interno.

if not os.path.exists(ruta_imagen):
Verifica si el archivo de imagen existe.

print(f'ERROR: No se encontró {ruta_imagen}')
Muestra un mensaje de error si la imagen no existe.

return
Finaliza la función si no se encuentra la imagen.

# 1. Cargar imagen original
Comentario que indica el primer paso.

img_original = Image.open(ruta_imagen)
Abre la imagen desde el disco.

print(f'Imagen cargada: {img_original.size} modo={img_original.mode}')
Muestra información de la imagen cargada, como tamaño y tipo.

# 2. Redimensionar manteniendo proporción
Comentario que indica el segundo paso.

img_resized = img_original.resize(
Redimensiona la imagen al tamaño de la pantalla OLED.

(device.width, device.height),
Usa el ancho y alto de la pantalla OLED.

Image.Resampling.LANCZOS
Aplica un filtro de alta calidad para mejorar el redimensionamiento.

# Filtro de alta calidad
Comentario que describe el filtro usado.

)
Finaliza la función resize.

# 3. Convertir a escala de grises
Comentario que indica el tercer paso.

img_gray = img_resized.convert('L')
Convierte la imagen a escala de grises.

# 4. Umbralización (threshold): píxeles > 128 = blanco, resto = negro
Comentario que explica la conversión a blanco y negro.

img_mono = img_gray.point(lambda x: 255 if x > 128 else 0, '1')
Convierte la imagen a formato monocromático usando un umbral de 128.

# 5. Mostrar en el display
Comentario que indica el último paso.

device.display(img_mono)
Muestra la imagen monocromática en la pantalla OLED.

print('Imagen mostrada en pantalla OLED.')
Muestra un mensaje indicando que la imagen fue mostrada.

def generar_imagen_prueba():
Define una función para crear una imagen de prueba.

"""Genera una imagen de prueba si no hay archivo disponible"""
Comentario que describe la función.

from PIL import ImageDraw
Importa herramientas para dibujar sobre imágenes.

img = Image.new('L', (128, 64), 0)
Crea una imagen nueva de 128x64 píxeles con fondo negro.

# Fondo negro
Comentario que describe el fondo de la imagen.

draw = ImageDraw.Draw(img)
Crea un objeto de dibujo sobre la imagen.

# Patrón de tablero de ajedrez
Comentario que indica la creación de un patrón visual.

for y in range(0, 64, 8):
Recorre filas cada 8 píxeles.

for x in range(0, 128, 8):
Recorre columnas cada 8 píxeles.

if (x//8 + y//8) % 2 == 0:
Verifica posiciones alternadas para crear el patrón de tablero.

draw.rectangle([(x,y),(x+7,y+7)], fill=200)
Dibuja cuadros claros en posiciones alternadas.

# Logo 'T' al centro
Comentario que indica la creación de una letra T.

draw.rectangle([(50,10),(78,20)], fill=255)
Dibuja la parte superior de la letra T.

draw.rectangle([(60,10),(68,55)], fill=255)
Dibuja la parte vertical de la letra T.

img.save('/tmp/prueba_oled.png')
Guarda la imagen generada en el directorio temporal.

return '/tmp/prueba_oled.png'
Devuelve la ruta de la imagen generada.

# Ruta a la imagen (cambiar por su archivo)
Comentario que indica dónde definir la ruta de la imagen.

ruta = '/tmp/mi_imagen.png'
Guarda la ruta de la imagen que se desea cargar.

if not os.path.exists(ruta):
Verifica si la imagen existe.

print('Archivo no encontrado. Generando imagen de prueba...')
Muestra un mensaje indicando que se generará una imagen de prueba.

ruta = generar_imagen_prueba()
Genera la imagen de prueba y guarda su ruta.

cargar_y_mostrar(ruta)
Carga y muestra la imagen en la pantalla OLED.

time.sleep(10)
Mantiene la imagen visible durante 10 segundos.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.

4C.py
#!/usr/bin/env python3
Indica que el programa debe ejecutarse usando Python 3.

# practica4c_slideshow.py
Comentario con el nombre del archivo del programa.

# Crea un slideshow con múltiples frames generados dinámicamente
Describe que el programa mostrará varias pantallas y animaciones dinámicas en la OLED.

from luma.core.interface.serial import i2c
Importa la comunicación I2C para conectar la pantalla OLED.

from luma.oled.device import ssd1306
Importa el controlador de la pantalla OLED SSD1306.

from luma.core.render import canvas
Importa canvas para dibujar gráficos y texto en pantalla.

from PIL import ImageFont
Importa las fuentes para mostrar texto.

import time, math
Importa funciones de tiempo y matemáticas.

serial = i2c(port=1, address=0x3C)
Configura la conexión I2C usando el puerto 1 y la dirección 0x3C.

device = ssd1306(serial)
Inicializa la pantalla OLED.

font = ImageFont.load_default()
Carga la fuente predeterminada para mostrar texto.

def pantalla_bienvenida():
Define una función para mostrar una pantalla de bienvenida.

with canvas(device) as draw:
Abre un área de dibujo para actualizar la pantalla OLED.

draw.rectangle([(0,0),(127,63)], outline=255)
Dibuja un rectángulo alrededor de toda la pantalla.

draw.text((15, 5), 'BIENVENIDO', font=font, fill=255)
Muestra el texto "BIENVENIDO".

draw.line([(10,17),(118,17)], fill=255)
Dibuja una línea horizontal decorativa.

draw.text((5, 22), 'Practica 4:', font=font, fill=255)
Muestra el texto "Practica 4:".

draw.text((5, 34), 'Graficos OLED',font=font, fill=255)
Muestra el texto "Graficos OLED".

draw.text((5, 48), 'SSD1306', font=font, fill=255)
Muestra el texto "SSD1306".

time.sleep(4)
Mantiene la pantalla de bienvenida visible durante 4 segundos.

def pantalla_ondas():
Define una función para mostrar una animación de ondas.

"""Efecto de onda sinusoidal animada"""
Comentario que describe la animación.

for frame in range(60):
Genera 60 cuadros de animación.

with canvas(device) as draw:
Abre el área de dibujo para cada cuadro.

for x in range(128):
Recorre todas las posiciones horizontales de la pantalla.

y = 32 + int(20 * math.sin((x + frame * 4) * math.pi / 20 ))
Calcula la posición vertical usando una función seno para crear una onda.

if 0 <= y < 64:
Verifica que el punto esté dentro de la pantalla.

draw.point([(x, y)], fill=255)
Dibuja un punto de la onda.

draw.point([(x, y+1)], fill=255)
Dibuja un segundo punto para hacer la onda más gruesa.

time.sleep(0.04)
Controla la velocidad de la animación.

def pantalla_barras():
Define una función para mostrar barras animadas tipo ecualizador.

"""Ecualizador de barras animado"""
Comentario que describe la animación.

import random
Importa funciones para generar números aleatorios.

alturas = [random.randint(10, 60) for _ in range(8)]
Genera alturas aleatorias para 8 barras.

for _ in range(40):
Repite la animación durante 40 cuadros.

# Suavizar transición de alturas
Comentario que indica que las barras cambiarán suavemente.

alturas = [min(60, max(10, h + random.randint(-8, 8))) for h in alturas]
Modifica ligeramente las alturas de las barras manteniéndolas entre 10 y 60 píxeles.

with canvas(device) as draw:
Abre el área de dibujo para actualizar el ecualizador.

draw.text((0, 0), 'Ecualizador', font=font, fill=255)
Muestra el título "Ecualizador".

for i, h in enumerate(alturas):
Recorre cada barra y su altura.

x0 = 5 + i * 15
Calcula la posición horizontal de cada barra.

draw.rectangle([(x0, 63-h), (x0+11, 63)], outline=255, fill=255)
Dibuja una barra vertical rellena.

time.sleep(0.1)
Controla la velocidad de actualización de las barras.

# Secuencia de presentación
Comentario que indica el orden de ejecución de las pantallas.

pantalla_bienvenida()
Ejecuta la pantalla de bienvenida.

pantalla_ondas()
Ejecuta la animación de ondas.

pantalla_barras()
Ejecuta la animación del ecualizador.

device.cleanup()
Limpia y apaga correctamente la pantalla OLED.


Conclusión:
Estos códigos permiten aprender y aplicar el manejo de una pantalla OLED SSD1306 utilizando Python y Raspberry Pi mediante comunicación I2C. A lo largo de las prácticas se trabajó desde funciones básicas, como mostrar texto estático y diferentes tipos de fuentes, hasta funciones más avanzadas como animaciones, efectos visuales, control de contraste, scroll por software y hardware, diseño de interfaces gráficas y manejo de imágenes.
También se implementaron elementos gráficos utilizando primitivas como líneas, rectángulos, círculos y puntos, permitiendo crear relojes analógicos, barras animadas y efectos visuales dinámicos. Además, se aprendió a utilizar funciones matemáticas, ciclos y procesamiento de imágenes para generar contenido visual en tiempo real dentro de la pantalla OLED.






