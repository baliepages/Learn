for line in open('foo'):
    print(line)
which is equivalent (but better) to:

f = open('foo', 'r')
for line in f.readlines():
   print(line)
f.close()


import time
time.sleep(5) # delays for 5 seconds


Parse String to Float or Int
>>> a = "545.2222"
>>> float(a)
545.22220000000004
>>> int(float(a))
545


Making a flat list out of list of lists in Python
[item for sublist in l for item in sublist]
flatten = lambda l: [item for sublist in l for item in sublist]


>>> import itertools
>>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
>>> merged = list(itertools.chain(*list2d))

>>> import itertools
>>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
>>> merged = list(itertools.chain.from_iterable(list2d))

>>> sum(l, [])
[1, 2, 3, 4, 5, 6, 7, 8, 9]



A = reduce(lambda x,y: x+y,l) #14.323 ms
B = sum(l, []) #13.437 ms
C = [item for sublist in l for item in sublist] #1.135 ms



Static class variables in Python
>>> class MyClass:
...     i = 3

>>> m = MyClass()
>>> m.i = 4
>>> MyClass.i, m.i
>>> (3, 4)



How do I read a file line-by-line into a list?
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


How to get the size of a list
>>> len([1,2,3])
3


How to clone or copy a list?
a_copy = a_list.copy()
new_list = old_list[:]
new_list = []; new_list.extend(old_list)
new_list = list(old_list)
[i for i in old_list]
for item in old_list: new_list.append(item)


METHOD                  TIME TAKEN
b = a[:]                6.468942025996512   #Python2 winner
b = a.copy()            6.986593422974693   #Python3 "slice equivalent"
b = []; b.extend(a)     7.309216841997113
b = a[0:len(a)]         10.916740721993847
*b, = a                 11.046738261007704
b = list(a)             11.761539687984623
b = [i for i in a]      24.66165203397395
b = copy.copy(a)        30.853400873980718
b = []
for item in a:
  b.append(item)        48.19176080400939
  
  
  
How do you split a list into evenly sized chunks?
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
		
import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))
[[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
 [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
 [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
 [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
 [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
 [70, 71, 72, 73, 74]]
 
 You can simply use list comprehension instead of write a function.
 [l[i:i + n] for i in range(0, len(l), n)]
 
 
 
How can I remove a newline in Python?
>>> 'test string\n'.rstrip()
'test string'
There is also the lstrip and strip methods.


Python join: why is it string.join(list) instead of list.join(string)?


This has always confused me. It seems like this would be nicer:
my_list = ["Hello", "world"]
print my_list.join("-")
# Produce: "Hello-world"

Than this:
my_list = ["Hello", "world"]
print "-".join(my_list)
# Produce: "Hello-world"



What does ** (double star) and * (star) do for parameters?
The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions 

In [1]: def foo(*args):
   ...:     for a in args:
   ...:         print a
   ...:         
   ...:         

In [2]: foo(1)
1


In [4]: foo(1,2,3)
1
2
3


The **kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary.

In [5]: def bar(**kwargs):
   ...:     for a in kwargs:
   ...:         print a, kwargs[a]
   ...:         
   ...:         

In [6]: bar(name='one', age=27)
age 27
name one


Both idioms can be mixed with normal arguments to allow a set of fixed and some variable arguments:

def foo(kind, *args, **kwargs):
   pass
Another usage of the *l idiom is to unpack argument lists when calling a function.

In [9]: def foo(bar, lee):
   ...:     print bar, lee
   ...:     
   ...:     

In [10]: l = [1,2]

In [11]: foo(*l)
1 2


first, *rest = [1,2,3,4]
first, *l, last = [1,2,3,4]


def foo(arg, kwarg=None, *args, kwarg2=None, **kwargs): 
    return arg, kwarg, args, kwarg2, kwargs
	
>>> foo(1,2,3,4,5,kwarg2='kwarg2', bar='bar', baz='baz')
(1, 2, (3, 4, 5), 'kwarg2', {'bar': 'bar', 'baz': 'baz'})

>>> foo(1,2,kwarg2='kwarg2', foo='foo', bar='bar')
(1, 2, 'kwarg2', {'foo': 'foo', 'bar': 'bar'})


Determine the type of an object?
type([]) #list
type({}) #dict
type('') #str
type(0) #int


How to convert string to lowercase in Python?
s = "Kilometer"
print(s.lower())



start = time.time()
...
...
delta_sec = int(time.time() - start_time)


Converting string into datetime
from datetime import datetime
datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')


Manually raising (throwing) an exception in Python
raise ValueError('A very specific bad thing happened')

try:
	raise ValueError('represents a hidden bug, do not catch this')
	raise Exception('This is the exception you expect to handle')
except Exception as error:
	print('caught this error: ' + repr(error))
	print(err.args)
	
	
	
How do I copy a file in python?
shutil has many methods you can use. One of which is:

from shutil import copyfile
copyfile(src, dst)


copy2(src,dst) is often more useful than copyfile(src,dst) because:

it allows dst to be a directory (instead of the complete target filename), in which case the basename of src is used for creating the new file;
it preserves the original modification and access info (mtime and atime) in the file metadata (however, this comes with a slight overhead).
Here is a short example:

import shutil
shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
	


	
Find current directory and file's directory
To get the full path to the directory a Python file is contained in, write this in that file:

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

To get the current working directory use

import os
cwd = os.getcwd()



Python string formatting: % vs. .format

#!/usr/bin/python
sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!" % {'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print a    # "i am a python string!"
print b    # "i am a python string!"
print c    # "with an arg!"
print d    # "with an arg!"

"hi there %s" % name
if name happens to be (1, 2, 3), it will throw a TypeError
you'd need to do
"hi there %s" % (name,)   # supply the single argument as a single-item tuple

.format doesn't have those issues. 










 











Add new keys to a dictionary?
>>> d = {'key':'value'}
>>> print d
{'key': 'value'}
>>> d['mynewkey'] = 'mynewvalue'
>>> print d
{'mynewkey': 'mynewvalue', 'key': 'value'}



How to get current time in Python
>>> from datetime import datetime
print(datetime.datetime.now().time())                         # 11:20:08.272239
>>> datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(datetime.datetime.now().time().strftime('%H:%M:%S.%f')) # 11:20:08.272239
>>> from time import gmtime, strftime
>>> strftime("%Y-%m-%d %H:%M:%S", gmtime())
'2009-01-05 22:14:39'
>>> str(datetime.now())
'2011-05-03 17:45:35.177000'


import datetime
date_time = datetime.datetime.now()

date = date_time.date()  # gives date
time = date_time.time()  # gives time

print date.year, date.month, date.day
print time.hour, time.minute, time.second, time.microsecond



Iterating over dictionaries using 'for' loops
d = {'x': 1, 'y': 2, 'z': 3} 
for key, value in d.items():





dict.get() has a default value of None, thereby avoiding KeyErrors:

In [1]: test = { 1 : 'a' }
In [2]: test[2]
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call last)
&lt;ipython console&gt; in <module>()
<type 'exceptions.KeyError'>: 2
In [3]: test.get( 2 )
In [4]: test.get( 1 )
Out[4]: 'a'
In [5]: test.get( 2 ) == None
Out[5]: True


Too lazy to initialize every field in a dictionary? 
from collections import defaultdict
d = defaultdict(list)
for stuff in lots_of_stuff:
     d[stuff.name].append(stuff)
	 

Dict Comprehensions
>>> {i: i**2 for i in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


	
Set Comprehensions
>>> {i**2 for i in range(5)}                                                       
set([0, 1, 4, 16, 9])


>>> l=[(1,2),(3,4)]
>>> [a+b for a,b in l ] 
[3,7]


mylist = ['foo', 'bar', 'some other value', 1,2,3,4]  
print(*mylist)


>>> from operator import add,mul
>>> reduce(add,[1,2,3,4])
10
>>> reduce(mul,[1,2,3,4])
24
>>> reduce(add,[[1,2,3,4],[1,2,3,4]])
[1, 2, 3, 4, 1, 2, 3, 4]



Simple built-in benchmarking tool
% python -m timeit 'r = range(0, 1000)' 'for i in r: pass'
10000 loops, best of 3: 48.4 usec per loop

% python -m timeit 'r = xrange(0, 1000)' 'for i in r: pass'
10000 loops, best of 3: 37.4 usec per loop



Manipulating Recursion Limit
sys.getrecursionlimit() & sys.setrecursionlimit()


join a list of strings together
''.join(list_of_strings)



map(), reduce(), and filter()

Even though Guido considered removing map, filter and reduce from Python 3, there was enough of a backlash that in the end only reduce was moved from built-ins to functools.reduce.


List filtering: list comprehension vs. lambda + filter

[i for i in list if i.attribute == value]

my_list = [x for x in my_list if x.attribute == value]
my_list = filter(lambda x: x.attribute == value, my_list)

Use a generator instead of a list comprehension:
def filterbyvalue(seq, value):
   for el in seq:
       if el.attribute==value: yield el

 
 
Understanding the map function
map creates a new list by applying a function to every element of the source.
map(function, iterable, ...) is basically equivalent to:
[f(x) for x in iterable]


Flatten a list
Goal: turn [[1, 2, 3], [4, 5], [6, 7, 8]] into [1, 2, 3, 4, 5, 6, 7, 8].
reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], [])

List of digits to a number
Goal: turn [1, 2, 3, 4, 5, 6, 7, 8] into 12345678.

Ugly, slow way:
int("".join(map(str, [1,2,3,4,5,6,7,8])))

Pretty reduce way:
reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7,8], 0)


LCM:
#!/usr/bin/env python
from fractions import gcd
from functools import reduce

def lcm(*args):
    return reduce(lambda a,b: a * b // gcd(a, b), args)
Example:

>>> lcm(100, 23, 98)
112700
>>> lcm(*range(1, 20))
232792560




Find the intersection of N given lists:

input_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
reduce(set.intersection, map(set, input_list))
returns : set([3, 4, 5])



Function composition: If you already have a list of functions that you'd like to apply in succession, such as:

color = lambda x: x.replace('brown', 'blue')
speed = lambda x: x.replace('quick', 'slow')
work = lambda x: x.replace('lazy', 'industrious')
fs = [str.lower, color, speed, work, str.title]
Then you can apply them all consecutively with:

>>> call = lambda s, func: func(s)
>>> s = "The Quick Brown Fox Jumps Over the Lazy Dog"
>>> reduce(call, fs, s)
'The Slow Blue Fox Jumps Over The Industrious Dog'


build a list of files to process:
files = []
files.extend(reduce(lambda x, y: x + y, map(glob.glob, args)))

Equivalent to:
files = []
for f in args:
    files.extend(glob.glob(f))

get the list with the maximum nth element
reduce(lambda x,y: x if x[2] > y[2] else y,[[1,2,3,4],[5,2,5,7],[1,6,0,2]])
would return [5, 2, 5, 7] as it is the list with max 3rd element 

Operators can be called as functions:
from operator import add
print reduce(add, [1,2,3,4,5,6])


find the MIN/MAX values in each month across the different years
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

print reduce(lambda x, y: x & y, stat_list)     # MIN
print reduce(lambda x, y: x | y, stat_list)     # MAX


Union or Intersection of sets:
>>> reduce(operator.or_, ({1}, {1, 2}, {1, 3}))  # union
{1, 2, 3}
>>> reduce(operator.and_, ({1}, {1, 2}, {1, 3}))  # intersection
{1}



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




Cartesian product with a list comprehension
[(a, b) for a in iterable_a for b in iterable_b]

that's basically equivalent to:

result = []
for a in iterable_a:
    for b in iterable_b:
        result.append((a, b))



		
 
 
>>> len(set([1,2,1,1,2,3,4]))
4

>>> set([1,2,3,4]).issubset([0,1,2,3,4,5])
True



import math
if not n >= 0:
	raise ValueError("n must be >= 0")
if math.floor(n) != n:
	raise ValueError("n must be exact integer")
if n+1 == n:  # catch a value like 1e300
	raise OverflowError("n too large")
	
	
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'

from collections import defaultdict
>>> m = defaultdict(list)
>>> m["foo"].append(1)
>>> m["foo"].append(2)
>>> dict(m)
{'foo': [1, 2]}

Iterables

>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3

>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4



Tuples and Sequences

>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


SETs:

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in either a or b
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}



Set comprehension:
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}



>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False



The dict() constructor builds dictionaries directly from sequences of key-value pairs:


>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:


>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:


>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}




Looping Techniques

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.


>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.


>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
To loop over two or more sequences at the same time, the entries can be paired with the zip() function.


>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.


>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.


>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.


>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]


Comparing Sequences and Other Types

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)















List - a mutable type
String - an immutable type

#pass  by value vs pass by reference

def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four') # modified in place
    print('changed to', the_list)

outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)



before, outer_list = ['one', 'two', 'three']
got ['one', 'two', 'three']
changed to ['one', 'two', 'three', 'four']
after, outer_list = ['one', 'two', 'three', 'four']




def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie'] #assignment does not override original value
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)


before, outer_list = ['we', 'like', 'proper', 'English']
got ['we', 'like', 'proper', 'English']
set to ['and', 'we', 'can', 'not', 'lie']
after, outer_list = ['we', 'like', 'proper', 'English']



#Python's slice notation

 -5  -4  -3  -2  -1   #index from rear
  0   1   2   3   4   #index from front
+---+---+---+---+---+
| a | b | c | d | e |
+---+---+---+---+---+
    1   2   3   4   #slicing from front
   -4  -3  -2  -1   #slicing from rear


a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items


# mostly used variations
s[start:end]
s[start:]
s[:end]

# step related variations
s[:end:step]
s[start::step]
s[::step]

# make a copy
s[:]

alpha = ['a', 'b', 'c', 'd', 'e', 'f']
alpha[0] #a
alpha[0] = 'A'
alpha #['A', 'b', 'c', 'd', 'e', 'f']
alpha[0:2] = ['Z', 'B']
alpha #['Z', 'B', 'c', 'd', 'e', 'f']
alpha[2:2] = ['x', 'xx']
alpha #['Z', 'B', 'x', 'xx', 'c', 'd', 'e', 'f']

Slicing With Step:
alpha = ['a', 'b', 'c', 'd', 'e', 'f']
alpha[1:5:2] #['b', 'd']
alpha[-1:-5:-2] #['f', 'd']


  +---+---+---+---+---+---+---+---+---+
  | C | O | M | P | U | T | E | R | S |
  +---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   
 -9  -8  -7  -6  -5  -4  -3  -2  -1 

COMPUTERS[ 4 : 7 ]     =  UTE
COMPUTERS[ 2 : 5 : 2 ] =  MU
COMPUTERS[-5 : 1 :-1 ] =  UPM
COMPUTERS[ 4 ]         =  U
COMPUTERS[-4 :-6 :-1 ] =  TU
COMPUTERS[ 2 :-3 : 1 ] =  MPUT
COMPUTERS[ 2 :-3 :-1 ] =  
COMPUTERS[   :   :-1 ] =  SRETUPMOC #reverse
COMPUTERS[-5 :   ]     =  UTERS
COMPUTERS[-5 : 0 :-1 ] =  UPMO
COMPUTERS[-5 :   :-1 ] =  UPMOC
COMPUTERS[-1 : 1 :-2 ] =  SEUM


# create our array for demonstration
In [1]: s = [i for i in range(10)]

In [2]: s
Out[2]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [3]: s[2:]   # from index 2 to last index
Out[3]: [2, 3, 4, 5, 6, 7, 8, 9]

In [4]: s[:8]   # from index 0 up to index 8
Out[4]: [0, 1, 2, 3, 4, 5, 6, 7]

In [5]: s[4:7]  # from index 4(included) up to index 7(excluded)
Out[5]: [4, 5, 6]

In [6]: s[:-2]  # up to second last index(negative index)
Out[6]: [0, 1, 2, 3, 4, 5, 6, 7]

In [7]: s[-2:]  # from second last index(negative index)
Out[7]: [8, 9]

In [8]: s[::-1] # from last to first in reverse order(negative step)
Out[8]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

In [9]: s[::-2] # all odd numbers in reversed order
Out[9]: [9, 7, 5, 3, 1]

In [11]: s[-2::-2] # all even numbers in reversed order
Out[11]: [8, 6, 4, 2, 0]

In [12]: s[3:15]   # end is out of range, python will set it to len(s)
Out[12]: [3, 4, 5, 6, 7, 8, 9]

In [14]: s[5:1]    # start > end, return empty list
Out[14]: []

In [15]: s[11]     # access index 11(greater than len(s)) will raise IndexError
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-15-79ffc22473a3> in <module>()
----> 1 s[11]

IndexError: list index out of range



_str__ and __repr__ in Python

__repr__ goal is to be unambiguous
__str__ goal is to be readable
Container’s __str__ uses contained objects’ __repr__


>>> import datetime
>>> today = datetime.datetime.now()
>>> str(today)
'2012-03-14 09:21:58.130922'
>>> repr(today)
'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'




Understanding Python super() with __init__() methods 
What does 'super' do in Python?

       +-----+
       |  T  |
       |a = 0|
       +-----+
     /         \
    /           \
+-------+    +-------+
|   A   |    |   B   |
|       |    | a = 2 |
+-------+    +-------+
    \           /
     \         /
       +-----+
       |  C  |
       +-----+
          :
          :    instantiation
          c
>>> class T(object):
...     a = 0
>>> class A(T):
...     pass
>>> class B(T):
...     a = 2
>>> class C(A,B):
...     pass
>>> c = C()

What is the superclass of C? There are two direct superclasses (i.e. bases) of C: A and B. A comes before B, so one would naturally think that the superclass of C is A. However, A inherits its attribute a from T with value a=0: if super(C,c) was returning the superclass of C, then super(C,c).a would return 0. This is NOT what happens. Instead, super(C,c).a walks trought the method resolution order of the class of c (i.e. C) and retrieves the attribute from the first class above C which defines it. In this example the MRO of C is [C, A, B, T, object], so B is the first class above C which defines a and super(C,c).a correctly returns the value 2, not 0:

>>> super(C,c).a
2
You may call A the superclass of C, but this is not a useful concept since the methods are resolved by looking at the classes in the MRO of C, and not by looking at the classes in the MRO of A (which in this case is [A,T, object] and does not contain B). The whole MRO is needed, not just the first superclass.

So, using the word superclass in the standard docs is misleading and should be avoided altogether.


class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()
		#Python 3.0: super().__init__() instead of super(ChildB, self).__init__()



Finding the index of an item given a list containing it in Python
>>> ["foo", "bar", "baz"].index("bar")
1


Check if a given key already exists in a dictionary
d = dict()

for i in xrange(100):
    key = i % 10
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


d = {'a': 1, 'b': 2}
'a' in d # <== evaluates to True
'c' in d # <== evaluates to False



Catch multiple exceptions in one line (except block)

try:
    # do something that may fail
except IdontLikeYourPasswordException:
    # put on makeup or smile
except PasswordTooSmallException:
    # stand on a ladder

An except clause may name multiple exceptions as a parenthesized tuple, for example

try:
    mainstuff()
except (KeyboardInterrupt, EOFError) as err: 
    print(err)
    print(err.args)
    quit(0)
	
	
Chaining comparison operators:
>>> x = 5
>>> 1 < x < 10
True
>>> 10 < x < 20 
False
>>> x < 10 < x*10 < 100
True
>>> 10 > x <= 9
True
>>> 5 == x > 4
True


	
Get the python regex parse tree to debug your regex.

>>> re.compile("""
 ^              # start of a line
 \[font         # the font tag
 (?:=(?P<size>  # optional [font=+size]
 [-+][0-9]{1,2} # size specification
 ))?
 \]             # end of tag
 (.*?)          # text between the tags
 \[/font\]      # end of the tag
 """, re.DEBUG|re.VERBOSE|re.DOTALL)
	
Enumerate
>>> a = ['a', 'b', 'c', 'd', 'e']
>>> for index, item in enumerate(a): print index, item

0 a
1 b
2 c
3 d
4 e



Creating generators objects

The advantage of this is that you don't need intermediate storage, which you would need if you did
x = [(a,b) for a in range(0,2) for b in range(4,6)]

>>> n = ((a,b) for a in range(0,2) for b in range(4,6))
>>> for i in n:
...   print i 

(0, 4)
(0, 5)
(1, 4)
(1, 5)


	
iter() can take a callable argument
The iter(callable, until_value) function repeatedly calls callable and yields its result until until_value is returned.

for c in iter(lambda: f.read(1),'\n'):


Be careful with mutable default arguments

>>> def foo(x=[]):
...     x.append(1)
...     print x
... 
>>> foo()
[1]
>>> foo()
[1, 1]
>>> foo()
[1, 1, 1]
Instead, you should use a sentinel value denoting "not given" and replace with the mutable you'd like as default:

>>> def foo(x=None):
...     if x is None:
...         x = []
...     x.append(1)
...     print x
>>> foo()
[1]
>>> foo()
[1]





Decorators
Decorators allow to wrap a function or method in another function that can add functionality, modify arguments or results, etc. You write decorators one line above the function definition, beginning with an "at" sign (@).

Example shows a print_args decorator that prints the decorated function's arguments before calling it:

>>> def print_args(function):
>>>     def wrapper(*args, **kwargs):
>>>         print 'Arguments:', args, kwargs
>>>         return function(*args, **kwargs)
>>>     return wrapper

>>> @print_args
>>> def write(text):
>>>     print text

>>> write('foo')
Arguments: ('foo',) {}
foo





	
In-place value swapping

>>> a = 10
>>> b = 5
>>> a, b
(10, 5)

>>> a, b = b, a
>>> a, b
(5, 10)




Using Lists as Stacks
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]



Using Lists as Queues
It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:


>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])



List Comprehensions:

>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(10)]



>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


Transpose a Matrix

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:


>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
del can also be used to delete entire variables:


>>> del a


Readable regular expressions

In Python you can split a regular expression over multiple lines, name your matches and insert comments.

>>> pattern = """
... ^                   # beginning of string
... M{0,4}              # thousands - 0 to 4 M's
... (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
...                     #            or 500-800 (D, followed by 0 to 3 C's)
... (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
...                     #        or 50-80 (L, followed by 0 to 3 X's)
... (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
...                     #        or 5-8 (V, followed by 0 to 3 I's)
... $                   # end of string
... """
>>> re.search(pattern, 'M', re.VERBOSE)


pat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)
This is far more readable than:

pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")


>>> pattern = (
...     "^"                 # beginning of string
...     "M{0,4}"            # thousands - 0 to 4 M's
...     "(CM|CD|D?C{0,3})"  # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
...                         #            or 500-800 (D, followed by 0 to 3 C's)
...     "(XC|XL|L?X{0,3})"  # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
...                         #        or 50-80 (L, followed by 0 to 3 X's)
...     "(IX|IV|V?I{0,3})"  # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
...                         #        or 5-8 (V, followed by 0 to 3 I's)
...     "$"                 # end of string
... )
>>> print pattern
"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"


Function argument unpacking
You can unpack a list or a dictionary as function arguments using * and **.

def draw_point(x, y):
    # do some magic

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)



Built-in base64, zlib, and rot13 codecs
>>> s = 'a' * 100
>>> s.encode('zlib')
'x\x9cKL\xa4=\x00\x00zG%\xe5'
Similarly you can encode and decode base64:

>>> 'Hello world'.encode('base64')
'SGVsbG8gd29ybGQ=\n'
>>> 'SGVsbG8gd29ybGQ=\n'.decode('base64')
'Hello world'
And, of course, you can rot13:

>>> 'Secret message'.encode('rot13')
'Frperg zrffntr'




Creating new types in a fully dynamic manner
>>> NewType = type("NewType", (object,), {"x": "hello"})
>>> n = NewType()
>>> n.x
"hello"
which is exactly the same as

>>> class NewType(object):
>>>     x = "hello"
>>> n = NewType()
>>> n.x
"hello"



Context managers and the "with" Statement

from __future__ import with_statement

with open('foo.txt', 'w') as f:
    f.write('hello!')
	

Dictionaries have a get() method
sum[value] = sum.get(value, 0) + 1




Conditional Assignment
x = 3 if (y == 1) else 2
x = 3 if (y == 1) else 2 if (y == -1) else 1

(func1 if y == 1 else func2)(arg1, arg2) 
Here func1 will be called if y is 1 and func2, otherwise. In both cases the corresponding function will be called with arguments arg1 and arg2.

Analogously, the following is also valid:
x = (class1 if y == 1 else class2)(arg1, arg2)
where class1 and class2 are two classes.





	
Named formatting

>>> print "The %(foo)s is %(bar)i." % {'foo': 'answer', 'bar':42}
The answer is 42.

>>> foo, bar = 'question', 123

>>> print "The %(foo)s is %(bar)i." % locals()
The question is 123.


New Style Formatting

>>> print("The {foo} is {bar}".format(foo='answer', bar=42))




Exception else clause:
try:
  put_4000000000_volts_through_it(parrot)
except Voom:
  print "'E's pining!"
else:
  print "This parrot is no more!"
finally:
  end_sketch()
  
  
  
Re-raising exceptions:

# Python 3 syntax
try:
    some_operation()
except SomeError as e:
    if is_fatal(e):
        raise
    handle_nonfatal(e)
	
	
	
	
Nested list comprehensions and generator expressions:

[(i,j) for i in range(3) for j in range(i) ]    
((i,j) for i in range(4) for j in range(i) )




Operator overloading for the set builtin:

>>> a = set([1,2,3,4])
>>> b = set([3,4,5,6])
>>> a | b # Union
{1, 2, 3, 4, 5, 6}
>>> a & b # Intersection
{3, 4}
>>> a < b # Subset
False
>>> a - b # Difference
{1, 2}
>>> a ^ b # Symmetric Difference
{1, 2, 5, 6}






Negative round

The round() function rounds a float number to given precision in decimal digits, but precision can be negative:

>>> str(round(1234.5678, -2))
'1200.0'
>>> str(round(1234.5678, 2))
'1234.57'




	
tuple unpacking in python 3
in python 3, you can use a syntax identical to optional arguments in function definition for tuple unpacking:

>>> first,second,*rest = (1,2,3,4,5,6,7,8)
>>> first
1
>>> second
2
>>> rest
[3, 4, 5, 6, 7, 8]
but a feature less known and more powerful allows you to have an unknown number of elements in the middle of the list:

>>> first,*rest,last = (1,2,3,4,5,6,7,8)
>>> first
1
>>> rest
[2, 3, 4, 5, 6, 7]
>>> last
8







Multi line strings

sql = "select * from some_table \
where id > 10"

sql = """select * from some_table 
where id > 10"""

sql = ("select * from some_table " # <-- no comma, whitespace at end
           "where id > 10 "
           "order by name") 
		   
		   

>>> import webbrowser
>>> webbrowser.open_new_tab('http://www.stackoverflow.com')



	
pow() can also calculate (x ** y) % z efficiently.
>>> x, y, z = 1234567890, 2345678901, 17
>>> pow(x, y, z)            # almost instantaneous
6
In comparison, (x ** y) % z didn't given a result in one minute on my machine for the same values.




You can easily transpose an array with zip.

a = [(1,2), (3,4), (5,6)]
zip(*a)
# [(1, 3, 5), (2, 4, 6)]





	
enumerate with different starting index
>>> l = ["spam", "ham", "eggs"]
>>> list(enumerate(l))
>>> [(0, "spam"), (1, "ham"), (2, "eggs")]
>>> list(enumerate(l, 1))
>>> [(1, "spam"), (2, "ham"), (3, "eggs")]




GOTO:
from goto import goto, label
for i in range(1, 10):
    for j in range(1, 20):
        for k in range(1, 30):
            print i, j, k
            if k == 3:
                goto .end # breaking out from a deeply nested loop
label .end
print "Finished"




Sequence multiplication and reflected operands

>>> 'xyz' * 3
'xyzxyzxyz'

>>> [1, 2] * 3
[1, 2, 1, 2, 1, 2]

>>> (1, 2) * 3
(1, 2, 1, 2, 1, 2)




Interleaving if and for in list comprehensions
>>> [(x, y) for x in range(4) if x % 2 == 1 for y in range(4)]
[(1, 0), (1, 1), (1, 2), (1, 3), (3, 0), (3, 1), (3, 2), (3, 3)]




Sort Tuples:
a = [(2, "b"), (1, "a"), (2, "a"), (3, "c")]
print sorted(a)
#[(1, 'a'), (2, 'a'), (2, 'b'), (3, 'c')]






if x=y:
	print('x=y')
elif x=z:
	print('x=z')
else:
	print('x!=y and x!=z')	
	
#ternary conditional operator:
'x=y' if x=y else 'x!=y'


>>>', '.join(['a', 'b', 'c'])
'a, b, c'


Iterables
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)

#Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly.

Generators
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)


#yield is a keyword that is used like return, except the function will return a generator. 
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i

mygenerator = createGenerator()
>>> for i in mygenerator:
...     print(i)

>>> a = [1, 2]
>>> b = [3, 4]
>>> a.extend(b)
>>> print(a)
[1, 2, 3, 4]



>>> class Bank(): # let's create a bank, building ATMs
...    crisis = False
...    def create_atm(self):
...        while not self.crisis:
...            yield "$100"


>>> hsbc = Bank() # when everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']

>>> hsbc.crisis = True # crisis is coming, no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # build a new one to get back in business
>>> for cash in brand_new_atm:
...    print cash



#The itertools module contains special functions to manipulate iterables.

import itertools

>>> horses = [1, 2, 3, 4]
>>> races = itertools.permutations(horses)
>>> print(races)
>>> print(list(itertools.permutations(horses)))


>>> from itertools import *
>>> l = [[1, 2], [3, 4]]
>>> list(chain(*l))
[1, 2, 3, 4]



#How do I check whether a file exists using Python?
import os.path
os.path.isfile(fname) 

#Unlike isfile(), exists() will return True for directories.	
>>> print os.path.isfile("/etc/password.txt")
True
>>> print os.path.isfile("/etc")
False
>>> print os.path.exists("/etc/password.txt")
True
>>> print os.path.exists("/etc")
True


from pathlib import Path
my_file = Path("/path/to/file")
if my_file.is_file():
    # file exists
	 f = open(filepath)
	 f = open(filepath, 'r')
	 f = open(filepath, 'w')
	 f = open(filepath, 'wx')  # python 3, x opens for exclusive creation, failing if the file already exists
	 f.read()
else:
    # file doesn't exist


from contextlib import suppress
	with suppress(OSError), open(path) as f:
    f.read()

	
import pathlib
p = pathlib.Path('path/to/file')
if p.is_file():  # or p.is_dir() to see if it is a directory
    # do stuff
try:
    with p.open() as f:
        # do awesome stuff
except OSError:
    print('Well darn.')


	
try:
    # http://effbot.org/zone/python-with-statement.htm
    # with is more safe to open file
    with open('whatever.txt') as fh: 
        # do something with fh
		return fh.read()
except IOError as e:
    print("({})".format(e)) #output would be ([Errno 2] No such file or directory: 'whatever.txt')

	
	
#What does if __name__ == “__main__”: do?

If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.

# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
	
	
python one.py

top-level in one.py
one.py is being run directly

python two.py

top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly


# a.py
import b


# b.py
print "Hello World from %s!" % __name__

if __name__ == '__main__':
    print "Hello World again from %s!" % __name__
	
	
	# b.py
print "Hello World from %s!" % __name__

if __name__ == '__main__':
    print "Hello World again from %s!" % __name__


$ python a.py
Hello World from b!

$ python b.py
Hello World from __main__!
Hello World again from __main__!


#Calling an external command in Python

The advantage of subprocess vs system is that it is more flexible (you can get the stdout, stderr, the "real" status code, better error handling, etc...).

print subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()

from subprocess import call
call(["ls", "-l"])

from subprocess import Popen, PIPE
cmd = "ls -l ~/"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print "Return code: ", p.returncode
print out.rstrip(), err.rstrip()

import subprocess
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()


import subprocess
import sys
# some code here
pid = subprocess.Popen([sys.executable, "longtask.py"]) # call subprocess
# some more code here




#How to merge two Python dictionaries in a single expression?
>>> x = {'a':1, 'b': 2}
>>> y = {'b':10, 'c': 11}
>>> z = x.update(y)

>>> print(z)
None
>>> x
{'a': 1, 'b': 10, 'c': 11}

Say you have two dicts and you want to merge them into a new dict without altering the original dicts. The desired result is to get a new dictionary (z) with the values merged, and the second dicts values overwriting those from the first.

z = {**x, **y}



def merge_two_dicts(x, y):
    #Given two dicts, merge them into a new dict as a shallow copy.
    z = x.copy()
    z.update(y)
    return z
	
z = merge_two_dicts(x, y)



def merge_dicts(*dict_args):
    #Given any number of dicts, shallow copy and merge into a new dict, precedence goes to key value pairs in latter dicts.
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
	
z = merge_dicts(a, b, c, d, e, f, g) 


z = dict(x.items() + y.items())
TypeError: unsupported operand type(s) for +: 'dict_items' and 'dict_items'

You would have to explicitly create them as lists, e.g. z = dict(list(x.items()) + list(y.items())). This is a waste of resources and computation power.


This example demonstrates what happens when values are unhashable:
>>> x = {'a': []}
>>> y = {'b': []}
>>> dict(x.items() | y.items())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'


Heres an example where y should have precedence, but instead the value from x is retained due to the arbitrary order of sets:
>>> x = {'a': 2}
>>> y = {'a': 1}
>>> dict(x.items() | y.items())
{'a': 2}


You can also chain the dicts manually inside a dict comprehension:
{k: v for d in dicts for k, v in d.items()} # iteritems in Python 2.7


itertools.chain will chain the iterators over the key-value pairs in the correct order:

import itertools
z = dict(itertools.chain(x.iteritems(), y.iteritems()))


Performance:
{**x, **y} 0.4094954460160807
merge_two_dicts(x, y) 0.7881555100320838
{k: v for d in (x, y) for k, v in d.items()} 1.4525277839857154
dict(itertools.chain(x.items(), y.items())) 2.3143140770262107
dict((k, v) for d in (x, y) for k, v in d.items()) 3.2069112799945287



>>> from collections import ChainMap
>>> x = {'a':1, 'b': 2}
>>> y = {'b':10, 'c': 11}
>>> z = ChainMap({}, y, x)
>>> for k, v in z.items():
        print(k, '-->', v)

a --> 1
b --> 10
c --> 11



Recursively/deep update a dict:

pluto_original = {
    'name': 'Pluto',
    'details': {
        'tail': True,
        'color': 'orange'
    }
}

pluto_update = {
    'name': 'Pluutoo',
    'details': {
        'color': 'blue'
    }
}


def deepupdate(original, update):
    """
    Recursively update a dict.
    Subdict's won't be overwritten but also updated.
    """
    for key, value in original.iteritems(): 
        if key not in update:
            update[key] = value
        elif isinstance(value, dict):
            deepupdate(value, update[key]) 
    return update
	
	
print deepupdate(pluto_original, pluto_update)


{
    'name': 'Pluutoo',
    'details': {
        'color': 'blue',
        'tail': True
    }
}

#reading dict
>>> d = {"third": 3, "first": 1, "fourth": 4, "second": 2}

>>> for k, v in d.items():
...     print "%s: %s" % (k, v)
...
second: 2
fourth: 4
third: 3
first: 1
	
	
#Sort a Python dictionary by value
It is not possible to sort a dict, only to get a representation of a dict that is sorted. Dicts are inherently orderless, but other types, such as lists and tuples, are not. So you need a sorted representation, which will be a list—probably a list of tuples.

for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
	
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

sorted_x.reverse() will give you a descending ordering

sorted_x will be a list of tuples sorted by the second element in each tuple.


And for those wishing to sort on keys instead of values:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

As of Python 3.6 the builtin dict will be ordered

k_seq = ('foo', 'bar', 'baz')
v_seq = (0, 1, 42)
ordered_map = dict(zip(k_seq, v_seq))

for k, v in ordered_map.items():
    print(k, v)
	
	
origin_list = [
    {"name": "foo", "rank": 0, "rofl": 20000},
    {"name": "Silly", "rank": 15, "rofl": 1000},
    {"name": "Baa", "rank": 300, "rofl": 20},
    {"name": "Zoo", "rank": 10, "rofl": 200},
    {"name": "Penguin", "rank": -1, "rofl": 10000}
]

for foo in sorted(origin_list, key=operator.itemgetter("rank")):
    print foo
	
{'name': 'Penguin', 'rank': -1, 'rofl': 10000}
{'name': 'foo', 'rank': 0, 'rofl': 20000}
{'name': 'Zoo', 'rank': 10, 'rofl': 200}
{'name': 'Silly', 'rank': 15, 'rofl': 1000}
{'name': 'Baa', 'rank': 300, 'rofl': 20}


Decorator basics:
def getTalk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes") :
        return word.lower()+"...";

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout  
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()      

# You can see that "talk" is here a function object:
print(talk)
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
#outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk("whisper")())
#outputs : yes...

How to make a chain of function decorators?

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello() ## returns "<b><i>hello world</i></b>"




How to check if a directory exists and create it if necessary?

if not os.path.exists(directory):
    os.makedirs(directory)
	
	
try:
	os.makedirs(path)
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise
			
try:
    os.makedirs(dirname)
except OSError:
    if os.path.exists(dirname):
        # We are nearly safe
        pass
    else:
        # There was an error on creation, so make sure we know about it
        raise
			
import errno
try:
    with open(filepath) as my_file:
        do_stuff(my_file)
except IOError as error:
    if error.errno == errno.ENOENT:
        print 'ignoring error because directory or file is not there'
    else:
        raise
		
		
#Best way to check if a list is empty
Using the implicit booleanness of the empty list a is quite pythonic.

if not a:
  print("List is empty")

Explicit:
if len(li) == 0:
    print('the list is empty')

	
comparing it to an anonymous empty list:
if a == []:
    print("a is empty")
	
try:
    next(iter(a))
    # list has elements
except StopIteration:
    print("Error: a is empty")
	
	

#Global Variables

# sample.py
myGlobal = 5

def func1():
    myGlobal = 42

def func2():
    print myGlobal

func1()
func2()

Prints 5.


def func1():
    global myGlobal
    myGlobal = 42
	
Prints 42




globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

print_globvar() 
set_globvar_to_one()
print_globvar()       # Prints 1



With parallel execution, global variables can cause unexpected results if you dont understand what is happening. Here is an example of using a global variable within multiprocessing. We can clearly see that each process works with its own copy of the variable:

import multiprocessing
import os
import random
import sys
import time

def worker(new_value):
    old_value = get_value()
    set_value(random.randint(1, 99))
    print('pid=[{pid}] '
          'old_value=[{old_value:2}] '
          'new_value=[{new_value:2}] '
          'get_value=[{get_value:2}]'.format(
          pid=str(os.getpid()),
          old_value=old_value,
          new_value=new_value,
          get_value=get_value()))

def get_value():
    global global_variable
    return global_variable

def set_value(new_value):
    global global_variable
    global_variable = new_value

global_variable = -1

print('before set_value(), get_value() = [%s]' % get_value())
set_value(new_value=-2)
print('after  set_value(), get_value() = [%s]' % get_value())

processPool = multiprocessing.Pool(processes=5)
processPool.map(func=worker, iterable=range(10))


before set_value(), get_value() = [-1]
after  set_value(), get_value() = [-2]
pid=[53970] old_value=[-2] new_value=[ 0] get_value=[23]
pid=[53971] old_value=[-2] new_value=[ 1] get_value=[42]
pid=[53970] old_value=[23] new_value=[ 4] get_value=[50]
pid=[53970] old_value=[50] new_value=[ 6] get_value=[14]
pid=[53971] old_value=[42] new_value=[ 5] get_value=[31]
pid=[53972] old_value=[-2] new_value=[ 2] get_value=[44]
pid=[53973] old_value=[-2] new_value=[ 3] get_value=[94]
pid=[53970] old_value=[14] new_value=[ 7] get_value=[21]
pid=[53971] old_value=[31] new_value=[ 8] get_value=[34]
pid=[53972] old_value=[44] new_value=[ 9] get_value=[59]


#Append Vs Extend
x = [1, 2, 3]
x.append([4, 5])
result: [1, 2, 3, [4, 5]]

x = [1, 2, 3]
x.extend([4, 5]) # Extends list by appending elements from the iterable
result: [1, 2, 3, 4, 5]

x.extend('hey')
result: [1, 2, 3, 4, 5, 'h', 'e', 'y']



# @staticmethod Vs @classmethod

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()

The object instance, a, is implicitly passed as the first argument.
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)


With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.

a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)

if you define something to be a classmethod, it is probably because you intend to call it from the class rather than from a class instance.

A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)



With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as thefirst argument. They behave like plain functions except that you can call them from an instance or the class:

a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)




#How to list all files of a directory?
os.listdir() will get you everything that is in a directory - files and directories.
If you want just files, you could either filter this down using os.path:


from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


I prefer using the glob module, as it does pattern matching and expansion.
import glob
print glob.glob("/home/adam/*.txt")



A one-line solution to get only list of files (no subdirectories):
filenames = next(os.walk(path))[2]

or absolute pathnames:
paths = [os.path.join(path,fn) for fn in next(os.walk(path))[2]]



file_paths = []  # List which will store all of the full filepaths.

# Walk the tree.
for root, directories, files in os.walk(directory):
	for filename in files:
		# Join the two strings in order to form the full filepath.
		filepath = os.path.join(root, filename)
		file_paths.append(filepath)  # Add it to the list.
		

Python 3.4
>>> import pathlib
>>> [p for p in pathlib.Path('.').iterdir() if p.is_file()]

Python 3.5
>>> import os
>>> [entry for entry in os.scandir('.') if entry.is_file()]




Does Python have a string contains substring method?

if "blah" not in somestring: 
    continue
	
s = "This be a string"
if s.find("is") == -1: #index, find, in
    print "Not found"
else:
    print "Found"
	

# print all files with dot in home directory
import commands
(st, output) = commands.getstatusoutput('ls -a ~')
print [f for f in output.split('\n') if '.' in f ]


Accessing the index in Python 'for' loops

ints = [8, 23, 45, 12, 78]
for idx, val in enumerate(ints):
    print(idx, val)
	
	
Its pretty simple to start it from 1 other than 0:

for index in enumerate(iterable, start=1):
   print index


for i in range(len(ints)):
   print i, ints[i]
   
   


functions are first class objects is simply great. You can pass them around like any other variable.

>>> def jim(phrase):
...   return 'Jim says, "%s".' % phrase
>>> def say_something(person, phrase):
...   print person(phrase)

>>> say_something(jim, 'hey guys')
'Jim says, "hey guys".'




>>> names = ['Bob', 'Marie', 'Alice']
>>> ages = [23, 27, 36]
>>> dict(zip(names, ages))
{'Alice': 36, 'Bob': 23, 'Marie': 27}

unzip is not needed.
>>> t1 = (0,1,2,3)
>>> t2 = (7,6,5,4)
>>> [t1,t2] == zip(*zip(t1,t2))
True


	
Flattening a list with sum().
>>> l = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
>>> sum(l, [])
[1, 2, 3, 4, 5, 6, 7, 8, 9]


	
"Unpacking" to function parameters
def foo(a, b, c):
        print a, b, c

bar = (3, 14, 15)
foo(*bar)

When executed prints:
3 14 15


for i in reversed([1, 2, 3]):
    print(i)
	
	
	
  
  
  
  










	
	
	