#!/usr/bin/env python3

import argparse
import datetime
import time
import os
import subprocess
import schedule

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


        print("Your alarm is set to : ", set_alarm_value)
        return set_alarm_value 
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")

# Function that reads alarm_file.txt for stored alarm
def read_alarm():

    # reading the alarm from 'alarm_file.txt'
    try:
        with open(ALARM_FILE, "r") as file:
            alarm_read = file.read().strip()
        return alarm_read
    except FileNotFoundError:
       return None
       
def notify():
        subprocess.run(["/usr/bin/notify-send", "--icon=error", "This is your alarm"])


def main():
    parser = argparse.ArgumentParser(description='Description of your alrt application.')
    # Add your custom command-line arguments here, if any
    # parser.add_argument('--example', help='Example argument')



    args = parser.parse_args()

    print("Hello from alrt!")

    set_alarm() 
    alarm_time = read_alarm()






######### this approach uses scheduling #############

    schedule.every().day.at(alarm_time).do(notify)


    while True:
        schedule.run_pending()
        time.sleep(1)




######### not so efficient approach #############
######### this approach uses a loop until the condition reaches which wastes resources #############
    #while True:
    #     # extracting current time of your laptop
    #     current_time = datetime.datetime.now().strftime("%H:%M")
    #     stored_alarm = read_alarm() 

    #     # check alarm against the current time
    #     if current_time == stored_alarm:
    #         subprocess.run(["/usr/bin/notify-send", "--icon=error", "This is your error message ..."])
    #         #print("This is alarm")
    #         break
    #     else:
    #         print("wait for the alarm")
    #         break
            
         
         
             

if __name__ == "__main__":
    main()

