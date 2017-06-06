'''MyName="Aleksander"
print("My name is: ", MyName)
print("20");
MyAge="20";
yourAge="22";
print(MyAge+yourAge);
print("I am ", 20 ,"Years old ")
print("I am ", MyAge ,"Years old ")
city= "wroclaw"
country="Poland"
print(city, " is in ", country)
land="europe"
print(country, " is in ", land);

initial="left"
position = initial;
initial = "right"
print(position)
string = """lol
kek
joke"""
print(string)
print("First letter", MyName[0])
print("Second letter", MyName[1])
print("Third letter", MyName[2])
print("Fourth letter", MyName[3])
#print(MyName[200:6])
country="H"+country[1:];#till the end of the string
print(country);
my_string="It5ly";
my_string=my_string[0:2]+"a"+my_string[3:]
print(my_string)
string_1="I live in Italy"
string_1=string_1[0:10]+country;
print (string_1)

integer_1=1.0
integer_2=5/2
print(integer_1+int(integer_2))
print(type(integer_1))
number = 500;
print(str(number)[0])
'''
'''
euro_in_pocket=100
eur=4.3
pln_in_pocket=euro_in_pocket*eur
print(pln_in_pocket)
'''
'''
list=[3,"hej",3,"gtgt"]
print(type(list))
list2=[1]
new_list=list+list2
print (new_list)
print (new_list[::-1])
'''
countries= ['Poland', 'Italy', 'USA', 'Germany']
counter=0
country="Poland"

for i,coun in enumerate(country):
    print(i+1,coun)

counter =0
for i in range(len(country)):
    print(i, country[i])


for i in country:
    print(i)

initial=["left"]
position = initial;
initial = "right" # we'r changing the referrance
print(position)

initial=["left"]
position = initial;
initial[0] = "right" # we'r changing the object, not referance
print(position)

#dictionaries keys and values
dicty ={"key": "value", "key1": "value2"}
print(dicty["key"])
print(dicty)
l=[1,2,3,4,5]
dicty[1]="KeyFrom"
dicty['ssss']="sckdfvbekgns";
print (dicty)

for k in dicty:
    print("Key: ", k, " Value: ", dicty[k])#we can get only a value of a key
    #print(dir(dicty))
    #print(help(dicty))
    print(dicty.values())

    for k in dicty.values():
        print(k)

    for k in dicty.keys():
        print(k)

    for k,v in dicty.items():
        print("key:", k, "val", v)
        #function, for loop,

    dicty[1]="Me";
    dicty["1"]="You";