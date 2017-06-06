input_list = [1,2,3,None,5]

def api_call(a_list):
    """Liczba liczb"""
    counter = 0
    for number in a_list:
        if ((type(number) is int) or (type(number) is float)):
            counter = counter +1
    return(counter)

assert api_call(input_list) == 4

#print(api_call(input_list))
