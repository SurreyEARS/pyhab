import pycom
import machine
import math
import network
import os
import time
import utime
from machine import RTC
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS
from pytracking import Pytrack
from network import WLAN
import gc

wlan = WLAN(mode=WLAN.STA)
wlan.connect('<ssid>', auth=(WLAN.WPA2, '<password>'), timeout=5000)
while not wlan.isconnected():
    machine.idle() # save power while waiting
print('WLAN connection succeeded!')
# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())

pycom.heartbeat(False)
gc.enable()

py = Pytrack()
l76 = L76GNSS(py, timeout=30)
chrono = Timer.Chrono()
chrono.start()
while True:
    print("{} - {}".format(l76.coordinates(), rtc.now()))
