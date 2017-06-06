input_list = [1,2,3,None,5]

def api_call(a_list):
    '''This function takes a lsit of values and then it returns a integer
    with the number of numbers in the list'''
    counter = 0
    for i in a_list:
        if type(i) == int: counter+=1
    return counter
assert api_call(input_list) == 4