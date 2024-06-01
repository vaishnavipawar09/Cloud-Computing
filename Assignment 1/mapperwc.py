#!/usr/bin/env python
import sys
import re

# Initialize a Dictionary to hold count of each word
FreqOfWord = {}

InputDataLines = sys.stdin.readlines()
lineIdx = 0

while lineIdx < len(InputDataLines):
    InputData = InputDataLines[lineIdx].strip()
    ExtractedWords = InputData.split()
    ExtractedWords = re.findall(r'\b\w+\b|\.\w+\b', InputData)
    for wordTerm in ExtractedWords:
        # Update the count for each word
        FreqOfWord[wordTerm] = FreqOfWord.get(wordTerm, 0) + 1
    lineIdx += 1

# Print out the word counts from the FreqOfWordS
for wordTerm, cnt in FreqOfWord.items():
    print(f'{wordTerm}\t{cnt}')
