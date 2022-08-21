'''
# Problem 2 - Code Monk

Monk and Inversions

find out the number of inversion in the matrix M. 
Number of inversions, in a matrix is defined as the number of unordered pairs of cells {(i,j),(p,q)}
such that M[i][j]>M[p][q] & i<=p,j<=q.

t = int(input())
while(t!=0):
    n = int(input())
    arr = []
    
    for i in range(n):
        arr.append(list(map(int,input().split())))

    c = 0
    for i in range(n):
        for j in range(n):
            for k in range(i,n):
                for l in range(j,n):
                    if(arr[i][j]>arr[k][l]):
                        c+=1
    print(c)
    t-=1

'''
'''
def cycle(a,n,k,c):
    m = 0
    for i in range(n):
        if (int(a[i:]+a[:i],2) > m):
            m = int(a[i:]+a[:i],2)
        c+=1
    k-=1
    if k!=0:
        return cycle(bin(m)[2:],n,k,c)
    else:
        return c

t = int(input())
while t!=0:
    n,k = list(map(int,input().split()))
    a = input()
    c=-1
    m = cycle(a,n,k,c)
    print(m)
    t-=1

'''
'''
Function which takes indefinite amount of lists and returns concatenated list

def foo(*args):
    lst = []
    for eachlist in args:
        lst = lst + eachlist
    return lst

Function which takes indefinite amount of lists and returns True if there are no empty elements inside else false

def foo(*args):
    return all(args)
'''
'''
print all numbers from 0 to 10 in increment of 0.1

for i in [i/10 for i in range(0,101)]:
    print(i)
'''
'''
def foo(number):
    return dict(sign = "positive" if number > 0 else
        ("negative" if number < 0 else "zero"),
        parity = "odd" if number % 2 == 1 else 
        ("even" if number % 2 == 0 else "non integer"))
'''
'''
def foo(lst):
    l = []
    ind = list(range(0,len(lst),7))
    for i in ind:
        l.extend(lst[i:i+5])
    return l

OR

import itertools

def foo(mylist,x,y):
    list_of_lists = [mylist[i:i+x] for i in range(0, len(mylist),y)]
    return list(itertools.chain.from_iterable(list_of_lists))

print(foo(['mon','tue','wed','thur','fri','sat','sun','mon','tue','wed','thur','fri','sat','sun','mon','tue','wed','thur','fri','sat','sun']))

'''
'''
import random

def foo():
    return [random.randint(1,10) for i in range(1000)]
print(foo())

'''
'''
def foo(lst):
    return [i for i in lst if type(i)==str and "xxx" in i]

'''
'''
def foo(d):
    return dict((k,v) for k,v in d.items() if v>4)
'''
'''
vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!"
}

def foo(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]

'''
'''
import datetime
import difflib


vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

def foo(query, vocabulary):
    new_vocab = {k:[v,difflib.SequenceMatcher(None,query,k).ratio()] 
    for (k,v) in vocabulary.items()}
    return new_vocab[max(new_vocab,key=lambda x: new_vocab[x][1])][0]

print(foo('tell me the time',vocabulary))
'''
'''
from datetime import datetime
import calendar

def foo(date):
    day_num = datetime.strptime(date,'%Y-%m-%d').weekday()      # or datetime.strptime(date,'%Y-%m-%d').strftime('%A')
    return calendar.day_name[day_num]

print(foo('2022-05-03'))

'''
'''
Create 9 empty files with names file1.txt,file2.txt etc. Do not overwrite them if exists already!
for i in range(1,10):
    open('file{}.txt'.format(i),'a').close()

'''
'''
import re
import glob 

files = glob.glob('*.txt')
l = []
m = []
for fname in files:
    f = open(fname,'r')
    l.append(f.read())

for val in l:
    m.extend(re.findall("[0-9]+\.*[0-9]*",val))   # re for any type of values '[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?'

val = [float(i) for i in m] 
print(sum(val)/len(val))

'''

'''
create empty folders in cur directory

import os

for i in range(1,51):
    path = os.getcwd()+'/'+str(i)

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    
To create subfolders 
--------------------

import os
for i in range(1,51):
    os.makedirs(str(i))
    for f in ['mon','tue','wed','thu','fri']:
        os.makedirs(str(i)+'/'+str(f))

To delete a file in directory
-----------------------------
import os 
import glob

files = glob.glob('*.txt')
for f in files:
    os.remove(f)


To delete all the files with 'xxx' or 'XXX' string in them
----------------------------------------------------------
import os 
import glob

files = glob.glob('*.txt')
for file in files:
    with open(file,'r') as f:
        content = f.read()
        if 'xxx' in content or 'XXX' in content:
            os.remove(file)

'''
'''
Print filename with minimum size
--------------------------------

import os 
import glob
l = []
files = glob.glob('*.txt')


for file in files:
    l.append((os.path.getsize(file),file))

m = min(l)
print(m[1])

sizes = {file: os.path.getsize(file) for file in files}

#print(sizes.get('file2.txt'))
print(min(sizes,key=sizes.get))

'''
'''
Read text file and append a new dictionary to file 
--------------------------------------------------
import json

with open('file2.txt','r') as json_file:
    data = json.load(json_file)

data['metals']['gold'] = {

         "conductivity": 33.5, 

         "density": 0.255, 

         "heat": 0.129, 

         "melting point": 2171, 

         "thermal expansion": 4.7, 

         "yield strength": 288, 

         "tensile strength": 441, 

         "minimum impact energy": 22

     }

with open('file2.txt','w') as file:
    json.dump(data,file,indent=4)


Rename a file 
-------------

import os
os.rename(filename)


Facts about CPython 
-------------------

Python itself is a language. A language is a set of rules. 
These rules should be interpreted by a software that understands that language. 
This software is usually called an "implementation".
There are many implementations of Python, but the main one is CPython. 
CPython is written in C language. In fact, the software you download from python.org is CPython 
and CPython has been programmed to understand Python language.

Builtin -- A code feature i.e built inside the CPython software, and not in an external.py file 
so it's not only a library also includes features,classes,functions etc.

Variables are just names referring to objects. Even though we delete variable x, 
the object (i.e. 1) is still in memory and it is referred by name y now. So, print(y) prints 1.

x = 1
y = x
del x
print(y) #output 1
'''
import re
with open('file2.txt','r') as f:
    content = f.read()

r  = re.findall("[A-Z][a-z ',]*\?",content)

print(r)