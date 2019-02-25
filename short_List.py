'''
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
'''

def lessThan4(aList):
    '''
    aList: a list of strings
    returns: a list of strings with each string less than 4 characters long
    '''
    short_List = []
    for item in aList:
        if len(item) < 4:
            short_List.append(item)
    return short_List
