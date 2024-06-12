
from w1thermsensor import W1ThermSensor, Sensor, Unit
from w1thermsensor.errors import SensorNotReadyError

def get_temperature():
    """getting the temp from sensor in degrees celsius"""
    sensor = W1ThermSensor()
    try:
        temp = sensor.get_temperature(Unit.DEGREES_C)
        return temp
    except SensorNotReadyError:
        print("Sensor is not ready. Waiting...")