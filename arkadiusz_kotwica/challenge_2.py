import random
input_list = [random.randint(-1,1) for i in range(100)]

def api_call(input_list):
    '''This function takes a list of values and then it returns a list with the
    same number of elements [True, False,...] where
    True if element >= 0
    False if element < 0'''
    l=[]

    for i in input_list:
        if i>=0:
            l.append(True)
        else:
            l.append(False)
    return l

l=api_call(input_list)
print(l)

#for i in api_call(input_list):
#   print(api_call(input_list))