def uniques(s):
    """ (str) -> Boolean
    
    Given a string, determine if it is comprised of all unique characters
    
    >>> uniques('abcde')
    >>> True
    
    >>> uniques('goo')
    >>> False
    """
    if len(s) == 0:
        return True
        
    counter = {}
    
    for i in s:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    
    for j in counter:
        if counter[j] > 1:
            return False
        else:
            continue
    
    return True
