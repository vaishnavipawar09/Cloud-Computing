import re
import sys

# We are using this regex to extract IP & Hour which is required in this Assignment
IpHourPattern = re.compile(
    '(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')

InputData = sys.stdin.readline()
while InputData:
    ResultFound = IpHourPattern.search(InputData)
    if ResultFound:
        IPAddress, TimeHour = ResultFound.groups()
        print(f'{TimeHour}, {IPAddress}, 1')
    InputData = sys.stdin.readline()
