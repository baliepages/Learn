>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb

Function: Fibbonacci Series:

>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

Default Argument Values
function_1(1000)                                          # 1 positional argument
function_1(voltage=1000)                                  # 1 keyword argument
function_1(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
function_1(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
function_1('a million', 'bereft of life', 'jump')         # 3 positional arguments
function_1('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword



def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
and of course it would print:

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch



Arbitrary Argument Lists
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'




Unpacking Argument Lists
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]



>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !




Lambda Expressions
Small anonymous functions can be created with the lambda keyword. 
This function returns the sum of its two arguments: lambda a, b: a+b. 

This example uses a lambda expression to return a function
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43


This example pass a small function as an argument:
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]



Function annotations are completely optional metadata information about the types used by user-defined functions:
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'



>>> f = open('workfile', 'w')
>>> f.read()
'This is the entire file.\n'


>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'


>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file


f.write(string) writes the contents of string to the file, returning the number of characters written.
>>> f.write('This is a test\n')
15


>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18


>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: I/O operation on closed file



>>> with open('workfile', 'r') as f:
...     read_data = f.read()
>>> f.closed
True



import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
	
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly



try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


Predefined Clean-up Actions

for line in open("myfile.txt"):
    print(line, end="")
The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing. 


The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly. After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

		
		
		
Iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
	
	
	
Generator Expressions:
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word  for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']	
	
	
	
	
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python35'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0


>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'


>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']


running python demo.py one two three at the command line:

>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
	

	
	
String Pattern Matching
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'



>>> 'tea for too'.replace('too', 'two')
'tea for two'



>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4




>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095




Internet Access
from urllib.request import urlopen
>>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
...     for line in response:
...         line = line.decode('utf-8')  # Decoding the binary data to text.
...         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...             print(line)



from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
     for line in response:
         line = line.decode('utf-8')  # Decoding the binary data to text.
         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
             print(line)








How do you read from stdin in Python?

import fileinput
for line in fileinput.input():
    pass
	
import sys
data = sys.stdin.readlines()
print "Counted", len(data), "lines."

name = input("Enter your name: ")   # Python 3


How do I sort a list of dictionaries by values of the dictionary in Python?

newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 
newlist = sorted(l, key=itemgetter('name'), reverse=True)

from operator import itemgetter
newlist = sorted(list_to_be_sorted, key=itemgetter('name')) 



How do I randomly select an item from a list using Python?

import random
foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))
	
For cryptographically secure random choices (e.g. for generating a passphrase from a wordlist), use random.SystemRandom class:
import random
foo = ['battery', 'correct', 'horse', 'staple']
secure_random = random.SystemRandom()
print(secure_random.choice(foo))
	
	
	
	
Replacements for switch statement in Python?
def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]
	
	

How to print without newline or space?
print('.', end='')




Why is “1000000000000000 in range(1000000000000001)” so fast in Python 3?
:-)



How to delete a file or folder?
os.remove() will remove a file.
os.rmdir() will remove an empty directory.
shutil.rmtree() will delete a directory and all its contents.




Calling a function of a module from a string with the function's name in Python

Assuming module foo with method bar:
import foo
method_to_call = getattr(foo, 'bar')
result = method_to_call()

As far as that goes, lines 2 and 3 can be compressed to:
result = getattr(foo, 'bar')()




How do you append to a file?
with open("test.txt", "a") as myfile:
    myfile.write("appended text")
	
	
	
	
Reverse a string in Python
>>> 'hello world'[::-1]
'dlrow olleh'



How to know if an object has an attribute in Python
if hasattr(a, 'property'): #a is class instance
    a.property
	
	
	
	
Find all files in a directory with extension .txt in Python

You can use glob:
import glob, os
os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)
	
or simply os.listdir:
import os
for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))
		
or if you want to traverse directory, use os.walk:
import os
for root, dirs, files in os.walk("/mydir"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))


			 
			 
			 
Create a dictionary with list comprehension in Python
d = dict((key, value) for (key, value) in iterable)
d = {key: value for (key, value) in iterable} #2.7 and older



How do I connect to a MySQL Database in Python?
#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb")        # name of the data base

try:
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time.
for x in range(0,numrows):
    row = cursor.fetchone()
    print row[0], "-->", row[1]
	
# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

finally:
db.close()



import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
	
	
	
	
Access environment variables from Python
import os
print os.environ['HOME']

Or you can see a list of all the environment variables using:
os.environ





How to remove an element from a list by index in Python?
In [9]: a = range(10)
In [10]: a
Out[10]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
In [11]: del a[-1]
In [12]: a
Out[12]: [0, 1, 2, 3, 4, 5, 6, 7, 8]




Random string generation with upper case letters and digits in Python
6U1S75
4Z4UKK
U911K4

''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
''.join(random.choices(string.ascii_uppercase + string.digits, k=N)) #3.6

>>> import string
>>> import random
>>> def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
...    return ''.join(random.choice(chars) for _ in range(size))
...
>>> id_generator()
'G5G74W'
>>> id_generator(3, "6793YUIO")
'Y3U'

>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.ascii_uppercase + string.digits
'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'




Nicest way to pad zeroes to string

Strings:
>>> n = '4'
>>> print n.zfill(3)
004

>>> print('{0:03d}'.format(4))  # python 3
004


Converting integer to string in Python?
>>> str(10)
'10'
>>> int('10')
10



How can I count the occurrences of a list item in Python?
>>> [1, 2, 3, 4, 1, 4, 1].count(1)
3


How to determine a variable's type?

>>> i = 123
>>> type(i)
<type 'int'>
>>> type(i) is int
True
>>> i = 123456789L
>>> type(i)
<type 'long'>
>>> type(i) is long
True
>>> i = 123.456
>>> type(i)
<type 'float'>
>>> type(i) is float
True



How to trim whitespace (including tabs)?

Whitespace on both sides:
s = "  \t a string example\t  "
s = s.strip()

Whitespace on the right side:
s = s.rstrip()

Whitespace on the left side:
s = s.lstrip()

s = s.strip(' \t\n\r')
This will strip any space, \t, \n, or \r characters

The examples above only remove strings from the left-hand and right-hand sides of strings. If you want to also remove characters from the middle of a string, try re.sub:

import re
print re.sub('[\s+]', '', s)
That should print out:

astringexample




Convert bytes to a Python string

>>> b"abcde"
b'abcde'

# utf-8 is used here because it is a very common encoding, but you
# need to use the encoding your data is actually in.
>>> b"abcde".decode("utf-8") 
'abcde'


bytes = [112, 52, 52]
"".join(map(chr, bytes))
>> p44



How to remove a key from a python dictionary?

if 'key' in myDict:
    del myDict['key']
	
Use dict.pop():

my_dict.pop('key', None)
This will return my_dict[key] if key exists in the dictionary, and None otherwise. If the second parameter is not specified (ie. my_dict.pop('key')) and key does not exist, a KeyError is raised.



Parsing values from a JSON file using Python?

{
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "valore"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}

import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

pprint(data)


data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]




Why does comparing strings in Python using either '==' or 'is' sometimes produce a different result?
is is identity testing, == is equality testing. what happens in your code would be emulated in the interpreter like this:

>>> a = 'pub'
>>> b = ''.join(['p', 'u', 'b'])
>>> a == b
True
>>> a is b
False



Extracting extension from filename in Python

>>> import os
>>> filename, file_extension = os.path.splitext('/path/to/somefile.ext')
>>> filename
'/path/to/somefile'
>>> file_extension
'.ext'



How do you change the size of figures drawn with matplotlib?
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')


Proper way to declare custom exceptions in modern Python?
class MyException(Exception):
    pass

raise MyException("My hovercraft is full of eels")




In Python, how do I determine if an object is iterable?

try:
    some_object_iterator = iter(some_object)
except TypeError, te:
    print some_object, 'is not iterable'
	
	
	
	
	
	
Why does Python code run faster in a function?

This runs faster

def main():
    for i in xrange(10**8):
        pass
main()

than

for i in xrange(10**8):
    pass
	
	
	
	
What's the difference between lists and tuples?

Apart from tuples being immutable there is also a semantic distinction that should guide their usage. Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order.




Most elegant way to check if the string is empty in Python?
if not myString:










