import _thread
import time

import pyb
from machine import Pin

pin_x1 = pyb.Pin('5', pyb.Pin.IN, pyb.Pin.PULL_DOWN)
led = Pin(20, Pin.OUT)
do_blink = False
state = 0


def flash():
    global do_blink
    while True:
        if do_blink:
            led.value(1)
            time.sleep(0.002)
            led.value(0)


def wait_pin_change(pin):
    # wait for pin to change value
    # it needs to be stable for a continuous 20ms
    cur_value = pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        pyb.delay(1)


def button():
    global state, pin_x1
    while True:
        wait_pin_change(pin_x1)
        state += 1
        if state < 2:
            state = 0


def main():
    global do_blink
    _thread.start_new_thread(flash, ())
    _thread.start_new_thread(button, ())
    while True:
        if state == 0:
            do_blink = False
            led.value(0)
        elif state == 1:
            do_blink = False
            led.value(1)
        elif state == 2:
            do_blink = True
        else:
            do_blink = False
            led.value(0)


if __name__ == "__main__":
    main()