import RPi.GPIO as GPIO

def set_alarm(alarm_state):
    GPIO.setwarnings(False)

    # Set up the GPIO pin
    buzzerPin = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzerPin, GPIO.OUT)
    try:
        if alarm_state:
            GPIO.output(buzzerPin, GPIO.HIGH)  
        else:
            GPIO.output(buzzerPin, GPIO.LOW) 

    except KeyboardInterrupt:
        GPIO.cleanup()
