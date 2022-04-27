import digitalio
import microcontroller

class Button():
    """"Supports the Pico:ed button by ELECFREAKS"""

    def __init__(self,pin:microcontroller.Pin):
        self._pin = digitalio.DigitalInOut(pin)


    def is_pressed(self):
        """Returns True when the key is pressed"""
        return not self._pin.value
