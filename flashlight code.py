import time
from threading import Thread

import RPi.GPIO as GPIO
import platform

GPIO.setmode(GPIO.BOARD)
button_id = 16
led = 18
GPIO.setup(button_id, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
state = 0
do_blink = False
timed_out = True
is_raspberry = True if platform.uname()[4] != "x86_64" and platform.uname()[4] != "AMD64" else False

keystroke = False


def get_button():
    global state, keystroke
    if is_raspberry:
        button = keystroke
    else:
        button = GPIO.event_detected(button_id)
    # print(button, end='\r')
    if button:
        if is_raspberry:
            keystroke = False
        if timed_out:
            thr = Thread(target=click, daemon=True)
            thr.start()
            if state == 0:
                state = 1
            else:
                state = 0

        elif state == 1:
            state = 2
        else:
            state = 0


def click():
    global timed_out
    timed_out = False
    time.sleep(0.75)
    timed_out = True


def blink():
    global do_blink
    while True:
        if do_blink:
            GPIO.output(led, GPIO.HIGH)
            if is_raspberry:
                print("blink")
            time.sleep(0.002)
            GPIO.output(led, GPIO.LOW)


def main():
    global do_blink
    t1 = Thread(target=blink, daemon=True)
    t1.start()
    GPIO.add_event_detect(button_id, GPIO.RISING)
    while True:
        # print(keystroke)
        get_button()

        if state == 0:
            do_blink = False
            GPIO.output(led, GPIO.LOW)
            if is_raspberry:
                print("off", end='\r')
        elif state == 1:
            do_blink = False
            GPIO.output(led, GPIO.HIGH)
            if is_raspberry:
                print("on", end='\r')
        else:
            do_blink = True


def tester():
    global keystroke
    while True:
        input()
        keystroke = True


if __name__ == "__main__":
    if is_raspberry:
        print("Press any key to simulate a button press")
        keys = Thread(target=tester, daemon=True)
        keys.start()
    main()

