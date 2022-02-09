"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PART - A

codes = set()
fixed_line_calls = 0
f2f = 0

for record in calls:
	caller = record[0]
	receiver = record[1]
	if caller[:5] == "(080)":
		fixed_line_calls += 1
		if '(' in receiver:
			if receiver[1] == '0':
				codes.add(receiver[1:receiver.index(')')])
				if receiver[:5] == "(080)":
					f2f += 1
		elif ' ' in receiver:
			if receiver[0] in ('7', '8', '9'):
				codes.add(receiver[:4])
		else:
			codes.add("140")
	elif ' ' in caller:
		continue
	else:
		if ('(' not in receiver) and (' ' not in receiver):
			f2f += 1

codes = sorted(list(codes))
print("The numbers called by people in Bangalore have codes:")
for numbercode in codes:
	print(numbercode)


# PART - B

percentage_of_f2f = 0
if f2f == 0:
	percentage_of_f2f = 0
else:
	percentage_of_f2f = (f2f / fixed_line_calls) * 100

print("{} percent of calls from fixed lines in Bangalore care calls to other fixed lines in Bangalore".format(round(percentage_of_f2f, 2)))
