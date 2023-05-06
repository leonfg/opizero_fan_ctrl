#coding=utf-8
#!/usr/bin/python
"""
@author: BI1OFX
@contact: leonfg83@163.com
@software: PyCharm
@file: fan_thermal_ctl.py
@time: 2023/5/6 0001 8:36
@desc: fan ctrl service
"""

import sys
import os
import time


class GPIO:

    def __init__(self, pin):
        self.pin = str(pin)
        os.system('/usr/bin/gpio mode ' + self.pin + ' out')

    def output(self, out_value):
        os.system('/usr/bin/gpio write ' + self.pin + ' ' + str(out_value))


def cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        return float(f.read())/1000


def main_proc():
    channel = 6

    gpio = GPIO(channel)
    # close air fan first
    gpio.output(0)
    is_close = True
    while True:
        temp = cpu_temp()
        if is_close:
            if temp > 50.0:
                print time.ctime(), temp, '℃ open air fan'
                gpio.output(1)
                is_close = False
        else:
            if temp < 47.0:
                print time.ctime(), temp, '℃ close air fan'
                gpio.output(0)
                is_close = True
        time.sleep(2.0)
        print time.ctime(), temp, '℃'


if __name__ == '__main__':
    main_proc()
