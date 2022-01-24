"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

duration_value = dict()

for entry in calls:
	duration_value[entry[0]] = duration_value.get(entry[0], 0) + int(entry[3])
	duration_value[entry[1]] = duration_value.get(entry[1], 0) + int(entry[3])
	

number = max(duration_value, key = lambda k: duration_value[k])
duration = duration_value[number]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, duration))
