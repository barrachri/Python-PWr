import random
input_list = [random.randint(-1,1) for i in range(100)]

def api_call(input_list):
    '''This function takes a list of values and then it returns a list with the
    same number of elements [True, False,...] where
    True if element >= 0
    False if element < 0'''

    new_list=[]
    for i in input_list:
        if i >= 0:
            new_list.append(True)
        elif i < 0:
            new_list.append(False)
    return new_list

# To print a list
print(api_call(input_list))
