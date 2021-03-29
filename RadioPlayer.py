
from gpiozero import Device, LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import board
import neopixel
import busio
import digitalio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import signal
import time
import pygame
import psutil
import subprocess


BUTTON_GPIO_PIN = 5

Device.pin_factory = PiGPIOFactory()

def pressed():
    print("Button pressed")
    pygame.mixer.music.stop()
  

button = Button(BUTTON_GPIO_PIN, pull_up=True, bounce_time=0.1)
button.when_pressed = pressed

pixel_pin = board.D10
num_pixels = 2
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
pixels[0] = (255, 0, 0)
pixels[1] = (0, 0, 255)
pixels.show()

print("Press button to turn LED on and off. 2")

#i2c = busio.I2C(board.SCL, board.SDA)
#print("i2cscan")
#print(i2c.scan())

p = subprocess.Popen(["ls"])

pygame.mixer.init()
pygame.mixer.music.load("/media/pi/RADIOPLAYER/music/09 Zanzibar.ogg")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()


signal.pause()
