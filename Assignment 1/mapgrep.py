import sys
import re
import os

# Retrieve the 'search_pattern' from the environment variable.
search_pattern = os.environ.get('search_pattern')
if not search_pattern:
    print("The 'search_pattern' environment variable is not defined")
    sys.exit(1)
Compiledpattern = re.compile(search_pattern)
# Iterate over each line passed to the script via standard input.
for InputData in sys.stdin:
    InputData = InputData.strip()
    # If the compiled pattern is discovered in the line, print it.
    if Compiledpattern.search(InputData):
        print(InputData)
