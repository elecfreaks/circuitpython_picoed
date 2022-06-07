# SPDX-FileCopyrightText: Copyright ELECFREAKS
# SPDX-License-Identifier: MIT

"""
`picoed`
====================================================

The Pico:ed build-in modules for CircuitPython.

"""

import board
import busio
from .display import Display
from .button import Button

__version__ = "0.1.0"
__repo__ = "https://github.com/elecfreaks/circuitpython_picoed.git"

i2c = busio.I2C(board.SCL, board.SDA)

try:
    # For Pico:ed V2
    internal_i2c = busio.I2C(board.I2C0_SCL, board.I2C0_SDA)
    display = Display(internal_i2c)
except RuntimeError:
    # For Pico:ed V1
    display = Display(i2c)

button_a = Button(board.BUTTON_A)
button_b = Button(board.BUTTON_B)
