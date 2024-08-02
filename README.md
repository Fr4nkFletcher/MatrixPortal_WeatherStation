# Adafruit Matrix Portal Weather Station

<!-- ![Weather Station](https://example.com/image.png) --> 

## Overview
An interactive weather station using the Adafruit Matrix Portal M4 and a BME280 sensor to display temperature, humidity, pressure, and altitude on a 64x32 LED matrix.

## Components Required
- Adafruit Matrix Portal M4
- 64x32 LED Matrix
- BME280 Sensor
- Jumper wires
- Breadboard (optional)

## Installation and Setup

### Install Libraries
1. Download the required libraries from the [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries).
2. Copy the following libraries to the `lib` folder on your CIRCUITPY drive:
   - adafruit_matrixportal
   - adafruit_display_text
   - adafruit_bme280
   - adafruit_bus_device
   - adafruit_register

### Connect the BME280 Sensor
1. Connect the BME280 sensor to the Matrix Portal using I2C:
   - VIN to 3.3V
   - GND to GND
   - SCL to SCL
   - SDA to SDA

### Upload the Code
1. Copy the `code.py` file from this repository to your CIRCUITPY drive.
2. The MatrixPortal should do the rest from here, but reboot if not.



