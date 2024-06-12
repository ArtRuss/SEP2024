import time

#from FrancisLibrary import healthycooking

# returns True if the measured temperature is above or equal to 100 C
def alarm_when_boiling(measured_temperature, user_selection):
    """When the temperature is over user_selection the alrm will be set off"""
    alarm_state = False
    if(measured_temperature >= user_selection):
        alarm_state = True
    return alarm_state

def alarm():
    """creates alarm sound for 5 secounds and pauses then decreases by one secound until 0"""
    for i in range (5):
        #healthycooking.set_alarm(True)
        print(True)
        time.sleep(5 - i)
        #healthycooking.set_alarm(False)
        print(False)
        time.sleep(.5)
    

if __name__ == "__main__":
# infinite loop to keep checking
    temps = [0, 10, 20, 30, 40, 50]
    while True:
# retrieve water temperature

        #measured_temperature = healthycooking.get_temperature()
        measured_temperature = float(input("temp: "))
        print(measured_temperature)
# update the alarm_state
        user_selection = int(input("User Selection: "))
        
        alarm_state = alarm_when_boiling(measured_temperature, temps[user_selection])
# set the alarm according to the alarm_state
        if(alarm_state):
            alarm()
            break
# wait until the next second to review again
        time.sleep(1)