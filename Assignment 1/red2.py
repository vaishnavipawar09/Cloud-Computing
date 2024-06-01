import sys
from collections import defaultdict

# Used IPCountPerHour, to store IPAddress & their Total Occurrences
IPCountPerHour = defaultdict(lambda: defaultdict(int))

for RecordData in sys.stdin:
    RecordData = RecordData.strip()
    TimeByHour, IPAddress, totaloccurrence = RecordData.split(',')
    # Updating the IPAddress with count of occurrences for the specific hour
    IPCountPerHour[TimeByHour][IPAddress] += int(totaloccurrence)

for TimeByHour, AllIPs in IPCountPerHour.items():
    CalHourParts = TimeByHour.split(':')
    CalHour = CalHourParts[2]
    # Sorting the counts in Descending order & Displaying Top 3 IP Addresses
    Top3Ips = sorted(AllIPs.items(), key=lambda x: x[1], reverse=True)[:3]
    # Printing Top3 Hour, IPAddresses and TotalCount
    idx = 0
    while idx < len(Top3Ips):
        IPAddress, total = Top3Ips[idx]
        print(f"Hour: {CalHour}:00 - IP: {IPAddress} - COUNT: {total}")
        idx += 1
print("-------------------------------------------------------")
