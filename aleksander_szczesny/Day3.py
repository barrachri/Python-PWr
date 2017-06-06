counter=5
if counter>1:
    print("Major of 1")

#elif couter ==5
    #print("counter is 5")
else:
    print("Manor of 1")
#while and for
l =[1,2,2,4,2]
#num_elements =len(my_list)
counter = 0
i=0
while i<len(l):
    if l[i]==2:
        counter+=1
    i+=1
print ("Number of 2: ", counter)
string ="olek"
for letter in string:
    print (letter)
else:
    print("fbn")

def MyFunction():
    print("This is Function")
    return "somethin"
MyFunction()
type(MyFunction())

def MySF(name="soem", num=5, y="none"):
    """
    comment
    """
    if number==0:
        print("You put 0")
    print (name)

MySF.__doc__

#capital letter- const
#scoop
GLOB=10
def fync_scoop():
    GLOB=20
    return GLOB
print(GLOB, fync_scoop())


#generators
a_gen = (i for i in range(1000))
next(a_gen)
def Gen(x):
    x=x
    while x<20:
        print("Before yield")
        yield x # it stops
        print ("After yield")
        x+=1
f=Gen(10)#f is generator objects

for i in f:
    print("+++++++++")
    print(i)
    print("---------")
#after u use the gen, u consume it for this varable
#It is being used for f.ex. creating bilions of numbers

f= Gen(18)
next(f)
next(f)
#next(f) - error occures
# modules

import app
app.my_fun()


