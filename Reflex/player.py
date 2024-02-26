from gpiozero import Button
from numpy import mean

import timer


class Player:
    def __init__(self, pin: int):
        self.button = Button(pin)
        self.timer = timer.Timer()
        self.points = 0
        self.mean_time = 0
        self.falstarts = 0

        self.ROUND_TIME = 2

        self.if_round_on = False
        self.button.when_activated = self.pressed

    def pressed(self):
        if self.if_round_on:
            t = self.timer.stop()

            print(self.button.pin)
            print(round(t, 3))

            self.points += (self.ROUND_TIME - t) * 10 / self.ROUND_TIME

            self.mean_time = mean(self.timer.all())

            self.if_round_on = False
        else:
            print("Falstart")
            self.points -= 10
            self.falstarts += 1
        pass

    def round_init(self, init_time=0):
        self.if_round_on = True
        self.timer.start() if init_time == 0 else self.timer.set_init_time(init_time)

    def is_round_on(self):
        return self.if_round_on

    def show_results(self):
        return {'mean time': self.mean_time,
                'points': self.points,
                'falstarts': self.falstarts
                }

    def add_points(self, x):
        self.points += x
