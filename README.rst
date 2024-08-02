Adafruit MatrixPortal Weather Station
======================================

.. image:: https://github.com/Fr4nkFletcher/Adafruit-MatrixPortal-Weather-Station/blob/main/img/IMG_0524.jpeg
   :alt: Weather Station
   :width: 600px
   :align: left

Overview
--------

An interactive weather station using the Adafruit MatrixPortal M4 and a BME280 sensor to display temperature, humidity, pressure, and altitude on a 64x32 LED matrix.

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/111/881/original/led_matrices_Adafruit_MatrixPortal_M4_Pinout.png
   :alt: Matrix Portal Pinout

Components Required
-------------------

- Adafruit Matrix Portal M4
- 64x32 LED Matrix
- BME280 Sensor
- Jumper wires

.. image:: https://github.com/Fr4nkFletcher/Adafruit-MatrixPortal-Weather-Station/blob/main/img/bme.jpg?raw=true
   :alt: BME pinout
   :width: 300px
   :align: right

Getting Started
---------------

Hardware Setup
~~~~~~~~~~~~~~

1. Connect the Adafruit MatrixPortal M4 to the 64x32 RGB LED matrix.
2. Power the MatrixPortal M4 using a USB-C cable connected to your computer or a power source.

Software Setup
~~~~~~~~~~~~~~

1. Install `CircuitPython <https://circuitpython.org/board/matrixportal_m4/>`_ on the MatrixPortal M4
2. Download the `Adafruit CircuitPython Bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240730/adafruit-circuitpython-bundle-9.x-mpy-20240730.zip>`_
3. Copy the following libraries to the ``lib`` folder on your CIRCUITPY drive:

   * adafruit_matrixportal
   * adafruit_display_text
   * adafruit_bme280
   * adafruit_bus_device
   * adafruit_register

Connect the BME280 Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect the BME280 sensor to the Matrix Portal using I2C:
   - VIN to 3.3V
   - GND to GND
   - SCL to SCL
   - SDA to SDA

Upload the Code
~~~~~~~~~~~~~~~

1. Copy the ``code.py`` file from this repository to your CIRCUITPY drive.
2. The MatrixPortal should do the rest from here, otherwise reset.
