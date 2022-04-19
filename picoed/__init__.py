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

__version__ = "0.1.0"
__repo__ = "https://github.com/elecfreaks/circuitpython_picoed.git"

i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c)
