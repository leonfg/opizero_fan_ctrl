#coding=utf-8
#!/usr/bin/python
"""
@author: BI1OFX
@contact: leonfg83@163.com
@software: PyCharm
@file: fan_on.py
@time: 2023/5/6 0001 9:20
@desc: fan on
"""

import sys
import time
import os


class GPIO:

    def __init__(self, pin):
        self.pin = str(pin)
        os.system('gpio mode ' + self.pin + ' out')

    def output(self, out_value):
        os.system('gpio write ' + self.pin + ' ' + str(out_value))


def main_proc():
    channel = 6
    gpio = GPIO(channel)
    gpio.output(1)


if __name__ == '__main__':
    main_proc()
