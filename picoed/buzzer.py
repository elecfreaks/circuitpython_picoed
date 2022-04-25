import board
import pwmio
import time

class Note():
    """Supports the Pico:ed display by ELECFREAKS"""
    do = 262
    re = 294
    mi = 330
    fa = 349
    sol = 392
    la = 440
    si = 494

class Buzzer():
    """Supports the Pico:ed display by ELECFREAKS"""

    def __init__(self):
        self.piezo = pwmio.PWMOut(board.BUZZER_GP0, duty_cycle=0,
        frequency=440, variable_frequency=True)

    def play_note(self,note):
        """Use a buzzer to play notes"""
        self.piezo.frequency = note
        self.piezo.duty_cycle = 65535 // 2
        time.sleep(0.25)
        self.piezo.duty_cycle = 0
        time.sleep(0.05)
