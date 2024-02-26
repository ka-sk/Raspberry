from gpiozero import Button
from signal import pause

button = Button(4)


def pressed():
    print("Hop!")


def released():
    print("Siup!")


def held():
    print("Wziuuuum!")


button.when_held = held
button.when_activated = pressed
button.when_deactivated = released

pause()
