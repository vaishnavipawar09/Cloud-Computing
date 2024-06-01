import sys
from collections import defaultdict

# We use IPCountPerHour, to store IP_Address & their Total Occurrence
IPCountPerHour = defaultdict(lambda: defaultdict(int))

for RecordData in sys.stdin:
    RecordData = RecordData.strip()
    TimeByHour, IPAddress, totaloccurrence = RecordData.split(',')
    CalHour = TimeByHour.split(':')[0]
    IPCountPerHour[CalHour][IPAddress] += int(totaloccurrence)

IPCountPerHour = list(IPCountPerHour.items())
indx = 0

while indx < len(IPCountPerHour):
    CalHour, AllIPs = IPCountPerHour[indx]
    # Sorting the counts in Descending order & Displaying Top 3 IP Addresses
    Top3Ips = sorted(
        AllIPs.items(), key=lambda item: item[1], reverse=True)[:3]
    # Printing Top3 Hour, IPAddresses and TotalCount
    print("-------------------------------------------------------")

    idx = 0
    while idx < len(Top3Ips):
        IPAddress, total = Top3Ips[idx]
        print(f"Hour: {CalHour}:00 - IP: {IPAddress} - COUNT: {total}")
        idx += 1

    indx += 1

print("-------------------------------------------------------")
