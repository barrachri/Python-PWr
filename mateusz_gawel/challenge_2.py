import random

input_list = [random.randint(-1, 1) for i in range(100)]


def api_call(input_list):
    input_list = input_list
    '''This function takes a list of values and then it returns a list with the
    same number of elements [True, False,...] where
    True if element >= 0
    False if element < 0'''
    out = []
    for num in input_list:
        if num >= 0:
            out.append(True)
        else:
            out.append(False)

    return out

test = api_call(input_list)
print(input_list)
print(test)