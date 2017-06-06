
import random

input_list = [random.randint(-1, 1) for i in range(100)]


def api_call(input_list):
    """
    
    :param input_list: 
    :return: 
    """
    '''This function takes a list of values and then it returns a list with the
    same number of elements [True, False,...] where
    True if element >= 0
    False if element < 0'''
    output_list=[]
    for i in input_list:
        if i >= 0:
            output_list.append(True)
        else:
            output_list.append(False)
    return output_list
print (input_list) 
print (api_call(input_list))
    # put your code here
    # leave the rest
