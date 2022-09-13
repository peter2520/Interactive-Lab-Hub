from sqlite3 import DateFromTicks
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import geocoder
from datetime import datetime
import pytz
import random

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
# these setup the code for our buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

cmd = "hostname -I | cut -d' ' -f1"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
geoip = geocoder.ip("me")
city = geoip.city
press_A = 0
press_B = 0

clock_color = "#FFFFFF"
blinking = 0
scale_size = 10

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py

    

    # clock = time.strftime("%H:%M:%S")

    if buttonA.value and not buttonB.value :  # just button B pressed
        # print('in B')
        press_B += 1
    
    if press_B % 5 == 0:
        city = geoip.city
        # clock = time.strftime("%p%I:%M:%S")
        localtime = datetime.now()
        date = localtime.strftime("%a %m/%d/%Y")
    elif press_B % 5 == 1:
        city = "Taipei"
        timezone = pytz.timezone('Asia/Taipei')
        localtime = datetime.now(timezone)
        date = localtime.strftime("%a %m/%d/%Y")
        # clock = localtime.strftime("%p%I:%M:%S")
    elif press_B % 5 == 2:
        city = "Tokyo"
        timezone = pytz.timezone('Asia/Tokyo')
        localtime = datetime.now(timezone)
        date = localtime.strftime("%a %m/%d/%Y")
        # clock = localtime.strftime("%p%I:%M:%S")
    elif press_B % 5 == 3:
        city = "London"
        timezone = pytz.timezone('Europe/London')
        localtime = datetime.now(timezone)
        date = localtime.strftime("%a %m/%d/%Y")
        # clock = localtime.strftime("%p%I:%M:%S")
    elif press_B % 5 == 4:
        city = "Los Angeles"
        timezone = pytz.timezone('America/Los_Angeles')
        localtime = datetime.now(timezone)
        date = localtime.strftime("%a %m/%d/%Y")
        # clock = localtime.strftime("%p%I:%M:%S") 


    if not buttonA.value and buttonB.value:  # just button A pressed
        # print('in A')
        press_A += 1
    if press_A % 2 == 1:
        clock = localtime.strftime("%p%I:%M:%S")
    elif press_A % 2 == 0:
        clock = localtime.strftime("%H:%M:%S")

    if not buttonA.value and not buttonB.value:  # Button A and button B both pressed
        blinking += 1


    if localtime.hour <= 12:
        greetings = "Good Morning!"
        color = "#f6be00"
    elif 12 < localtime.hour <= 18:
        greetings = "Good Afternoon!"
        color = "#ff8200"
    elif 18 < localtime.hour <= 24:
        greetings = "Good Night!"
        color = "#082468"

    y = top
    draw.text((x, y), city, font=font1, fill="#87ceeb")

    # y += font1.getsize(date)[1] + 5
    draw.text((x + 110, y), date, font=font1, fill="#FFFF00")

    y += font1.getsize(date)[1] + 20

    if blinking % 3 == 1:
        clock_color = "#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
        print("inAB_1")
    
    
    if blinking % 3 == 2:
        clock_color = "#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
        # print("inAB_2")
        print(scale_size)
        font2_scale = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", scale_size)
        draw.text((x, y), clock, font=font2_scale, fill=clock_color)
        scale_size += 5
        if scale_size > 40:
            scale_size = 10

    else:
        draw.text((x, y), clock, font=font2, fill=clock_color)

    y += font1.getsize(date)[1] + 45
    draw.text((x, y), greetings, font=font3, fill=color)

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)


