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


def get_button():
    global state
    button = GPIO.event_detected(button_id)
    if button:
        if timed_out:
            thr = Thread(target=click, daemon=True)
            thr.start()
            if state != 0:
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
    while True:
        if do_blink:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led, GPIO.LOW)


def main():
    global do_blink
    t1 = Thread(target=blink, daemon=True)
    t1.start()
    GPIO.add_event_detect(button_id, GPIO.RISING)
    while True:
        get_button()

        if state == 0:
            do_blink = False
            GPIO.output(led, GPIO.LOW)
        elif state == 1:
            do_blink = False
            GPIO.output(led, GPIO.HIGH)
        else:
            do_blink = True


if __name__ == "__main__":
    main()
