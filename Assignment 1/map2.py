import re
import sys
import os

# Extracted starting hour & ending hour from env variable named Timewindow
startingHour, endingHour = map(int, os.environ.get('timewindow').split("-"))
IpHourPattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?(\d{4}:\d{2}):\d{2}')

for InputData in sys.stdin:
    ResultFound = IpHourPattern.search(InputData)
    if ResultFound:
        IPAddress, Timehour = ResultFound.groups()
        CalHourParts = Timehour.split(':')
        _, _, CalHour = Timehour.partition(':')
        # Extracting the CalculatedHour in terms of integer value
        CalHour = int(CalHour)
        # Checking whether the Calculatedhour fits within the TimeWindow
        if startingHour <= CalHour < endingHour:
            print('Hour:', Timehour, ', IP:', IPAddress, ', 1', sep='')
        else:
            continue
