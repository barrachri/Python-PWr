#! /usr/bin/python3.4
input_list = [1,2,3, None, 5]

def api_call(a_list):
    '''This function takes a list of values and then it returns a integer
    with the number of numbers in that list'''
    counter=0
    for i in a_list:
        if type(i)==int:
            counter=counter+1
    return counter

assert api_call(input_list) == 4
