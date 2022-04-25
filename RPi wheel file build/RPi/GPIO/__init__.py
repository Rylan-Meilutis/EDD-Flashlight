"""
Copyright (c) 2012-2019 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import platform

VERSION = '0.7.0'

if platform.uname()[4] != "x86_64" and platform.uname()[4] != "AMD64":
    from RPi._GPIO import *
else:

    def setmode(BOARD):
        return None


    def setup(button_id, IN):
        return None


    def event_detected(button_id):
        return None


    def BOARD():
        return None


    def IN():
        return None


    def OUT():
        return None


    def output(led, HIGH):
        return None


    def HIGH():
        return None


    def LOW():
        return None


    def add_event_detect(button_id, RISING):
        return None


    def RISING():
        return None


    print("You are not running this on a supported device!\nPlease run this on a supported device for functionality.")
