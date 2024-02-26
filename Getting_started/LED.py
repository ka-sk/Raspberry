from gpiozero import LED

GPIO_PIN = 4

diode = LED(GPIO_PIN)

diode.on()