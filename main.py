import pycom
from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

pycom.heartbeat(False)

py = Pysense()
mp = MPL3115A2(py, mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

print("Temperature:", mp.temperature())
print("Altitude:",mp.altitude())
mpp = MPL3115A2(py, mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
print("Pressure:", mpp.pressure())
print("Temperature:", si.temperature())
print("Humidity:", si.humidity())
print("Light:", lt.light())
print("Acceleration:", li.acceleration())
print("Roll:", li.roll())
print("Pitch:", li.pitch())
print("Battery voltage:", py.read_battery_voltage())
