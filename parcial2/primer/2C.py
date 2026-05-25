# P2C_hw_scroll.py — Scroll horizontal por hardware del SSD1306
# NOTA: Enviar comandos directos requiere el byte de control 0x00
from machine import I2C, Pin
import ssd1306
import time
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
ADDR = 0x3C # ajustar si tu módulo usa 0x3D
def cmd(c):
 i2c.writeto(ADDR, bytes([0x00, c]))
# Mostrar contenido inicial
oled.fill(0)

oled.text('SCROLL HW', 16, 28, 1)
oled.show()
time.sleep(1)
# Activar scroll continuo hacia la derecha
# 0x26=scroll derecho, 0x00=dummy, páginas 0-7, intervalo=5 frames
cmd(0x26) # Scroll horizontal derecha
cmd(0x00) # Byte dummy
cmd(0x00) # Página inicial: 0
cmd(0x00) # Intervalo: 5 frames
cmd(0x07) # Página final: 7
cmd(0x00) # Byte dummy
cmd(0xFF) # Byte dummy
cmd(0x2F) # Activar scroll
time.sleep(5)
# Detener scroll
cmd(0x2E) # Desactivar scroll
oled.fill(0)
oled.text('Scroll OFF', 12, 28, 1)
oled.show()
