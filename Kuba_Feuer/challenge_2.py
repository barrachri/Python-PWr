import random

input_list = [random.randint(-1, 1) for i in range(100)]


def api_call(input_list):
    ilosc = len(input_list)
    nowa_lista = []

    for i in range(0,ilosc):

        if input_list[i] >= 0:
            nowa_lista.append(True)
        else:
            nowa_lista.append(False)

    return nowa_lista

p = api_call(input_list)

print(p)
print(input_list)


    # put your code here
    # leave the rest