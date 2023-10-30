import sys
import re
import time
import collections

print(sys.path)

text = 'My phone number is 100 100 100, the country code is 57, my lucky number is 7'

result = re.findall('[0-9]+', text)

print(result)

timestamp = time.time()
local = time.localtime()

result = time.asctime(local)

print(timestamp)
print(result)

numbers = [1, 1, 1, 2, 2, 2, 3, 4, 5, 2, 2, 3, 4, 21]

counter = collections.Counter(numbers)

print(counter)