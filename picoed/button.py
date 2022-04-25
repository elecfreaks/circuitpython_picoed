import board
import digitalio

class Button():
    """"Supports the Pico:ed display by ELECFREAKS"""

    def __init__(self,button):
        if button == "A":
            self.button_pin = digitalio.DigitalInOut(board.BUTTON_A)
        elif button == "B":
            self._button_pin = digitalio.DigitalInOut(board.BUTTON_B)
        else:
            raise ValueError('Parameter error,please select "A", "B"')


    def is_pressed(self):
        """Returns True when the key is pressed"""
        return not self._button_pin.value
