"""
The program records the value of our counter every second to a file
"""
from datetime import datetime
import time

# Open a file with write permissions
f = open("log.txt","w")

# Create the counter and record the data
for i in range(0,10):
    print(datetime.now().strftime('%Y%m%d_%H:%M:%S - '), i)
    f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S - '))
    time.sleep(1)
    f.write(str(i))
    f.write('\n')
# Close the file
f.close()

