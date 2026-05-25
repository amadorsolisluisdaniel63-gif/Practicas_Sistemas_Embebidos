Práctica 1 Texto en Pantalla
Nombre de la Práctica
Despliegue de Texto Estático y Dinámico en Pantalla OLED SSD1306

Objetivo de la Práctica
Programar la pantalla OLED SSD1306 para mostrar información textual estática y actualizable en distintas posiciones y con distintos valores de contraste, comprendiendo el sistema de coordenadas de la pantalla y el funcionamiento de la fuente bitmap 8×8 del FrameBuffer.

Marco Conceptual
La fuente de texto integrada en MicroPython es una fuente bitmap monoespaciada de 8×8 píxeles. Esto significa que cada carácter ocupa exactamente 8 columnas y 8 filas. La pantalla de 128×64 px puede mostrar como máximo 16 columnas × 8 filas de caracteres (128/8 = 16 cols, 64/8 = 8 filas).
Sistema de coordenadas:  
Origen (0,0) en la esquina superior izquierda.  
Eje X: horizontal, aumenta hacia la derecha (0 a 127).  
Eje Y: vertical, aumenta hacia abajo (0 a 63).  
text(string, x, y, color): x e y son las coordenadas del píxel superior izquierdo del primer carácter.


1A.py
# P1A_texto_basico.py — Texto estático en múltiples líneas → Comentario que indica el nombre y propósito del programa.
from machine import I2C, Pin → Importa las funciones necesarias para usar comunicación I2C y controlar pines del ESP32.
import ssd1306 → Importa la librería de la pantalla OLED SSD1306.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
oled.fill(0) → Limpia la pantalla y la deja completamente negra.
# Línea 1 — título centrado → Comentario que indica que el siguiente texto será el título centrado.
oled.text('TESOEM', 36, 0, 1) → Escribe el texto “TESOEM” en la posición X=36 y Y=0 con color blanco.
# Separador horizontal → Comentario que indica que se dibujará una línea horizontal.
oled.line(0, 10, 127, 10, 1) → Dibuja una línea horizontal desde la coordenada (0,10) hasta (127,10) en color blanco.
# Información en filas → Comentario indicando que se mostrarán datos organizados por filas.
oled.text('Materia:', 0, 16, 1) → Muestra la palabra “Materia:” en la posición X=0 y Y=16.
oled.text('Embebidos', 0, 26, 1) → Muestra el texto “Embebidos” debajo de “Materia:”.
oled.text('Alumno:', 0, 38, 1) → Muestra la palabra “Alumno:” en otra fila.
oled.text('Tu Nombre', 0, 48, 1) → Muestra el nombre del alumno en la última fila.
oled.show() → Actualiza la pantalla OLED para que todo el contenido dibujado aparezca visible.



1B.py
# P1B_contador.py — Actualiza texto dinámicamente (simula sensor) → Comentario que indica que el programa mostrará un contador dinámico en la pantalla OLED simulando datos de un sensor.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para manejar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
contador = 0 → Crea una variable llamada contador e inicia su valor en 0.
while True: → Inicia un ciclo infinito que se ejecutará continuamente.
oled.fill(0) → Limpia la pantalla OLED en cada repetición del ciclo.
oled.text('Contador:', 0, 0, 1) → Muestra el texto “Contador:” en la parte superior izquierda de la pantalla.
oled.text(str(contador), 40, 28, 1) → Convierte el valor del contador a texto y lo muestra en la posición X=40 y Y=28.
oled.text('Presiona RST', 0, 50, 1) → Muestra el mensaje “Presiona RST” en la parte inferior de la pantalla indicando que el botón reset reinicia el programa.
oled.show() → Actualiza la pantalla OLED para mostrar todo el contenido dibujado.
contador += 1 → Incrementa el valor del contador en 1 en cada ciclo.
time.sleep(0.5) → Espera medio segundo antes de repetir el ciclo nuevamente.



1C.py

# P1C_contraste.py — Cicla el brillo de la pantalla → Comentario que indica que el programa cambiará automáticamente el brillo de la pantalla OLED.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para manejar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
oled.fill(0) → Limpia completamente la pantalla OLED.
oled.text('Contraste:', 16, 20, 1) → Muestra el texto “Contraste:” en la posición X=16 y Y=20.
oled.show() → Actualiza la pantalla para mostrar el texto dibujado.
# Barrido de brillo: 0 (mínimo) → 255 (máximo) → 0 → Comentario que explica que el brillo aumentará y disminuirá continuamente.
while True: → Inicia un ciclo infinito que repetirá continuamente el cambio de brillo.
for nivel in range(0, 256, 5): → Crea un ciclo que aumenta el valor del brillo desde 0 hasta 255 en pasos de 5.
oled.contrast(nivel) → Cambia el nivel de contraste o brillo de la pantalla OLED según el valor actual de nivel.
oled.fill(0) → Limpia la pantalla antes de actualizar la información.
oled.text('Brillo:', 16, 20, 1) → Muestra la palabra “Brillo:” en la pantalla.
oled.text(str(nivel), 52, 36, 1) → Convierte el valor actual del brillo a texto y lo muestra en la pantalla.
oled.show() → Actualiza la pantalla OLED para mostrar los cambios realizados.
time.sleep_ms(30) → Espera 30 milisegundos antes de cambiar nuevamente el brillo.
for nivel in range(255, -1, -5): → Crea un ciclo que disminuye el brillo desde 255 hasta 0 en pasos de 5.
oled.contrast(nivel) → Ajusta nuevamente el contraste usando el valor actual de nivel.
oled.fill(0) → Limpia la pantalla antes de actualizar los datos.
oled.text('Brillo:', 16, 20, 1) → Muestra nuevamente la palabra “Brillo:” en la pantalla.
oled.text(str(nivel), 52, 36, 1) → Muestra el valor actual del brillo mientras disminuye.
oled.show() → Actualiza la pantalla OLED con el nuevo valor del brillo.
time.sleep_ms(30) → Espera 30 milisegundos antes de continuar con el siguiente cambio de brillo.



Práctica 2 — Texto con Scrolling
Nombre de la Práctica
Animaciones de Desplazamiento de Texto por Software y por Hardware
Objetivo de la Práctica
Implementar dos técnicas de scrolling en la pantalla OLED SSD1306: 
(a) scrolling por software usando el método scroll() del FrameBuffer para desplazar el contenido del buffer, y (b) scrolling horizontal por hardware activando los registros internos del SSD1306 mediante comandos I2C directos.
Marco Conceptual — Scrolling por Software vs Hardware
El SSD1306 implementa scroll por hardware directamente en el controlador, sin carga adicional para el microcontrolador. Este modo desplaza el contenido visible de la GDDRAM de forma autónoma. El scrolling por software, en cambio, se realiza en el FrameBuffer del ESP32, permitiendo mayor flexibilidad (texto ticker, noticias) pero con mayor carga de CPU y tráfico I2C.

Implementación 
Software: método scroll() del FrameBuffer | Hardware: comandos I2C directos al SSD1306 
Carga CPU 
Software: alta (re-dibuja cada frame) | Hardware: nula (el SSD1306 opera solo) 
Flexibilidad 
Software: total (cualquier velocidad, dirección, texto) | Hardware: limitada (horizontal o diagonal) 
Modificación de texto 
Software: posible en tiempo real | Hardware: no (texto fijo durante scroll) 
Velocidad mínima 
Software: dependiente del loop | Hardware: ~2 fps (configurar intervalo) 


2A.py
# P2A_ticker.py — Texto que se desplaza horizontalmente (ticker) → Comentario que indica que el programa mostrará un texto moviéndose horizontalmente como un letrero electrónico.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
mensaje = ' >>> TESOEM - Sistemas Embebidos - ISC 2025 <<< ' → Guarda en una variable el mensaje que se mostrará desplazándose en la pantalla.
pos_x = 128 → Define la posición horizontal inicial del texto fuera de la pantalla por el lado derecho.
while True: → Inicia un ciclo infinito para que el texto se desplace continuamente.
oled.fill(0) → Limpia la pantalla OLED antes de dibujar el siguiente cuadro de animación.
oled.text(mensaje, pos_x, 28, 1) → Dibuja el mensaje en la posición horizontal indicada por pos_x y en la altura Y=28.
oled.show() → Actualiza la pantalla OLED para mostrar el texto en su nueva posición.
pos_x -= 3 → Reduce la posición horizontal en 3 píxeles para mover el texto hacia la izquierda.
# Reiniciar cuando el texto complete su recorrido → Comentario que explica que el mensaje volverá a iniciar cuando salga completamente de la pantalla.
if pos_x < -(len(mensaje) * 8): → Verifica si todo el texto ya salió de la pantalla por el lado izquierdo. Se multiplica por 8 porque cada carácter ocupa aproximadamente 8 píxeles de ancho.
pos_x = 128 → Reinicia la posición del texto al lado derecho de la pantalla para repetir la animación.
time.sleep_ms(40) → Espera 40 milisegundos antes de mostrar el siguiente movimiento, logrando aproximadamente 25 cuadros por segundo.


2B.py
# P2B_scroll_vertical.py — Lista de items que sube como créditos de película → Comentario que indica que el programa mostrará textos desplazándose verticalmente hacia arriba como créditos de una película.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
noticias = [ → Crea una lista que almacenará varios textos o mensajes.
'Temp: 23 C', → Primer elemento de la lista que muestra la temperatura.
'Humedad: 65%', → Segundo elemento que muestra el porcentaje de humedad.
'Presion: 1013mb', → Tercer elemento que muestra la presión atmosférica.
'Velocidad: 12km/h', → Cuarto elemento que muestra la velocidad del viento.
'Calidad aire: Buena', → Quinto elemento que indica la calidad del aire.
'UV Index: 3', → Sexto elemento que muestra el índice UV.
] → Finaliza la lista de noticias o datos.
# Construir una 'pantalla larga' concatenando todas las noticias → Comentario que explica que se creará una animación larga con todos los textos.
ALTURA_TOTAL = len(noticias) * 10 + 64 → Calcula la altura total del desplazamiento multiplicando la cantidad de líneas por 10 píxeles y agregando espacio extra al final.
for offset in range(ALTURA_TOTAL): → Inicia un ciclo que moverá gradualmente los textos hacia arriba.
oled.fill(0) → Limpia la pantalla OLED antes de dibujar el siguiente cuadro de la animación.
for i, texto in enumerate(noticias): → Recorre cada elemento de la lista obteniendo su posición y contenido.
y = i * 10 - offset + 64 → Calcula la posición vertical de cada texto para crear el efecto de movimiento ascendente.
if -8 < y < 64: → Verifica que el texto esté dentro del área visible de la pantalla antes de dibujarlo.
oled.text(texto, 2, y, 1) → Dibuja el texto en la posición X=2 y en la posición vertical calculada.
oled.show() → Actualiza la pantalla OLED para mostrar los textos en movimiento.
time.sleep_ms(50) → Espera 50 milisegundos antes de mostrar el siguiente cuadro de la animación.


2C.py

# P2C_hw_scroll.py — Scroll horizontal por hardware del SSD1306 → Comentario que indica que el programa realizará un desplazamiento horizontal usando el hardware interno del controlador SSD1306.
# NOTA: Enviar comandos directos requiere el byte de control 0x00 → Comentario que explica que para enviar instrucciones directas al display se necesita usar el byte de control 0x00.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
ADDR = 0x3C → Guarda la dirección I2C de la pantalla OLED. Algunos módulos usan 0x3D.
def cmd(c): → Define una función llamada cmd para enviar comandos directamente al controlador SSD1306.
i2c.writeto(ADDR, bytes([0x00, c])) → Envía un comando al display usando la dirección I2C y el byte de control 0x00.
# Mostrar contenido inicial → Comentario que indica que se mostrará un mensaje inicial en pantalla.
oled.fill(0) → Limpia completamente la pantalla OLED.
oled.text('SCROLL HW', 16, 28, 1) → Muestra el texto “SCROLL HW” en la posición X=16 y Y=28.
oled.show() → Actualiza la pantalla OLED para mostrar el texto.
time.sleep(1) → Espera 1 segundo antes de iniciar el desplazamiento.
# Activar scroll continuo hacia la derecha → Comentario que indica que se iniciará el desplazamiento horizontal automático.
# 0x26=scroll derecho, 0x00=dummy, páginas 0-7, intervalo=5 frames → Explica el significado de los comandos enviados al controlador SSD1306.
cmd(0x26) → Envía el comando para activar el scroll horizontal hacia la derecha.
cmd(0x00) → Envía un byte dummy requerido por el protocolo del SSD1306.
cmd(0x00) → Define la página inicial del scroll en la página 0.
cmd(0x00) → Configura el intervalo de velocidad del desplazamiento en 5 frames.
cmd(0x07) → Define la página final del scroll en la página 7.
cmd(0x00) → Envía otro byte dummy requerido por el controlador.
cmd(0xFF) → Envía un byte dummy adicional requerido para completar la configuración.
cmd(0x2F) → Activa oficialmente el desplazamiento horizontal en la pantalla.
time.sleep(5) → Mantiene el scroll funcionando durante 5 segundos.
# Detener scroll → Comentario que indica que el desplazamiento será detenido.
cmd(0x2E) → Envía el comando para desactivar el scroll horizontal.
oled.fill(0) → Limpia nuevamente la pantalla OLED.
oled.text('Scroll OFF', 12, 28, 1) → Muestra el mensaje “Scroll OFF” indicando que el desplazamiento fue detenido.
oled.show() → Actualiza la pantalla para mostrar el mensaje final.


Práctica 3 — Texto y Manejo de Colores / Inversión
Nombre de la Práctica
Técnicas de Contraste Visual: Inversión, Regiones de Color y Efectos de Atención
Objetivo de la Práctica
Explorar las capacidades de manipulación visual del SSD1306 implementando inversión global de pantalla, inversión de regiones específicas (texto resaltado), animaciones de parpadeo para alertas críticas, y técnicas de 'color sobre negro' vs 'negro sobre blanco' para mejorar la legibilidad de interfaces de usuario en sistemas embebidos.
Marco Conceptual — Color en Pantallas Monocromas
El SSD1306 es estrictamente monocromo: cada píxel solo puede estar encendido (1 = color del LED) o apagado (0 = negro). Sin embargo, es posible crear efectos visuales ricos utilizando:  Inversión global (invert=True): todo el buffer se complementa a nivel de bit, intercambiando píxeles
encendidos y apagados.  Fondos rectangulares: rellenar un rectángulo con 1 (blanco) y luego escribir texto con color=0 (negro)
crea texto oscuro sobre fondo claro.  Parpadeo: alternar invert() o fill() en un temporizador genera efectos de alerta.  Regiones de interés: combinar fill_rect() con text() permite crear botones, etiquetas y paneles de
información.  Módulos bicolor (amarillo/azul): las filas 0-15 emiten luz amarilla y las filas 16-63 emiten luz azul. Usar y=0 para títulos amarillos y y>=16 para contenido azul es una técnica de diseño efectiva.

3A.py

# P3A_inversion.py — Inversión global y efecto de alerta parpadeante → Comentario que indica que el programa mostrará una alerta visual usando inversión de colores y parpadeo en la pantalla OLED.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
def mostrar_info(): → Define una función llamada mostrar_info para mostrar información normal en la pantalla.
oled.fill(0) → Limpia la pantalla dejando el fondo negro.
oled.text('Sistema OK', 16, 20, 1) → Muestra el texto “Sistema OK” en la posición X=16 y Y=20 en color blanco.
oled.text('T: 24.5 C', 20, 36, 1) → Muestra la temperatura simulada en la pantalla.
oled.show() → Actualiza la pantalla OLED para mostrar la información.
def alerta(mensaje, repeticiones=5): → Define una función llamada alerta que mostrará un mensaje parpadeante varias veces.
for _ in range(repeticiones): → Inicia un ciclo que repetirá el efecto de alerta el número de veces indicado.
oled.fill(1) → Llena toda la pantalla de color blanco.
oled.text('! ALERTA !', 16, 8, 0) → Muestra el texto “! ALERTA !” en color negro sobre el fondo blanco.
oled.text(mensaje, 0, 28, 0) → Muestra el mensaje de alerta recibido como parámetro en color negro.
oled.show() → Actualiza la pantalla para mostrar la alerta invertida.
time.sleep_ms(300) → Espera 300 milisegundos antes de cambiar el efecto visual.
oled.fill(0) → Cambia nuevamente el fondo de la pantalla a negro.
oled.text('! ALERTA !', 16, 8, 1) → Muestra el texto “! ALERTA !” en color blanco sobre fondo negro.
oled.text(mensaje, 0, 28, 1) → Muestra el mensaje de alerta en color blanco.
oled.show() → Actualiza la pantalla OLED para mostrar el nuevo estado del parpadeo.
time.sleep_ms(300) → Espera otros 300 milisegundos antes de repetir el ciclo.
# Secuencia de demostración → Comentario que indica el inicio de la demostración del programa.
mostrar_info() → Llama la función que muestra la información normal del sistema.
time.sleep(2) → Espera 2 segundos mostrando la información normal.
alerta('TEMP ALTA!') → Ejecuta la función de alerta mostrando el mensaje “TEMP ALTA!”.
mostrar_info() → Vuelve a mostrar la pantalla normal después de finalizar la alerta.


3B.py

# P3B_paneles.py — Interfaz con regiones de color diferenciadas → Comentario que indica que el programa creará una interfaz gráfica dividida en paneles usando diferentes fondos y textos.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
oled.fill(0) → Limpia la pantalla dejando el fondo completamente negro.
# ── Panel de título (blanco sobre negro, centrado) ── → Comentario que indica la creación de un panel de encabezado.
oled.fill_rect(0, 0, 128, 14, 1) → Dibuja un rectángulo blanco desde la posición (0,0) con ancho de 128 píxeles y altura de 14 píxeles para crear el fondo del título.
oled.text('TESOEM ISC', 16, 3, 0) → Muestra el texto “TESOEM ISC” en color negro sobre el fondo blanco del encabezado.
# ── Separadores ── → Comentario que indica que se dibujarán líneas divisorias.
oled.line(0, 15, 127, 15, 1) → Dibuja una línea horizontal para separar el encabezado del contenido principal.
# ── Panel de datos (texto blanco sobre negro) ── → Comentario que indica la sección de datos del sistema.
oled.text('CPU:', 0, 20, 1) → Muestra la etiqueta “CPU:” en color blanco.
oled.text('78%', 40, 20, 1) → Muestra el porcentaje de uso de CPU.
oled.text('RAM:', 0, 32, 1) → Muestra la etiqueta “RAM:” en otra fila.
oled.text('45%', 40, 32, 1) → Muestra el porcentaje de uso de memoria RAM.
# ── Barra de progreso para CPU ── → Comentario que indica que se dibujará una barra de progreso para CPU.
oled.rect(64, 20, 60, 8, 1) → Dibuja el marco de una barra de progreso en la posición X=64 y Y=20 con tamaño de 60x8 píxeles.
oled.fill_rect(65, 21, int(58 * 0.78), 6, 1) → Rellena la barra de progreso proporcionalmente al 78% de uso de CPU.
# ── Barra de progreso para RAM ── → Comentario que indica que se dibujará una barra de progreso para RAM.
oled.rect(64, 32, 60, 8, 1) → Dibuja el marco de la barra de progreso para RAM.
oled.fill_rect(65, 33, int(58 * 0.45), 6, 1) → Rellena la barra proporcionalmente al 45% de uso de RAM.
# ── Pie de página invertido ── → Comentario que indica que se creará un pie de página con colores invertidos.
oled.fill_rect(0, 52, 128, 12, 1) → Dibuja un rectángulo blanco en la parte inferior de la pantalla para el pie de página.
oled.text('v1.0 Activo', 12, 54, 0) → Muestra el texto “v1.0 Activo” en color negro sobre el fondo blanco.
oled.show() → Actualiza la pantalla OLED para mostrar toda la interfaz gráfica creada.


3C.py

from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.
def dibujar_contenido(modo_oscuro): → Define una función llamada dibujar_contenido que mostrará información dependiendo si el modo oscuro está activado o no.
fondo = 0 if modo_oscuro else 1 → Define el color del fondo: negro si el modo oscuro está activo y blanco si está desactivado.
texto = 1 if modo_oscuro else 0 → Define el color del texto: blanco para modo oscuro y negro para modo claro.
oled.fill(fondo) → Llena toda la pantalla con el color de fondo seleccionado.
oled.text('Modo:', 10, 10, texto) → Muestra la palabra “Modo:” en la posición X=10 y Y=10 usando el color definido para el texto.
etiqueta = 'Oscuro' if modo_oscuro else 'Claro' → Guarda en la variable etiqueta el texto “Oscuro” o “Claro” dependiendo del modo actual.
oled.text(etiqueta, 10, 24, texto) → Muestra el nombre del modo actual en la pantalla.
oled.text('TESOEM 2025', 10, 40, texto) → Muestra el texto “TESOEM 2025” en la parte inferior de la pantalla.
oled.show() → Actualiza la pantalla OLED para mostrar todos los cambios realizados.
modo = True → Inicializa la variable modo en verdadero, comenzando con el modo oscuro activado.
while True: → Inicia un ciclo infinito para alternar continuamente entre modo oscuro y modo claro.
dibujar_contenido(modo) → Llama la función para dibujar el contenido según el modo actual.
time.sleep(2) → Espera 2 segundos antes de cambiar de modo.
modo = not modo → Cambia el valor de la variable modo; si era verdadero pasa a falso y viceversa, alternando entre modo oscuro y claro.



Práctica 4 — Gráficos Simples y Carga de Imágenes
Nombre de la Práctica
Gráficos Vectoriales, Primitivas de Dibujo y Carga de Imágenes Bitmap Monocromas
Objetivo de la Práctica
Implementar un conjunto de primitivas gráficas (líneas, rectángulos, elipses, polígonos simples) para construir interfaces de información visual, y desarrollar la técnica de conversión de imágenes digitales al formato de array de bytes compatible con el FrameBuffer del SSD1306, cargando logos e iconos en la pantalla mediante la función bytearray y blit().
Marco Conceptual — Conversión de Imágenes a Bitmap MonocromoDado que el SSD1306 es una pantalla 1-bit (monocromo), cualquier imagen a mostrar debe convertirse a un array de bytes donde cada bit representa un píxel encendido (1) o apagado (0). El proceso es:  Preparar la imagen: redimensionar al tamaño deseado (ej. 48×48 px), convertir a escala de grises y
aplicar umbral (threshold) para obtener blanco/negro puro.  Serializar a bytes: recorrer la imagen píxel a píxel en orden horizontal. Por cada 8 píxeles, construir un byte donde el bit más significativo (MSB) es el píxel de la izquierda.  Codificar en Python: el resultado es un objeto bytes o bytearray que se pasa a framebuf.FrameBuffer.  Mostrar con blit(): crear un FrameBuffer temporal con la imagen y copiarlo al buffer principal usando
oled.blit().  Herramienta recomendada: img2oled (Python script) o convertidores en línea como image2cpp
(javl.github.io/image2cpp).

4A.py

# P4A_graficos.py — Demostración de primitivas de dibujo → Comentario que indica que el programa mostrará diferentes figuras y gráficos básicos en la pantalla OLED.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
import math → Importa la librería matemática para realizar cálculos geométricos.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.

def demo_lineas(): → Define una función para mostrar líneas en pantalla.
oled.fill(0) → Limpia la pantalla dejando el fondo negro.
oled.text('Lineas', 40, 0, 1) → Muestra el título “Lineas” en la parte superior.
for i in range(0, 128, 16): → Recorre valores desde 0 hasta 128 avanzando de 16 en 16.
oled.line(0, 64, i, 10, 1) → Dibuja líneas desde la esquina inferior izquierda hacia diferentes puntos superiores formando un abanico.
oled.show() → Actualiza la pantalla para mostrar las líneas dibujadas.
time.sleep(2) → Espera 2 segundos antes de pasar a la siguiente demostración.

def demo_rectangulos(): → Define una función para mostrar rectángulos.
oled.fill(0) → Limpia la pantalla OLED.
oled.text('Rectang.', 28, 0, 1) → Muestra el título “Rectang.” en la parte superior.
oled.rect(5, 12, 50, 40, 1) → Dibuja un rectángulo vacío con contorno blanco.
oled.fill_rect(70, 12, 50, 40, 1) → Dibuja un rectángulo completamente relleno de color blanco.
# Texto encima del rectángulo sólido → Comentario indicando que se escribirá texto sobre el rectángulo relleno.
oled.text('OK', 82, 28, 0) → Muestra el texto “OK” en color negro sobre el rectángulo blanco.
oled.show() → Actualiza la pantalla OLED para mostrar los rectángulos.
time.sleep(2) → Espera 2 segundos antes de continuar.

def demo_elipses(): → Define una función para mostrar elipses.
oled.fill(0) → Limpia la pantalla OLED.
oled.text('Elipses', 32, 0, 1) → Muestra el título “Elipses”.
oled.ellipse(32, 40, 28, 20, 1) → Dibuja una elipse vacía centrada en la posición indicada.
oled.ellipse(96, 40, 28, 20, 1, True) → Dibuja una elipse rellena de color blanco.
oled.show() → Actualiza la pantalla para mostrar las elipses.
time.sleep(2) → Espera 2 segundos antes de continuar.

def demo_circulo_manual(cx, cy, r): → Define una función para dibujar círculos manualmente usando coordenadas y píxeles.
# Dibujar círculo con algoritmo de punto medio → Comentario que indica que se usará el algoritmo del punto medio para formar el círculo.
x, y = r, 0 → Inicializa las variables de posición del círculo usando el radio recibido.
while x >= y: → Ejecuta un ciclo mientras el valor de X sea mayor o igual que Y.
for px, py in [(cx+x,cy+y),(cx-x,cy+y),(cx+x,cy-y),(cx-x,cy-y), → Calcula puntos simétricos del círculo respecto al centro.
(cx+y,cy+x),(cx-y,cy+x),(cx+y,cy-x),(cx-y,cy-x)]: → Completa las ocho posiciones simétricas para formar el círculo completo.
oled.pixel(px, py, 1) → Enciende un píxel blanco en cada coordenada calculada.
y += 1 → Incrementa el valor de Y para continuar formando el círculo.
x = int((r*r - y*y)**0.5) → Calcula el nuevo valor de X usando la ecuación del círculo.

def demo_circulos(): → Define una función para mostrar varios círculos.
oled.fill(0) → Limpia la pantalla OLED.
oled.text('Circulos', 28, 0, 1) → Muestra el título “Circulos”.
for radio in range(5, 30, 5): → Recorre diferentes radios desde 5 hasta 25 avanzando de 5 en 5.
demo_circulo_manual(64, 38, radio) → Llama la función para dibujar círculos centrados en la pantalla con diferentes tamaños.
oled.show() → Actualiza la pantalla para mostrar los círculos.
time.sleep(2) → Espera 2 segundos antes de terminar.

# Ejecutar demos en secuencia → Comentario que indica que todas las demostraciones se ejecutarán una tras otra.
demo_lineas() → Ejecuta la demostración de líneas.
demo_rectangulos() → Ejecuta la demostración de rectángulos.
demo_elipses() → Ejecuta la demostración de elipses.
demo_circulos() → Ejecuta la demostración de círculos.



4B.py

# P4B_dashboard.py — Panel de información con gráficos → Comentario que indica que el programa mostrará un panel con información y barras gráficas simulando datos de sensores.
from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import time → Importa la librería de tiempo para usar retardos en el programa.
import random → Importa la librería para generar números aleatorios simulando datos de sensores.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.

def barra(x, y, w, h, porcentaje, label): → Define una función llamada barra para dibujar barras de progreso con etiquetas y porcentajes.
oled.text(label, x, y, 1) → Muestra la etiqueta de la barra en la posición indicada.
oled.rect(x, y+10, w, h, 1) → Dibuja el contorno de la barra de progreso.
relleno = int(w * porcentaje / 100) → Calcula el tamaño del relleno de la barra según el porcentaje recibido.
if relleno > 0: → Verifica que exista al menos un valor para rellenar la barra.
oled.fill_rect(x+1, y+11, relleno-1, h-2, 1) → Rellena la barra proporcionalmente al porcentaje calculado.
oled.text(str(porcentaje)+'%', x+w+2, y+10, 1) → Muestra el porcentaje numérico al lado de la barra.

# Simular valores de sensores → Comentario que indica que se generarán datos simulados.
for _ in range(20): → Ejecuta un ciclo 20 veces para actualizar el dashboard.
temp = random.randint(18, 40) → Genera un valor aleatorio de temperatura entre 18 y 40.
hum = random.randint(30, 90) → Genera un valor aleatorio de humedad entre 30 y 90.
cpu = random.randint(10, 95) → Genera un valor aleatorio de uso de CPU entre 10 y 95.
oled.fill(0) → Limpia la pantalla OLED antes de dibujar nuevos datos.

# Título → Comentario que indica la sección del encabezado.
oled.fill_rect(0, 0, 128, 11, 1) → Dibuja un rectángulo blanco en la parte superior para el encabezado.
oled.text('DASHBOARD', 24, 2, 0) → Muestra el texto “DASHBOARD” en color negro sobre el encabezado blanco.

# Barras de información → Comentario que indica que se mostrarán las barras gráficas.
barra(0, 14, 90, 10, temp, 'T') → Dibuja una barra para la temperatura usando el valor generado aleatoriamente.
barra(0, 30, 90, 10, hum, 'H') → Dibuja una barra para la humedad.
barra(0, 46, 90, 10, cpu, 'C') → Dibuja una barra para el uso de CPU.

oled.show() → Actualiza la pantalla OLED para mostrar toda la información y gráficos.
time.sleep(1) → Espera 1 segundo antes de actualizar nuevamente los datos del dashboard.

4C.py

# P4C_imagen.py — Mostrar logo como array de bytes → Comentario que indica que el programa mostrará una imagen o logo usando un arreglo de bytes en la pantalla OLED.
# El array se genera con image2cpp (javl.github.io/image2cpp) → Comentario que explica que el arreglo de bytes fue generado usando la herramienta online Image2CPP.
# Configuración: 32x32 px, 'Plain bytes', 'Horizontal — 1 bit per pixel' → Indica la configuración usada para convertir la imagen: tamaño de 32x32 píxeles y formato monocromático de 1 bit por píxel.

from machine import I2C, Pin → Importa las librerías necesarias para usar comunicación I2C y controlar los pines del ESP32.
import ssd1306 → Importa la librería para controlar la pantalla OLED SSD1306.
import framebuf → Importa la librería framebuf para manejar imágenes y buffers gráficos.

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000) → Configura la comunicación I2C usando el canal 0, el pin 22 como reloj (SCL), el pin 21 como datos (SDA) y una frecuencia de 400 kHz.
oled = ssd1306.SSD1306_I2C(128, 64, i2c) → Inicializa la pantalla OLED con resolución de 128x64 píxeles usando la conexión I2C configurada.

# ── Array de ejemplo: logo 'T' de TESOEM (32x32) ────────────────── → Comentario que indica que el siguiente arreglo representa un logo en forma de letra “T”.
# Para generar el tuyo: convertir imagen PNG a BMP 1-bit, luego image2cpp → Explica cómo convertir una imagen personalizada a formato compatible con MicroPython y OLED.

logo_bytes = bytearray([ → Crea un arreglo de bytes que almacena la información binaria de la imagen.
0xFF,0xFF,0xFF,0xFF → Valores hexadecimales que representan los píxeles encendidos de la imagen.
# fila 0 — barra horizontal superior → Comentario que explica que esos datos corresponden a la parte superior de la letra “T”.
0x07,0xE0,0x07,0xE0 → Datos binarios que representan el tallo vertical de la letra “T”.
] → Finaliza el arreglo de bytes de la imagen.

# Crear FrameBuffer temporal con la imagen → Comentario que indica que se creará un buffer gráfico temporal usando los datos de la imagen.
logo_fb = framebuf.FrameBuffer(logo_bytes, 32, 32, framebuf.MONO_HLSB) → Convierte el arreglo de bytes en una imagen de 32x32 píxeles usando formato monocromático horizontal de 1 bit.

# Mostrar logo centrado → Comentario que indica que la imagen será mostrada en el centro de la pantalla.
oled.fill(0) → Limpia completamente la pantalla OLED dejando el fondo negro.
oled.blit(logo_fb, 48, 16) → Copia y dibuja la imagen almacenada en logo_fb en la posición X=48 y Y=16 para centrarla en la pantalla.
# centrar: x=(128-32)/2=48, y=(64-32)/2=16 → Explica el cálculo usado para centrar la imagen horizontal y verticalmente.
oled.show() → Actualiza la pantalla OLED para mostrar el logo dibujado.


Conclusión:
Finalmente, la práctica de imágenes mediante arreglos de bytes y framebuf demostró cómo integrar logotipos y gráficos personalizados dentro de proyectos embebidos. En conjunto, todos los ejercicios fortalecieron los conocimientos sobre programación de sistemas embebidos, manejo de dispositivos de visualización y desarrollo de interfaces gráficas básicas para aplicaciones en tiempo real usando MicroPython y ESP32.







