#!/usr/bin/env python
import sys

# Initialize the present word and its count
presWord = None
presCount = 0

# Interating through each line from the standard input.
for InputData in sys.stdin:
    InputData = InputData.strip()
    wordTerm, cnt = InputData.split('\t', 1)

# If the count is not a number, skip the line and convert it to an integer.
    try:
        cnt = int(cnt)
    except ValueError:
        continue

# Increase the count if the current word and the new word match.
    if presWord == wordTerm:
        presCount += cnt
    else:
        if presWord:
            print(f'{presWord}\t{presCount}')
            print("-------------------------------")
        # Reset the count and update the current word
        presWord = wordTerm
        presCount = cnt

# After processing each line, output the final word along with its number.
if presWord:
    print(f'{presWord}\t{presCount}')
