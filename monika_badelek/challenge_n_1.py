input_list = [1,2,3,None,5]

def api_call(a_list):
    """Liczba liczba"""
    counter = 0
    for number in input_list:
        if type(number) == int:
            counter = counter +1
    return(counter)

assert api_call(input_list) == 4

#print(api_call(input_list))
