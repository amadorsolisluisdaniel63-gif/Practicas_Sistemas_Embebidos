# P3B_paneles.py — Interfaz con regiones de color diferenciadas
from machine import I2C, Pin
import ssd1306
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
# ── Panel de título (blanco sobre negro, centrado) ──
oled.fill_rect(0, 0, 128, 14, 1) # fondo blanco (filas 0-13)
oled.text('TESOEM ISC', 16, 3, 0) # texto negro
# ── Separadores ──
oled.line(0, 15, 127, 15, 1)
# ── Panel de datos (texto blanco sobre negro) ──
oled.text('CPU:', 0, 20, 1)
oled.text('78%', 40, 20, 1)
oled.text('RAM:', 0, 32, 1)
oled.text('45%', 40, 32, 1)
# ── Barra de progreso para CPU ──
oled.rect(64, 20, 60, 8, 1) # marco
oled.fill_rect(65, 21, int(58 * 0.78), 6, 1) # relleno proporcional
# ── Barra de progreso para RAM ──
oled.rect(64, 32, 60, 8, 1)
oled.fill_rect(65, 33, int(58 * 0.45), 6, 1)
# ── Pie de página invertido ──
oled.fill_rect(0, 52, 128, 12, 1)
oled.text('v1.0 Activo', 12, 54, 0)
oled.show()
