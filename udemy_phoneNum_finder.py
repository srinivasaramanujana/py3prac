# program to extract valid US phone numbers from a text

def isPhoneNumber(text):
    '''
    input(str) -> text
    output(str) -> valid 12 character US phone number; e.g. 123-343-9899
    '''
    if len(text) != 12: # not a valid US phone number size (12)
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # missing first 3 digits
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

#text = '123-343-9899'
#print(isPhoneNumber(text))

message = 'You can call me on 123-432-1212, or on my office phone 453-989-3278'

foundNum = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNum = True
if not foundNum:
    print('Could not find phone number!')
