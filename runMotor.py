#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from time import sleep

# import numpy
# import random

# import cv2

leds = Leds()

Motor1          = Motor(OUTPUT_A)
Motor2          = Motor(OUTPUT_B)
Motor3          = Motor(OUTPUT_C)

Gyro1           = GyroSensor(INPUT_1)
Gyro2           = GyroSensor(INPUT_2)
TouchSensor1    = TouchSensor(INPUT_3)

# # make sure axis is rotating with a constant velocity
# pos_vec = numpy.linspace(1,10000,num=100)

# while not TouchSensor1.is_pressed:
# #     vel_sp = 500 + random.uniform(-100,100)
# #
# #     m.run_timed(speed_sp=vel_sp)
#     Motor1.run_timed(time_sp=300, speed_sp=-500)
#     Motor2.run_timed(time_sp=300, speed_sp=-500)
#     Motor3.run_timed(time_sp=300, speed_sp=-500)
# #     print(vel_sp)
# #
#     sleep(0.01)

# us = UltrasonicSensor()
# gy = GyroSensor()
#
# Put the US sensor into distance mode.
# us.mode='US-DIST-CM'

# Gyro1.mode='TILT-ANG'

Gyro1.mode='GYRO-ANG'
Gyro2.mode='GYRO-ANG'

# units = us.units
units1 = Gyro1.units
units2 = Gyro2.units

Kp = 0.001

while not TouchSensor1.is_pressed:
    # distance = us.value() / 10  # convert mm to cm
    Gyro1_output = Gyro1.value()
    Gyro2_output = Gyro2.value()
    # print(str(distance) + " " + units)
    print("Gyro 1: %.6f and Gyro 2: %.6f" % (Gyro1_output, Gyro2_output) )
    if Gyro1_output < 60:  # This is an inconveniently large distance
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")

    Motor3.duty_cycle_sp = (Gyro1_output/180)*100

    Motor3.run_direct()

    sleep(0.01)

Motor3.stop()

Sound.beep('finished')
leds.set_color("LEFT", "GREEN")  # set left led green before exiting


