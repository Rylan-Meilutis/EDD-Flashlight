import platform
import time
from threading import Thread

import RPi.GPIO as GPIO

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
print_statement = ""


def get_button():
    global state, keystroke
    if not is_raspberry:
        button = keystroke
    else:
        button = GPIO.event_detected(button_id)
    if button:
        if not is_raspberry:
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
    global do_blink, print_statement
    while True:
        if do_blink:
            GPIO.output(led, GPIO.HIGH)
            if not is_raspberry:
                print_statement = "blink"
            time.sleep(0.002)
            GPIO.output(led, GPIO.LOW)


def main():
    global do_blink, print_statement
    t1 = Thread(target=blink, daemon=True)
    t1.start()
    GPIO.add_event_detect(button_id, GPIO.RISING)
    while True:
        get_button()

        if state == 0:
            do_blink = False
            GPIO.output(led, GPIO.LOW)
            if not is_raspberry:
                print_statement = "off"
        elif state == 1:
            do_blink = False
            GPIO.output(led, GPIO.HIGH)
            if not is_raspberry:
                print_statement = "on"
        else:
            do_blink = True
        if not is_raspberry:
            print(print_statement, end='\r')


def tester():
    global keystroke
    while True:
        input()
        keystroke = True


if __name__ == "__main__":
    if not is_raspberry:
        print("Press any key to simulate a button press")
        keys = Thread(target=tester, daemon=True)
        keys.start()
    main()
