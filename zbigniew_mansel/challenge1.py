input_list = [1,2,3,None,5]


def api_call(a_list):
    counter = 0
    i = 0
    for i in range(len(a_list)):
        if type(a_list[i]) == int:
            counter += 1
    print("Number of numbers: ", counter)

assert api_call(input_list) == 4

