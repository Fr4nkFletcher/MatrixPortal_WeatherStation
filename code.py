import time
import board
import terminalio
import displayio
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text import label
import adafruit_bme280.advanced as adafruit_bme280

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)

matrixportal.display.brightness = 0.5

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
bme280.sea_level_pressure = 1013.25

def create_text_label(text, color, x, y, scale=1):
    text_area = label.Label(terminalio.FONT, text=text, color=color, scale=scale)
    text_area.x = x
    text_area.y = y
    return text_area

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# icon bitmaps
temp_icon = [
    0b00111000,
    0b01000100,
    0b01000100,
    0b01000100,
    0b01111100,
    0b01111100,
    0b01111100,
    0b00111000
]

humidity_icon = [
    0b00010000,
    0b00111000,
    0b01111100,
    0b11111110,
    0b11111110,
    0b11111110,
    0b11111110,
    0b01111100
]

pressure_icon = [
    0b00000000,
    0b01100110,
    0b01100110,
    0b01100110,
    0b01100110,
    0b00000000,
    0b01100110,
    0b01100110
]

altitude_icon = [
    0b00010000,
    0b00111000,
    0b01111100,
    0b11111110,
    0b00111000,
    0b00111000,
    0b00111000,
    0b00111000
]

# icon tile
def create_icon(bitmap_data, color):
    bitmap = displayio.Bitmap(8, 8, 2)  # 8x8 pixels, 2 colors
    palette = displayio.Palette(2)
    palette[0] = 0x000000  # Black (off)
    palette[1] = color     # Color (on)

    for y in range(8):
        for x in range(8):
            bitmap[x, y] = (bitmap_data[y] >> (7-x)) & 1

    return bitmap, palette

temp_color = 0xFFFF00  # Yellow
humidity_color = 0x00FFFF  # Cyan
pressure_color = 0xFF00FF  # Magenta
altitude_color = 0x00FF00  # Green

# Create bitmaps and palettes for icons
temp_bitmap, temp_palette = create_icon(temp_icon, temp_color)
humidity_bitmap, humidity_palette = create_icon(humidity_icon, humidity_color)
pressure_bitmap, pressure_palette = create_icon(pressure_icon, pressure_color)
altitude_bitmap, altitude_palette = create_icon(altitude_icon, altitude_color)

# Create TileGrids for each icon
temp_tile = displayio.TileGrid(temp_bitmap, pixel_shader=temp_palette, x=12, y=0)
humidity_tile = displayio.TileGrid(humidity_bitmap, pixel_shader=humidity_palette, x=12, y=8)
pressure_tile = displayio.TileGrid(pressure_bitmap, pixel_shader=pressure_palette, x=12, y=16)
altitude_tile = displayio.TileGrid(altitude_bitmap, pixel_shader=altitude_palette, x=12, y=24)

main_group = displayio.Group()

# Create labels
# for sensor values
temp_value = create_text_label("", temp_color, 22, 4, scale=1)
hum_value = create_text_label("", humidity_color, 22, 12, scale=1)
pres_value = create_text_label("", pressure_color, 22, 20, scale=1)
alt_value = create_text_label("", altitude_color, 22, 28, scale=1)

main_group.append(temp_tile)
main_group.append(humidity_tile)
main_group.append(pressure_tile)
main_group.append(altitude_tile)
main_group.append(temp_value)
main_group.append(hum_value)
main_group.append(pres_value)
main_group.append(alt_value)

matrixportal.display.root_group = main_group

while True:
    temp_f = celsius_to_fahrenheit(bme280.temperature)
    temp_value.text = f"{temp_f:.1f}F"
    hum_value.text = f"{bme280.humidity:.1f}%"
    pres_value.text = f"{bme280.pressure:.0f}hP"
    alt_value.text = f"{bme280.altitude:.0f}m"

    # Refresh the display
    matrixportal.display.refresh()

    time.sleep(2)
