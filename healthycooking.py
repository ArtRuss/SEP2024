# week 1 healthy cooking solution 

import time 

def check_temp(temp):
    """Check_temp check if the temp is above 100.
    If above 100 it returns True if False it returns
    False.
    """
    if temp >= 100:
        return True
    else:
        return False
    

if __name__ == '__main__':
    alarm = False 
    while True:
        temp = float(input("Enter temp in C: "))
        alarm = check_temp(temp)
        if alarm:
            print("100 temp is reached")
            time.sleep(5)
            break
        else:
            print("The desired temp has not been reached")
        
