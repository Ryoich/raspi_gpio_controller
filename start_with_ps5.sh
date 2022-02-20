#!/bin/sh

bluetoothctl -- connect D0:BC:C1:AE:75:A6

/usr/bin/python /home/pi/raspi_gpio_controller/test.py
