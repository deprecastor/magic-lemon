# magic-lemon
A little project with lemons and ESP32

## Hardware
 - [ESP32-S3-Nano](https://www.waveshare.com/wiki/ESP32-S3-Nano)
 - [GC9A01 1,28" TFT](docs/1_28inchTFT_datasheet.pdf)
 - [L3G4200 Gyroscope](docs/RBS11102-L3G4200_AN3393.pdf)

### Wiring
```
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃ ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐ ┃
            ┃ ┊  ╔══════════════════════════╗    ┊ ┃
            ┃ ┊  ║         ESP32─S3         ║    ┊ ┃
            ┃ └┄┄╢D13  GPIO48    GPIO47  D12╟    ┊ ┃
            ┣━━━━╢3V3            GPIO38  D11╟──┐ ┊ ┃  ╔══════╗
            ┃    ╢B0   GPIO46    GPIO21  D10╟  │ ┊ ┃  ║GC9A01║
            ┃    ╢A0   GPIO1     GPIO18   D9╟  │ ┊ ┗━━╢3V3   ║
╔═══════╗   ┃    ╢A1   GPIO2     GPIO17   D8╟  │ └┄┄┄>╢SCK   ║
║L3G4200║   ┃    ╢A2   GPIO3     GPIO10   D7╟  └─────>╢SDA   ║
║    3V3╟━━━┛    ╢A3   GPIO4     GPIO9    D6╟────────>╢RST   ║
║    SDA╟<>──────╢A4   GPIO11    GPIO8    D5╟────────>╢DC    ║
║    SCL╟<┄┄┄┄┄┄┄╢A5   GPIO12    GPIO7    D4╟  ┏━━━━━━╢GND   ║
║    GND╟━━━┓    ╢A6   GPIO13    GPIO6    D3╟  ┃      ╚══════╝
╚═══════╝   ┃    ╢A7   GPIO14    GPIO5    D2╟  ┃
            ┃    ╢Vbus                   GND╟━━┛
            ┃    ╢B1   GPIO0             RST╟
            ┗━━━━╢GND            GPIO44  RX0╟
                 ╢VIN  GPIO3     GPIO43  TX1╟
                 ╚══════════════════════════╝
```
Not shown: Voltage supply to the ESP on VIN (4-25V, 3V barely works)


## Software
Micropython with display support from https://github.com/russhughes/gc9a01_mpy

Use [esptool](https://github.com/espressif/esptool) to flash the firmware image.

For this particular board, esptool was unable to cleanly enter the bootloader-stage.

But you can manually do that by connecting a button (or jumper wire) between B1 and GND and hold that while pluging the board into USB. Relase button (disconnect jumper), start flashing with esptool.

With micropython installed, you can put the `*.py` and `*.jpg` files on your device with [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)

Or just use your favorite IDE.


### Credits
 - Gyro-lib from https://github.com/kriddaw/L3G4200D
 - lemon.jpg sliced from [Abhijit Tembhekar's Picture](https://commons.wikimedia.org/wiki/File:Lemons_on_white.jpg) CC-BY 2.0

