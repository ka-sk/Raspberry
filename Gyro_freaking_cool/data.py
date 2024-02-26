# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_icm20x
import os

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

path = "/home/kask/Python/Raspberry/Gyro_freaking_cool/data"
os.chdir(path)

icm = adafruit_icm20x.ICM20948(i2c)

magnetic = [open(path + "/magnetic_x.txt", "w"), open(path + "/magnetic_y.txt", "w"), open(path + "/magnetic_z.txt", "w")]
gyro = [open(path + "/gyro_x.txt", "w"), open(path + "/gyro_y.txt", "w"), open(path + "/gyro_z.txt", "w")]

init_time = time.perf_counter()

timer = open(path + "/timer.txt", "w")


while time.perf_counter() - init_time < 20:
    os.system("clear")
    for i in range(3):
        magnetic[i].write(str(round(icm.magnetic[i], 3)) + "\n")

        print(round(icm.magnetic[i], 3), end=' ')

        gyro[i].write(str(round(icm.gyro[i], 3)) + "\n")

        print(round(icm.magnetic[i], 3), end=" ")
        print("\n")

    timer.write(str(round(time.perf_counter() - init_time, 3))+'\n')

    time.sleep(0.2)

for i in range(3):
    magnetic[i].close()
    gyro[i].close()
    