#!/bin/sh
bluetoothctl -- connect 28:C1:3C:84:68:EE
/usr/bin/python /home/pi/raspi_gpio_controller/test.py
