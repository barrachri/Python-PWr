input_list=[1,2,3, None, 5]

def api_call(a_list):
    '''This function takes a list of values and then it returns a integer 
    with the number of numbers in that list'''
    x=0
    for i in input_list:
        if type(i)==type(0):
            x+=1
    return x

print(api_call(input_list))

assert api_call(input_list) == 4