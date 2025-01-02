from machine import Pin, SPI, SoftI2C
import random
import vga1_bold_16x32 as font
import gc9a01
import time
import os
import sdcard
from gy50 import GY50

spi = SPI(1, baudrate=60000000, sck=Pin(48), mosi=Pin(38), miso=Pin(47))

tft = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(9 , Pin.OUT),
        cs=Pin(6, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(40, Pin.OUT),
        rotation=0,
        options=0,
        buffer_size=0)
tft.init()
print("MAIN imported")
tft.text(font, "boot...", 18, 96)

#mounted = False
#while not mounted:
#    try: 
#        cs = Pin(7, Pin.OUT)
#        sd = sdcard.SDCard(spi, cs)
#        vfs = os.VfsFat(sd)
#        os.mount(vfs, "/sd")
#        mounted = True
#    except Exception as e:
#        print("SDCard failed:", e)
#        time.sleep(.3)
#
#
#
#
#def doimg(name):
#    jpg_displayed = False
#    while not jpg_displayed:
#        try: 
#            tft.jpg("/sd/"+name,0,0)
#            jpg_displayed = True
#        except:
#            time.sleep(.3)
#

def main():
    tft.init()
    print("start main")
    p0 = Pin(0, Pin.OUT)
    for i in range(10):
        p0.value(i%2)
        time.sleep(0.05)
    i2c = SoftI2C(scl=Pin(1), sda=Pin(2))
    i2c.start()
    addr = i2c.scan()[0]
    gyro = GY50(i2c, addr)
    bg = gc9a01.color565(255,255,75)
    # display is 240 x 240
    #tft.fill_circle(120, 120, 120, bg)
    #doimg("zitrone1.jpg")
    tft.jpg("lemon.jpg",0,0)
    mv = [] # ringpuffer
    answers = (
        "Ja", "Nein", "Vielleicht", "Warum?", "Argh!", "Wegen v=0"
    )
    next_answer = random.choice(answers)
    #os.listdir("/sd")
    while True:
        gxyz = gyro.xyz_values()
        dx,dy,dz = gxyz["x"], gxyz["y"], gxyz["z"]
        max_d = max(abs(dx), abs(dy), abs(dz))
        mv.append(max_d)
        if len(mv) > 40:
            del mv[0]
        avg = sum(mv) / len(mv)
        if avg > 30:
            tft.text(font, "           ", 18, 96, gc9a01.color565(150,0,0),bg)
            next_answer = random.choice(answers)
        else:
            tft.text(font, next_answer+"           ", 18, 96, gc9a01.color565(0,0,0), bg)


        print(
            "  %6.1f  " % gxyz["x"],
            "  %6.1f  " % gxyz["y"],
            "  %6.1f  " % gxyz["z"],
            "  %6.1f  " % max_d,
            "  %6.1f  " % avg
        )
    



main()
