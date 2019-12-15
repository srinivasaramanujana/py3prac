def sum_nested_numlist(L):
    '''
    Function to sum all nums in a nested list
    Input: nested list (lst)
    output: total sum (int)
    '''
    for i in L:
        if isinstance(i, list):
            total += sum_nested_numlist(i)
        else:
            total += i
    return total

nest_lst = [1,2,3,[4,5],6,[7,8]]
print(sum_nested_numlist([nest_lst]))
