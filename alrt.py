#!/usr/bin/env python3

import argparse
import datetime
import time
import os

ALARM_FILE = 'alarm_file.txt'
# Function to set alarm
def set_alarm():
    

    # Take user input for alarm
    user_input = input("Set your alarm (HH:MM): ")

    try:
        time_obj = datetime.datetime.strptime(user_input, "%H:%M")
        set_alarm_value = time_obj.time().strftime("%H:%M")

        with open(ALARM_FILE, "w") as file:
            file.write(set_alarm_value)


        print("Your alarm: ", set_alarm_value)
        return set_alarm_value 
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")

def main():
    parser = argparse.ArgumentParser(description='Description of your alrt application.')
    # Add your custom command-line arguments here, if any
    # parser.add_argument('--example', help='Example argument')

    args = parser.parse_args()

    # Your application logic goes here
    print("Hello from alrt!")

    alarm_time = set_alarm()

    # extracting current time of your laptop
    current_time = datetime.datetime.now().strftime("%H:%M")

    # check alarm against the current time
    if current_time == alarm_time:
        print("This is alarm")
    else:
        print("Wait for alarm")
    
    
        

if __name__ == "__main__":
    main()

