# Program to get the number of each character in a string.

message = 'It was a dull cold day in April and the clock was striking 5'
count = {} # dictionary as character counter

for char in message.lower():
    count.setdefault(char, 0) # if character not already counted, start its counter from 0
    count[char] += 1

print(count)
