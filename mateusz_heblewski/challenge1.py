input_list = [1, 2, 3, None, 5]

def api_call(a_list):
    counter = 0
    for element in input_list:
        if type(element) == int:
            counter += 1
    return counter

assert api_call(input_list) == 4
