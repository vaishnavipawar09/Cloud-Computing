import sys

# Interating through each line from the standard input.
for InputData in sys.stdin:
    # Eliminate the whitespace at the front and rear.
    CleanedLine = InputData.strip()
    # Based on the spaces, divide the line into words.
    Components = CleanedLine.split()

    # Verify that the line is not empty.
    if Components:
        IPAddress, *remainingParts = Components
        # Print the IP address and the remaining line after that.
        print(f"{IPAddress}\t{' '.join(remainingParts)}")
