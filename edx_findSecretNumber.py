# Helper function below
def isMyNumber(x):
    secNum = 10
    if x < secNum:
        return -1
    if x == secNum:
        return 0
    else:
        return 1
# Helper function ends
# --------------------

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    foundNumber = False
    while not foundNumber:
        if isMyNumber(guess) == 0:
            break
        else:
            if isMyNumber(guess) == 1:
                guess -= 1
            if isMyNumber(guess) == -1:
                guess += 1
    return guess
