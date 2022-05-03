from machine import Pin

high_level = False
button = Pin(5, Pin.IN, Pin.PULL_UP)

press = False
switch = False


def toggle():
    global switch, button, press, high_level
    press = True if button.value() == 0 else False
    if press:
        if not switch:
            high_level = not high_level
        switch = True

    else:
        switch = False


led = Pin(20, Pin.OUT)

while True:
    toggle()
    if high_level:
        led.value(1)
    else:
        led.value(0)
