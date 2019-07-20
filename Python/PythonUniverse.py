from __future__ import with_statement

'''
Balie - Python tutorial v1.0
Modify code to display code and output
'''


#Input
'''
print("Enter your name:")
x = input()
print("Hello ", x)
'''

#Random
import random
print(random.randrange(1,10))

#module
import bpmodule as bp
bp.greeting('Jonathan')

#Date
import datetime
'''
x = datetime.datetime.now()
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'

print(x.year)
print(x.strftime('%A'))
print(str(x)) # '2012-03-14 09:21:58.130922'
print(repr(x)) # 'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
__repr__ goal is to be unambiguous
__str__ goal is to be readable

#Converting string into datetime #exercise
from datetime import datetime
datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

y = datetime.datetime(2020, 5, 17)
print(y)


import datetime
from datetime import datetime
x = datetime.datetime.now().time()                         # 11:20:08.272239
x = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
x = datetime.datetime.now().time().strftime('%H:%M:%S.%f') # 11:20:08.272239
from time import gmtime, strftime
x = strftime("%Y-%m-%d %H:%M:%S", gmtime())
x = str(datetime.now())
date_time = datetime.datetime.now()
date = date_time.date()  # gives date
time = date_time.time()  # gives time
print (date.year, date.month, date.day)
print (time.hour, time.minute, time.second, time.microsecond)

'''



import time
time.sleep(1) # delays for 5 seconds

#Log Timing:
start = time.time()
#....
#....
delta_sec = int(time.time() - start)

'''
Simple built-in benchmarking tool
% python -m timeit 'r = range(0, 1000)' 'for i in r: pass'
10000 loops, best of 3: 48.4 usec per loop
'''


#Context managers "with" statements

'''
from __future__ import with_statement
SyntaxError: from __future__ imports must occur at the beginning of the file
'''

with open('writer.txt', 'w') as f:
    f.write('hello!')



#Format
whoAmI = 'My name is {name}, I am a {profession}.'
print(whoAmI.format(name = 'Balie', profession = 'Software Programmer'))

#Class
#Parent Class
class Employee:
  def __init__(self, empid, name):
    self.empid = empid
    self.name = name

  def getEMail(self):
    return str(self.empid) + '@cognizant.com'

#Child Class
class SrAssociate(Employee):
  def __init__(self, empid, name, minSalary = 75000):
  	Employee.__init__(self, empid, name)
  	self.minSalary = minSalary

  def getBonus(self):
    return self.minSalary*0.1

#Child Class
class JrAssociate(Employee):
  def __init__(self, empid, name, minSalary = 65000):
  	Employee.__init__(self, empid, name)
  	'''
  	super().__init__(self, empid, name)
  	TypeError: __init__() takes 3 positional arguments but 4 were given
  	'''
  	self.minSalary = minSalary

  def getBonus(self):
    return self.minSalary*0.05

'''
balie = Employee(136168)
TypeError: __init__() missing 1 required positional argument: 'name' 
'''

balie = Employee(136168,'Balie')
print(balie.empid)
print(balie.name)
print(balie.getEMail())

'''
print(balie.minSalary)
AttributeError: 'Employee' object has no attribute 'minSalary'
'''
jude = SrAssociate(136169,'Jude', 80000)
print(jude.empid)
print(jude.name)
print(jude.getEMail())
print(jude.minSalary)
print(jude.getBonus())

if hasattr(jude, 'empid'):
	getattr(jude, 'empid') # same as jude.empid
	setattr(jude, 'empid', 9999) #same as jude.empid = 1111
	delattr(jude, 'empid') # same as del jude.empid

karthi = JrAssociate(136170,'Jude', 60000)

print(karthi.empid)
print(karthi.name)
print(karthi.getEMail())
print(karthi.minSalary)
print(karthi.getBonus())

#Variables
txt = ('No better jewel to be worn'
'Than you'
'No better blessing'
'Than you') #@Notes MultiLine Text needs to be encapsuled in brackets or triple quotes
txt2 = '''No better jewel to be worn
Than you
No better blessing
Than you'''

maritalStatus, visa, city, zipcode = 'married', 'H1B', 'Bentonville', 72712
l_callLog = ['Kalai', 'Dad', 'Ziyad', 'Srini', 'Kalai', 'Shekar', 'Kalai', 'Srini', 'Balu', 'Voicemail']
s_interests = {'BasketBall', 'Music', 'WebApps', 'Swimming', 'Blogging'} #Set has no index function
t_family = ('Sakthivel', 'Banumathi', 'Balasubramanian', 'Sudha', 'Kalai', 'Palani', 'Indhu', 'Pari', 'Venba') # Only index and Count
d_skills = {'SQL' : 8, 'Python': 6, 'Tableau': 5, 'Datastage': 8, 'Data Analytics': 9}

print(d_skills.keys())
print(d_skills.values())
print(d_skills.items())


l1 = l_callLog.copy()
s1 = s_interests.copy()
s2 = frozenset(s_interests) #immutable set
'''
t1 = t_family.copy()
AttributeError: 'tuple' object has no attribute 'copy'
'''
d1 = d_skills.copy()



#Loop
for x in d_skills: #works for all iterables including dict
  print(x)

#nested loops
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
  for y in fruits:
    print(x, y)

for i in reversed(range(1, 10, 2)):
	print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
	print(f)


#from goto import goto, label
'''
ModuleNotFoundError: No module named 'goto'
'''

#Misc

'''
#Manipulating Recursion Limit
sys.setrecursionlimit(1000)
sys.getrecursionlimit() 
'''


#Tuple unpacking:
first,second,*rest = (1,2,3,4,5,6,7,8)
first,*rest,last = (1,2,3,4,5,6,7,8)


#Create new types dynamically
NewType = type("NewType", (object,), {"x": "hello"})
n = NewType()
print(n.x)
 
#which is same as 
class NewType(object):
 	x = "hello"

n = NewType()
print(n.x)



print(type(d_skills))

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple) # John#Peter#Vicky
print(x)

x = "hello"
#if condition returns False, AssertionError is raised:
assert x == "hello", "x should be 'hello'"

import math
raw_data = [56.2, float('NaN'), 51.7]
for value in raw_data:
	if not math.isnan(value):
		print('Numeric Error')

print(["foo", "bar", "baz"].index("bar"))


#Encode Decode

import base64

pwd = 'HiDevil'

x = base64.b64encode(bytes(pwd, 'utf-8'))
print(x)

'''
x = base64.b64encode(pwd)
TypeError: a bytes-like object is required, not 'str'
'''

'''
x = pwd.encode('base64')
LookupError: 'base64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
'''

y = base64.b64decode(x)
print(y)




#Exercise

'''
Given a list of values inputs and a positive integer n, write a function that splits inputs into groups of length n.
For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)].
'''

def groupListItems(inputs, n):
    iters = [iter(inputs)] * n
    print(list(iters))
    return zip(*iters)

for x in groupListItems(range(100), 25):
    print(x)

#Another way???
#How do you split a list into evenly sized chunks?
n = 25
l = [i for i in range(100)]

x = [l[i:i + n] for i in range(0, len(l), n)]
print(x)





#Find length of items in a list without using function:
x = list(map(len, ['abc', 'de', 'fghi']))
#[3, 2, 4]

x = list(map(sum, zip([1, 2, 3], [4, 5, 6])))
#[5, 7, 9]




import itertools 

#Making a flat list out of list of lists in Python

#Warmup
old_list = [1, 2, 3]
new_list = [i for i in old_list]

l = [[1,2,3],[4,5,6], [7], [8,9]]
flattened = lambda l: [item for sublist in l for item in sublist]
print(flattened)
#Or using itertools:
merged = list(itertools.chain(*l))
#Or using reduce
import functools 
from functools import reduce
print(reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], []))
print('------------------------------------------------------------')

#Check if a given key already exists in a dictionary
d = {'a': 1, 'b': 2}
'a' in d # <== evaluates to True
'c' in d # <== evaluates to False

#Fibonacci 
def fib(n): 
     a, b = 0, 1
     while a < n:
         print(a, end=' ') #instead of printing in a new line, a space is added.
         a, b = b, a+b

fib(10)


#Transpose a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#Method 1
print(matrix)
zipped_tuple = list(zip(*matrix))
print(zipped_tuple)

zipped_list = [[row[i] for row in matrix] for i in range(4)]
print(zipped_list)

#Method 2
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
print(transposed)


#You can easily transpose an array with zip.
a = [(1,2), (3,4), (5,6)]
zip(*a)
# [(1, 3, 5), (2, 4, 6)]

#Performance behaviour of InBuilt Functions
import timeit
print(timeit.timeit('pow(1234567890, 2345678901, 17)', number=10000))

#Dict:

#Join all items in a dictionary into a string
myDict = {"name": "John", "country": "Norway"}
mySeparator = "@"
x = mySeparator.join(myDict)
print(x) # name@country

#The fromkeys() method returns a dictionary with the specified keys and values.
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y) # ['key1': 0, 'key2': 0, 'key3': 0]
thisdict = dict.fromkeys(x) # ['key1': None, 'key2': None, 'key3': None]



#String
txt = "Hello, welcome to My world. My name is Balie. My world is beautiful. It is fun."
print(txt.endswith(".")) # True
print(txt.find("welcome")) # 7
print(txt.find("e", 5, 10)) # 8
print(txt.rfind("My")) #46

#Exercise
txt = ",ssaaaww...,,banana,ssaaaww...,,"
x = txt.lstrip(",.asw") #banana
print(x)

#Partition
txt = "I could eat bananas all day"
x = txt.partition("bananas") #('I could eat ', 'bananas', ' all day')
x = txt.partition("apples") # ('I could eat bananas all day', '', '')
"""Search for the word "bananas", and return a tuple with three elements:
1 - everything before the "match"
2 - the "match"
3 - everything after the "match"""

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas") # ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

#Replace
#Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2) # three three was a race horse, two two was one too."

#Split
txt = "welcome to the jungle"
x = txt.split() # ['welcome', 'to', 'the', 'jungle']
txt = "apple#banana#cherry#orange"
x = txt.split("#", 1) # ['apple', 'banana#cherry#orange']
txt = "apple, banana, cherry"
x = txt.rsplit(", ", 1) #['apple, banana', 'cherry']




#Function
def topDictItems(unsortedDict, Qty):
  sortedDict = sorted(unsortedDict, key=unsortedDict.get, reverse=True)
  for x in range(Qty):
  	print(sortedDict[x])
  topDict = sorted(unsortedDict, key=unsortedDict.get, reverse=True)[:5]
  return topDict

topSkills = topDictItems(d_skills, 2)
print(topSkills)

#Pass by reference Vs Pass by value
def update_list(the_list):
    the_list.append('four') # modified in place - Be careful with mutable arguments, multiple calls would load repeatedly

def update_list(the_list):
    the_list = ['Some', 'new', 'values'] #assignment does not override original value


#Unpack Args
def draw_point(x, y):
    print(x, y)

t_args = (3, 4)
d_args = {'y': 3, 'x': 2} #Not positional 

draw_point(*t_args)
draw_point(**d_args)


def foo(*args):
	for a in args:
		print(a)

foo(1) # 1
foo(1,2,3) # 1 2 3

#The **kwargs will give you all keyword arguments

def bar(**kwargs):
	for a in kwargs:
		print (a, kwargs[a])

bar(name='one', age=27)
# age 27, name one






#Slice
#Exercise
a=list('banana')
print(a[::-1])
print(sorted(a)) #Misc


#Map
#map creates a new list by applying a function to every element of the source.
#map(function, iterable) is basically equivalent to: [f(x) for x in iterable]


#pass a function to each element to be processed
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x)) #convert the map into a list, for readability

#Reduce
import functools 
from functools import reduce

#LCM:
from fractions import gcd
def lcm(*args):
    return reduce(lambda a,b: a * b // gcd(a, b), args)

lcm(100, 23, 98) # 112700
lcm(*range(1, 20)) # 232792560

#exercise: turn [1, 2, 3, 4, 5, 6, 7, 8] into 12345678.
x = reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7,8], 0)
print(x)

#Exercise: Find the intersection of N given lists:
input_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
reduce(set.intersection, map(set, input_list)) #set([3, 4, 5])

#exercise: Flatten
print(reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], []))

#Exercise: apply a sequence of functions on a string:
s = "The Quick Brown Fox Jumps Over the Lazy Dog"

color = lambda x: x.replace('brown', 'blue')
speed = lambda x: x.replace('quick', 'slow')
work = lambda x: x.replace('lazy', 'industrious')

fs = [str.lower, color, speed, work, str.title]
call = lambda s, func: func(s)

reduce(call, fs, s) # 'The Slow Blue Fox Jumps Over The Industrious Dog'


#Exercise: get the list with the maximum nth element
reduce(lambda x,y: x if x[2] > y[2] else y,[[1,2,3,4],[5,2,5,7],[1,6,0,2]])
# would return [5, 2, 5, 7] as it is the list with max 3rd element 


#Operators can be called as functions:
import operator
from operator import add
from operator import or_
from operator import and_
print (reduce(add, [1,2,3,4,5,6]))

#Union or Intersection of sets:
reduce(operator.or_, ({1}, {1, 2}, {1, 3}))  # union {1, 2, 3}
reduce(operator.and_, ({1}, {1, 2}, {1, 3}))  # intersection {1}

#find the MIN/MAX values in each month across the different years
from collections import Counter

stat2011 = Counter({"January": 12, "February": 20, "March": 50, "April": 70, "May": 15,
           "June": 35, "July": 30, "August": 15, "September": 20, "October": 60,
           "November": 13, "December": 50})

stat2012 = Counter({"January": 36, "February": 15, "March": 50, "April": 10, "May": 90,
           "June": 25, "July": 35, "August": 15, "September": 20, "October": 30,
           "November": 10, "December": 25})

stat2013 = Counter({"January": 10, "February": 60, "March": 90, "April": 10, "May": 80,
           "June": 50, "July": 30, "August": 15, "September": 20, "October": 75,
           "November": 60, "December": 15})

stat_list = [stat2011, stat2012, stat2013]

print (reduce(lambda x, y: x & y, stat_list))     # MIN
print (reduce(lambda x, y: x | y, stat_list))     # MAX
print('-------------------------------------------------------------------------------------------------')

l = [[i] for i in range(10)]
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b, l)) 
# Check result ????????

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b, l)) 

from operator import add,mul
reduce(add,[1,2,3,4]) #10
reduce(mul,[1,2,3,4]) #24
reduce(add,[[1,2,3,4],[1,2,3,4]]) # [1, 2, 3, 4, 1, 2, 3, 4]



#zip
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
"""The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator."""

#use the tuple() function to display a readable version of the result:
print(tuple(x))

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}?  It is {1}.'.format(q, a))


#Filter
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages) 

for x in adults:
  print(x)


#Oops
x = isinstance(5, int) #The issubclass() function, to check if an object is a subclass of another object.
x = isinstance("Hello", (float, int, str, list, dict, tuple))
x = issubclass(SrAssociate, Employee) #The issubclass() function checks if the specified object is a subclass of the specified object



#lambda
#non-named non-reusable functions to implement simpler functionality
l_sqrt = [(lambda x: x*x)(x) for x in range(10)]
print(l_sqrt)

for i in [x*x for x in range(10)]:
	print(i)

xs = range(1,5)
ys = [ i*10 for i in range(1,6) ]
result = list(map(lambda x,y: x+y, xs, ys))
print(result)

'''
@Notes: Forward referencing
balie['skillLevel'] = 'B'
NameError: name 'balie' is not defined
'''

#Dict
carProfile =	dict(brand='Toyota', model='Camry', year=2014, miles = 50000, color= 'grey') #constructor

print(carProfile)

balieProfile = {
  'name': 'Balie',
  'age': 36,
  'married' : True,
  'country': 'India',
  'company': 'Cognizant',
  'experience': 13.5,
  'department': 'AIM',
  'dummyprop': 'dummyval',
  'children': ('Ann','Billy'),
  'pets': None,
  'cars': [
    {'model': 'BMW 230', 'mpg': 27.5},
    {'model': 'Ford Edge', 'mpg': 24.1}
  ]
}


'''
missing commas separator for property
'dummyprop': 'dummyval'
SyntaxError: invalid syntax
'''

print(balieProfile.get('experience')) # avoids KeyErrors: if key is not found no error raised unlike balieProfile['experience'] 
print(len(balieProfile))


#Add
l_callLog.append('Mommy')
l_callLog.append(['Append1','Append2']) # l_callLog.remove(['Append1', 'Append2'])
l_callLog.extend(['Extend1','Extend2'])
'''
@Notes
The append is a built-in function in Python that is used to add its arguments as a single element to the end of the list. 
When using append, the length of the list will increase by one.
The extend is a built-in function in Python that iterates over its arguments adding each element to the list while extending it.
When using extend, the length of the list will increase by how many elements were passed in the argument.
'''
l_callLog.insert(0,'Mommy') #List is an Array, ordered and supports index 
s_interests.add('Cooking') #Add one item
s_interests.update('Trekking', 'Tutoring') #Add multiple items
carProfile['engine'] = 'v6'

'''
print(reverse(l_callLog))
NameError: name 'reverse' is not defined
'''

'''
print(l_callLog.reverse())
None
.reverse() function changes the list in place. It does not return the list
'''
l_callLog.reverse()
l_rev = reversed(l_callLog)


'''
l_callLog.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
'''
l_callLog.remove(['Append1', 'Append2'])
l_callLog.sort()
print(l_callLog)



#Update
l_callLog[0] = 'Kalai_updated'
'''
t_family[0] = 'Sakthivel_updated'
TypeError: 'tuple' object does not support item assignment
'''
carProfile['color'] = 'Grey_updated'
carProfile.update({'color': 'Green_updated'})
jude.name += ' Vijay'
print(jude.name)


#Delete
l_callLog.remove('Mommy') #Delete by item : Deletes only first occurence
l_callLog.pop() #popped value can be captured in a variable for processing. Deleted value is not.
l_callLog.pop(2)
del l_callLog[3] #Delete by Index

s_interests.remove('Cooking') #Raises an error if item doesn't exist
s_interests.discard('Destroyiong the Planet') #Doesn't raise an error if item doesn't exist
#@Notes Discard is 'delete if exists - doesn't throw error if object doesn't exist. Remove is Delete - Fails if object doesn;t exist'

'''
del balieProfile.department 
AttributeError: 'dict' object has no attribute 'department'
@Notes #works only for object.property, not dict items.
'''

del balieProfile['department']
balieProfile.pop('dummyprop') # removes specified item
x = balieProfile.popitem()  # Removes the last inserted key-value pair
del jude.name



'''
l_callLog.pop(25)
IndexError: pop index out of range
'''

print(l_callLog)



#Check number of skills
'''
v_skillCount = d_skills.count()
AttributeError: 'dict' object has no attribute 'count'
'''
v_skillCount = 0
v_skillList = []
v_skillScore = []

'''
    for k, v in d_skills:
ValueError: too many values to unpack (expected 2)
'''

for k, v in d_skills.items():
	v_skillCount += 1
	v_skillList.append(k)
	v_skillScore.append(v)

if v_skillCount > 7:
	balieProfile['skillLevel'] = 'A'
elif v_skillCount >= 4 and v_skillCount <= 7:
	balieProfile['skillLevel'] = 'B'
else:
	balieProfile['skillLevel'] = 'C'


'''
balieProfile['skillLevel'] = 'Good' if v_skillCount > 7 else balieProfile['skillLevel'] = 'Average'
SyntaxError: can't assign to conditional expression
'''
print('10 is greater') if 10 > 5 else print('5 is greater')

#Conditional Assignment:
balieProfile['skillLevel'] = 'A' if (v_skillCount > 7) else 'B' if (v_skillCount >= 4 and v_skillCount <= 7) else 'C'
# (func1 if y == 1 else func2)(arg1, arg2) 
# x = (class1 if y == 1 else class2)(arg1, arg2)



if 'Tableau' in v_skillList:
  print('Tableau skill set available')





#Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myClass = MyNumbers()
myIter = iter(myClass)

for x in myIter:
  print(x)

'''
iter() can take a callable argument
The iter(callable, until_value) function repeatedly calls callable and yields its result until until_value is returned.
for c in iter(lambda: f.read(1),'\n'):
'''


#Array
txt = 'My name is Balie Pages'
print(txt)
print(txt[0])
print(txt[1:25])

txt[-1]    # last item in the array
txt[-2:]   # last two items in the array
txt[:-2]   # everything except the last two items
'''
txt[1000]
IndexError: list index out of range
'''

#Set 
#No Duplicates
s1 = {'apple', 'orange', 'pear', 'banana'}
s2 = set([1,2,3,4,5,6,'apple','orange',1,2,3,45,6,]) #using constructor
s3 = set('123456789') #Convert String to Set
result = s1.issubset(s2)
result = s1.issuperset(s2)
result = s1.isdisjoint(s2)
print(result)

print(s1-s2)
print(s1.difference(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 & s2)
print(s1.intersection(s2))

print(s1 ^ s2)
print(s1.symmetric_difference(s2))

#Comprehension

#Dict Comprehension
a = {i: i**2 for i in range(5)} #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#Set Comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'} #Set Comprehension
a = {i**2 for i in range(5)} #set([0, 1, 4, 16, 9])

#List Comprehension
l=[(1,2),(3,4)]
a = [a+b for a,b in l ] # [3,7]

#primes_cubed = [x*x*x for x in range(1000) if prime(x)]

 
l = list('baliepages')
print(l)
print ('----------------------------------------------')
'''
my_list = [x for x in l if x.attribute == 'e']
AttributeError: 'str' object has no attribute 'attribute'
'''
my_list = [x for x in l if x == 'e']
print (my_list)
my_list = list(filter(lambda x: x == 'e', l))
print (my_list)

print ('----------------------------------------------')

combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x, y))
print(combs)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

#Interleaving for and if
x = [(x, y) for x in range(4) if x % 2 == 1 for y in range(4)]
print(x)

#List
#Using Lists as Stacks 
#appned and pop --> Last In First Out

#Using Lists as Queues
#First In First Out

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # Eric leaves
queue.popleft()                 # John leaves
print(queue)                    # ['Michael', 'Terry', 'Graham']



#Dict

thisdict =	{
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

for x in thisdict:
  print(x) # Prints brand model year
for x in thisdict:
  print(thisdict[x]) #Prints Ford Mustand 1964
for x in thisdict.values():
  print(x) #Prints Ford Mustand 1964
for x, y in thisdict.items():
  print(x, y)
for x in thisdict.items():
  print(x)


print(thisdict.get('model'))


#Exception
try:
  print(x)
except (KeyboardInterrupt, EOFError) as err:
  print(err)
  print('caught this error: ' + repr(error))
  print(err.args)
  quit(0)
  if is_fatal(e):
  	raise
except:
  print('Something else went wrong')
else:
  print('Nothing went wrong')
finally:
  print('The \'try except\' is finished') #This can be useful to close objects and clean up resources

#Raise Exception
n = 10
if n < 1:
	raise ValueError('n must be >= 0')
if n > 1000:
	raise OverflowError('n too large')


#Generator:

#Generators are iterators, but you can only iterate over them once. 
#It's because they do not store all the values in memory, they generate the values on the fly.

mygenerator = (x*x for x in range(3))
for i in mygenerator:
	print(i)


v_matrix = ((a,b) for a in range(0,2) for b in range(4,6))
for x in v_matrix:
	print(x)
'''
The advantage of this is that you dont need intermediate storage, which you would need if you did
x = [(a,b) for a in range(0,2) for b in range(4,6)]
'''

#yield is a keyword that is used like return, except the function will return a generator. 
def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i

mygenerator = createGenerator()
for i in mygenerator:
	print(i)



#Decorator
'''
Decorators allow to wrap a function or method in another function that can add functionality, modify arguments or results, etc. You write decorators one line above the function definition, beginning with an "at" sign (@).
Example shows a print_args decorator that prints the decorated functions arguments before calling it:
'''

def sayhello(name):
	print("Hello " + name)

def decor(func):
	def wrap(*args, **kwargs):
		print('------*****------')
		print(args, kwargs)
		func(*args)
		print('------*****------')
	return wrap

sayhello = decor(sayhello)
sayhello('Balie')
'''
TypeError: wrap() takes 0 positional arguments but 1 was given
'''



#File

for line in open('demofile.txt'):
    print(line)
#which is equivalent (but better) to:

f = open('demofile.txt', 'r')
for line in f.readlines():
   print(line)
f.close()

#Copy File
from shutil import copyfile
copyfile('C:/python/demofile.txt', 'C:/python/Archive/newname1.txt')
'''
copyfile('C:/python/demofile.txt', 'C:/python/Archive/newname.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:/python/demofile.txt'
'''

print('------------------------------------------------------------')
#copy2 allows dst to be a directory (instead of the complete target filename), in which case the basename of src is used for creating the new file;
import shutil
shutil.copy2('C:/python/demofile.txt', 'C:/python/Archive/newname2.txt') # complete target filename given
shutil.copy2('C:/python/demofile.txt', 'C:/python/Archive') # target filename is /dst/dir/file.txt
print('------------------------------------------------------------')

try:
  f = open('demofile.txt', 'r')
  '''
  iter() can take a callable argument
  The iter(callable, until_value) function repeatedly calls callable and yields its result until until_value is returned.
  '''
  for l in iter(lambda: f.read(1),'\n'):
  	print(l)

  #f.write('Some random Stuff \n')
  '''
  io.UnsupportedOperation: not writable
  '''
  print(f.read(5)) #@Notes: Captures first 5 characters
  print(f.readline()) #@Notes: Captures Rest of firstline
  print(f.read()) #@Notes: Writes everything from secondline. Readline() flushes out the content after writing
  print(f.read(5)) #@Notes: Captures nothing: Buffer flushed already
  
  for x in f: #loop through file line by line
  	print(x) #@Notes: Captures nothing: Buffer flushed already
  '''
  IndentationError: expected an indented block
  '''
  f.flush() #clear the buffer when writing to a file
  f.seek(4)
  f.truncate(20) 
  f.write("\nSee you soon!")
  f.writelines(["\nIn and Out!", "\nOver and out."])
except:
  print('Something went wrong')
finally:
  print('Good bye')
  '''
  if f.isopen():
  	f.close()
	AttributeError: '_io.TextIOWrapper' object has no attribute 'isopen'
'''


import os
if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
if os.path.exists("dummy"):
  os.rmdir("dummy")


#pwd
cwd = os.getcwd()
print(cwd)
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

import os

files = [
    # full filenames
    "var/log/apache/errors.log",
    "home/kane/images/avatars/crusader.png",
    "home/jane/documents/diary.txt",
    "home/kane/images/selfie.jpg",
    "var/log/abc.txt",
    "home/kane/.vimrc",
    "home/kane/images/avatars/paladin.png",
]

# unfolding of plain filename list to file-tree
fs_tree = ({}, # dict of folders
           []) # list of files
for full_name in files:
    path, fn = os.path.split(full_name)
    reduce(
        # this fucction walks deep into path
        # and creates placeholders for subfolders
        lambda d, k: d[0].setdefault(k,         # walk deep
                                     ({}, [])), # or create subfolder storage
        path.split(os.path.sep),
        fs_tree
    )[1].append(fn)

print fs_tree
#({'home': (
#    {'jane': (
#        {'documents': (
#           {},
#           ['diary.txt']
#        )},
#        []
#    ),
#    'kane': (
#       {'images': (
#          {'avatars': (
#             {},
#             ['crusader.png',
#             'paladin.png']
#          )},
#          ['selfie.jpg']
#       )},
#       ['.vimrc']
#    )},
#    []
#  ),
#  'var': (
#     {'log': (
#         {'apache': (
#            {},
#            ['errors.log']
#         )},
#         ['abc.txt']
#     )},
#     [])
#},
#[])



#SQL
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(	
    	host='localhost', 
		database='world',
    	user='baliepages', 
    	password='baliepages', 
    	port=3306,
    	auth_plugin='mysql_native_password')

    if connection.is_connected():
       cursor = connection.cursor()
       cursor.execute('select database();')
       record = cursor.fetchone() #The fetchone() method will return the first row of the result
       print ('Your connected to - ', record)

       cursor.execute('SHOW TABLES')
       for x in cursor:
           print(x)

       '''
       sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
       val = [
       ('Peter', 'Lowstreet 4'),
       ('Amy', 'Apple st 652'),
       ('Hannah', 'Mountain 21'),
       ('Michael', 'Valley 345'),
       ('Sandy', 'Ocean blvd 2'),
       ('Betty', 'Green Grass 1'),
       ('Richard', 'Sky st 331'),
       ('Susan', 'One way 98'),
       ('Vicky', 'Yellow Garden 2'),
       ('Ben', 'Park Lane 38'),
       ('William', 'Central st 954'),
       ('Chuck', 'Main Road 989'),
       ('Viola', 'Sideway 1633')
       ]
       cursor.executemany(sql, val)'''

       sql = 'UPDATE customers SET address = %s WHERE address = %s'
       val = ('Valley 345', 'Canyon 123')
       cursor.execute(sql, val)
       connection.commit()
       print(cursor.rowcount, 'record inserted.')

       sql = 'SELECT * FROM customers WHERE address = %s'
       adr = ('Yellow Garden 2', )
       cursor.execute(sql, adr)
       result = cursor.fetchall()
       for x in result:
         print(x)

except Error as e :
    print ('Error while connecting to MySQL : ', e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('MySQL connection is closed')








#Null
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
v_nonNull = string1 or string2 or string3
print(v_nonNull)







#Tuples:
t1 = 12345, 54321, 'hello!'
t2 = t1, (1, 2, 3, 4, 5)
print(t1[0])
print (t2)

# Tuples are immutable
try:
	t1[0] = 1000 #TypeError: 'tuple' object does not support item assignment
except (TypeError, AttributeError) as e :
    print ('Defined Error', e)
except Error as e :
    print ('Undefined Error', e)
finally:
	print('Try catch finished')



#Collections
from collections import defaultdict
m = defaultdict()
m = defaultdict(list)
print(m)
m['roll_nbr'].append(1)
m['roll_nbr'].append(2)
m['name'] = ['Balie'] # If it were a simple Str instead of Array 'AttributeError: 'str' object has no attribute 'append' '
m['name'].append('Pages')
print(m)
print(dict(m))


#exercise
#'Get the character at position 1 of a string' 
a = 'Hello, World!'
print(a[1])
print(a[2:5])
print(a[2::2])





#json to python to json dict:
import json
'''
x = "{ 'name':'John', 'age':30, 'city':'New York'}" 
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
'''
x = '{ "name":"John", "age":30, "city":"New York"}' # some json
y = json.loads(x) # parse json object
print(y['age']) # the result is a Python dictionary
z = json.dumps(x) # convert back into json
print(z) # the result is a JSON string






#Regex
import re

#Check if the string starts with 'The' and ends with 'Spain':
str = 'James is 37, one two three, He lives in Spain.'
x = re.search('^James.*Spain.$', txt)

if (x):
  print('YES! We have a match!')
else:
  print('No match')


#Find all lower case characters alphabetically between 'a' and 'm':
x = re.findall('[a-m]', str)
print(x)
#Find all digit characters:
x = re.findall('\d', str)
print(x)
#Search for a sequence that starts with 'Sp', followed by two (any) characters, and an 'n':
x = re.findall('Sp..n', str)
print(x)
#Check if the string starts with 'hello':
x = re.findall('^James', str)
print(x)
#Check if the string ends with 'hain':
x = re.findall('Sain.$', str)
print(x)
#Check if the string contains 'th' followed by 1 or more 'e' characters:
x = re.findall('thre+', str)
print(x)
#Check if the string contains 'th' followed by exactly two 'e' characters:
x = re.findall('thre{2}', str)
print(x)
#Check if the string contains either 'India' or 'Spain':
x = re.findall('India|Spain', str)
print(x)
#Check if the string has any + characters:
x = re.findall('[,]', str)
print(x)
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall('[a-zA-Z]', str)
print(x)
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall('[0-5][0-9]', str)
print(x)
#Check if the string has any digits:
x = re.findall('[0-9]', str)
print(x)
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall('[0123]', str)
print(x)
#Check if the string has other characters than a, r, or n:
x = re.findall('[^arn]', str)
print(x)
#Check if the string has any characters between a and n:
x = re.findall('[a-n]', str)
print(x)
#Check if the string has any a, r, or n characters:
x = re.findall('[arn]', str)
print(x)
#First space position
x = re.search('\s', str)
print('The first white-space character is located in position:', x.start()) 
print(x)
#Split the string at every white-space character:
x = re.split('\s', str)
print(x)
#Split the string at the first white-space character:
x = re.split('\s', str, 2)
print(x)
#Replace all white-space characters with the digit '9':
x = re.sub('\s', '@', str)
print(x)
#Replace the first two occurrences of a white-space character with the digit 9:
x = re.sub('\s', '@', str, 2)
print(x)
#Search for an upper case 'S' character in the beginning of a word, and print its position:
x = re.search(r'\bS\w+', str)
print(x.span())



#Boolean
mylist = [True, False, True]
x = all(mylist) # The all() function returns True if all items in an iterable are true, otherwise it returns False.
y = any(mylist)


#Arithmetic
a = (1, 5, 3, 9)
x = max(a)
y = min(a)
z = sum(a)
p = pow(4, 3)
print(a, x, y, z, p)


#Code
# The compile() function returns the specified source as a code object, ready to be executed.
x = compile('print(55)\nprint(88)', 'test', 'exec') 
exec(x)

# The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
x = 'print(55)'
eval(x) 

# The exec() function executes the specified Python code.
x = 'name = "John"\nprint(name)'
exec(x) 

#The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression


#web
#requests
import requests
print("requests file:", requests.__file__)

#the required first parameter of the 'get' method is the 'url':
x = requests.get('http://webminnal.blogspot.com')
y = x.text
#print the response text (the content of the requested file):
#print(y)


#Enumerate
# The enumerate() function adds a counter as the key of the enumerate object.
x = ('apple', 'banana', 'cherry')
y = enumerate(x) 
print(list(y))

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)



#Clear
l_callLog.clear()
s_interests.clear()
d_skills.clear()
'''
t_family.clear()
AttributeError: 'tuple' object has no attribute 'clear'
'''


#Delete
del l_callLog
del s_interests
del d_skills
del t_family
del jude

