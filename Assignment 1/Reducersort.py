import sys

# Initializing a dictionary to hold entries organized by IP__Addresses.
NetworkLogEntries = {}

# Interating through each line from the standard input.
for InputData in sys.stdin:
    InputData = InputData.strip()
    IPAddress, logEntryDetails = InputData.split('\t', 1)
# If the IP__Address doesn't exist in the dictionary, initialize an empty list
    if IPAddress not in NetworkLogEntries:
        NetworkLogEntries[IPAddress] = []
# Appending the log details associated with the IP__Address
    NetworkLogEntries[IPAddress].append(logEntryDetails)

sortedIpAddress = sorted(NetworkLogEntries.keys())

# Printing out the log Details for each IP__Address.
for IPAddress in sortedIpAddress:
    for logEntryDetails in NetworkLogEntries[IPAddress]:
        print(f"{IPAddress} {logEntryDetails}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
