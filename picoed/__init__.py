# SPDX-FileCopyrightText: Copyright ELECFREAKS
# SPDX-License-Identifier: MIT

"""
`picoed`
====================================================

The Pico:ed build-in modules for CircuitPython.

"""

import board
import busio
import time
import digitalio
from .display import Display
from .display import Image
from .button import Button

__version__ = "0.1.0"
__repo__ = "https://github.com/elecfreaks/circuitpython_picoed.git"



def get_version():
    charge_pin = digitalio.DigitalInOut(board.VERSION_CHARGE)
    charge_pin.direction = digitalio.Direction.OUTPUT

    check = digitalio.DigitalInOut(board.VERSION_CHECK)
    check.direction = digitalio.Direction.INPUT

    charge_pin.value = True
    time.sleep(0.01)
    charge_pin.value = False
    start_time = time.monotonic()
    i = 0
    while True:
        i += 1
        if i > 3000:
            return float(1)
        if check.value == True:
            end_time = time.monotonic()
            charge_pin.deinit()
            check.deinit()
            charge_time = end_time - start_time
            if  0.04 <= charge_time <= 0.06:
                return float(2)
            else:
                return float(1)

if get_version() == 2:
    i2c = busio.I2C(board.I2C0_SCL, board.I2C0_SDA)
else:
    i2c = busio.I2C(board.SCL, board.SDA)

display = Display(i2c)

button_a = Button(board.BUTTON_A)
button_b = Button(board.BUTTON_B)
