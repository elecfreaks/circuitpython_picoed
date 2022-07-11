# SPDX-FileCopyrightText: Copyright ELECFREAKS
# SPDX-License-Identifier: MIT

"""
`picoed.led`
====================================================

CircuitPython driver for the Pico:ed built-in LED.

"""

import digitalio


class Led:
    """Supports the Pico:ed built-in LED by ELECFREAKS"""

    def __init__(self, pin):
        self._pin = pin
        self._io = None

    def _init(self):
        if not self._io:
            self._io = digitalio.DigitalInOut(self._pin)
            self._io.direction = digitalio.Direction.OUTPUT

    def deinit(self):
        """Destroy the pin."""
        if self._io:
            self._io.deinit()
            self._io = None

    def on(self):
        """Turn on the LED."""
        self._init()
        self._io.value = True

    def off(self):
        """Turn off the LED."""
        self._init()
        self._io.value = False

    def toggle(self):
        """Toggles the LED."""
        self._init()
        self._io.value = not self._io.value
