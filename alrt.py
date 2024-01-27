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
    user_input = input("Set your alarm (HH:MM:SS): ")

    try:
        time_obj = datetime.datetime.strptime(user_input, "%H:%M:%S")
        set_alarm_value = time_obj.time().strftime("%H:%M:%S")

        with open(ALARM_FILE, "a") as file:
            file.write(set_alarm_value + '\n') # appending the new alarm instead of overwriting it


        print("Your alarm is set to : ", set_alarm_value)
        return set_alarm_value 
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")

# Function that reads alarm_file.txt for stored alarm
#def read_alarm():
#
#    # reading the alarm from 'alarm_file.txt'
#    try:
#        with open(ALARM_FILE, "r") as file:
#            alarm_read = file.read().strip()
#        return alarm_read
#    except FileNotFoundError:
#       return None
       
def notify():
        subprocess.run(["/usr/bin/notify-send", "--icon=error", "This is your alarm\n You should start doing your task instead of getting distracted by things around you"])

#def schedule_alarm(alarm_time):
#    alarm_command = f'/usr/bin/notify-send --icon=error "This is your alarm"'
#    at_command = f'echo "{alarm_command}" | at {alarm_time}'
#    os.system(at_command)





def main():
    parser = argparse.ArgumentParser(description='Description of your alrt application.')
    # Add your custom command-line arguments here, if any
    # parser.add_argument('--example', help='Example argument')



    args = parser.parse_args()

    print("Hello from alrt!")

    set_alarm() 

    with open(ALARM_FILE, 'r') as file:
        alarm_times = file.readlines()
        for alarm_time in alarm_times:
            alarm_time = alarm_time.strip()
            #schedule_alarm(alarm_time)
            schedule_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
            schedule.every().day.at(alarm_time).do(notify)


    #alarm_time = read_alarm()

######### this approach uses scheduling #############


    while True:
        schedule.run_pending()
        time.sleep(1)

######### this approach uses scheduling #############

    # Run the scheduled tasks (notify function)
    # schedule.run_pending()



######### not so efficient approach #############
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
######### not so efficient approach #############
            
         
         
             

if __name__ == "__main__":
    main()

