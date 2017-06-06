#! /usr/bin/python3.4
print ("Hello Poland")
print("My name is:")
name=input("Your name:")
age=input("Your age:")
print(name,": I am", age," years old")
city = "Wroclaw"
today=29
print("Today is", today,"in",city)
#Output - > Today is 29 in Wroclaw
my_age="21"
your_age= "22"
our_age=my_age+your_age
print(our_age)

country = "Poland"
print(city," is in ",country,)
europe= "Europe"
print(country, "is in", europe)

initial="left"
position = initial
initial = "right"
print(position)
#string3=```Multi line
#        string```
print("First letter:", name[0])
print("Second letter:", name[1])
print("Third letter:", name[2])
print(name[0:3])

for i in range(len(name)):
    print (name[i])

#my_string= "Yoland"
#my_string="P"+my_string[1:]
#print(my_string)
my_string="It5ly"
my_string= my_string[0:2]+"a"+my_string[3:]
print(my_string)

string_1="I live in Italy"
current_country="Poland"
string_1= string_1[0:10]+current_country
print(string_1)
integer_1=1
integer_2="10"
print(integer_1+int(integer_2))
print(str(integer_1)+integer_2)

this_is_a_number=5/2
print(this_is_a_number)
print(type(this_is_a_number))

number=500
to_string=str(number)
print(str(number)[0])
print(to_string[0])


euro=4.3
#1 EUR= 4,3 PLN
euro_in_my_pocket =100
pln_in_my_pocket= euro*euro_in_my_pocket
print(pln_in_my_pocket)


my_first_list=[1,2,3,4,5]
print(my_first_list)
a_mixed_list=[1,2,"Ciao"]
print(a_mixed_list)


empty_list=[]
print(type(empty_list))

new_list=my_first_list+a_mixed_list
print(new_list)
new=my_first_list*5
print(new)
print(my_first_list[::-1])


countries=["Poland","Italy","USA","Germany"]
counter=0
for i in range(len(countries)):
    print(i,countries[i])


for i in range(4):
    print(countries[counter])
    counter=counter+1

print(counter)

for i,v in enumerate(current_country):
    print (i,v)


#initial =["left"]
#position =initial
#initial=["right"]
#print(position)
#change reference


initial =["left"]
position =initial
initial[0]="right"
print(position)
#change object


dicty = {"key":"value", "key1":"value"}
print(dicty["key"])
print(dicty)

l=[1,2,3,4,5]

dicty["sss"]="KeyFromAList"
print(dicty)



for k in dicty:
    print("Key:",k,"Value:", dicty[k])


for k,v in dicty.items():
    print("Key:",k,"Value:",v)


a,b =("a","b")
print(a)
print(b)
