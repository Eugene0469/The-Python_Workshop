'''
The script outputs the current system time
'''
import datetime

# Get the current time and store it in the variable currentTime
currentTime = datetime.datetime.now().time()

#Print out the time only if the script is being executed and not being imported
if __name__ == '__main__':
    print("Current time:", currentTime)
