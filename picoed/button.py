import board
import digitalio

class Button():
    """"Supports the Pico:ed display by ELECFREAKS"""

    def __init__(self,button):
        self._buttonPin_A = digitalio.DigitalInOut(board.BUTTON_A)
        self._buttonPin_B = digitalio.DigitalInOut(board.BUTTON_B)
        if button == "A":
            self._buttonPin = "A"
        elif button == "B":
            self._buttonPin = "B"
        elif button == "AB":
            self._buttonPin = "AB"
        else:
            raise ValueError('Parameter error,please select "A", "B", "AB"')
    
    def is_pressed(self):
        if self._buttonPin == "A":
            return self._buttonPin_A.value
        elif self._buttonPin == "B":
            return self._buttonPin_B.value
        elif self._buttonPin == "AB":
            return self._buttonPin_A.value and self._buttonPin_B.value