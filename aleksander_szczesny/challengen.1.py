input_list = [1,2,3, None, 5]

def api_call(a_list):
    """
    
    :param a_list: 
    :return: 
    """
    counter = 0
    i=0
    while i<len(a_list):
    #for i in len(a_list):
        if type(a_list[i])==int:
            counter+=1
    return counter
    #for i in a_list
        #if type(a_list[i])==int:
            #counter+=1
    # put your code here
    # leave the rest
assert api_call(input_list) == 4
print (api_call(input_list))