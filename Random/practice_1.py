'''
num = [1,0,-1,-4,0,5,9]

pos = round(len([index for (index , item) in enumerate(num) if item >0])/len(num),6)
neg = round(len([index for (index , item) in enumerate(num) if item <0])/len(num),6)
zero = round(len([index for (index , item) in enumerate(num) if item == 0])/len(num),6)

print(pos,neg,zero,sep='\n')
'''
'''
arr = [5,3,1,7,9]
arr.sort()
a1 = arr[:-1]
arr.sort(reverse=True)
a2 = arr[:-1]

print(sum(a1),sum(a2))
'''
'''
s = '12:01:00AM'

mer = s[-2:]

if (mer=='PM' and s[:2]!='12'):
    a = int(s[:2]) + 12
    print(str(a)+s[2:-2])
elif(mer=='AM' and s[:2]=='12'):
    b = '00'
    print(b+s[2:-2])
else:
    print(s[:-2])
'''

'''
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
'''
'''
arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
Lsum =0
Rsum =0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if i==j:
            Lsum+=arr[i][j]
        if i+j == len(arr)-1:
            Rsum+=arr[i][j]
print(abs(Lsum-Rsum))
'''
'''
arr = [63,54,17,78,43,70,32,97,16,94,
74,18,60,61,35,83,13,56,75,52,
70,12,24,37,17,0,16,64,34,81,
82,24,69,2,30,61,83,37,97,16,
70,53,0,61,12,17,97,67,33,30,
49,70,11,40,67,94,84,60,35,58,
19,81,16,14,68,46,42,81,75,87,
13,84,33,34,14,96,7,59,17,98,
79,47,71,75,8,27,73,66,64,12,
29,35,80,78,80,6,5,24,49,82]

m = len(arr)
c_arr = [0]*m
for i in range(0,len(arr)):
    c_arr[arr[i]]+=1
print(len(c_arr))
'''

'''
#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    es = ''
    for letter in s:
        w = ord(letter)
        if (64<w<91 or 96<w<123):
            if(letter.islower() and w+k >122):
                d = w+k-122
                while d>26:
                    d = d-26
                w = d + 96
                es+=chr(w)
            elif(letter.isupper() and w+k>90):
                d = w+k-90
                while d>26:
                    d = d-26
                w = d+ 64
                es+=chr(w)
            else:
                es+=chr(w+k)
        else:
            es+=chr(w)
    return es

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()


Better solution:

def caesarCipher(s, k):
    # Write your code here
    s1=""
    for i in range(len(s)):
        if('A'<=s[i]<='Z'):
            s1+=chr((ord(s[i])+k-ord('A'))%26+ord('A'))
        elif('a'<=s[i]<='z'):
            s1+=chr((ord(s[i])+k-ord('a'))%26+ord('a'))
        else:
            s1+=s[i]
    return s1

'''

def palindromeIndex(s):
    rev = s[::-1]
    len_s = len(s)
    if s == rev:
        return -1
    else:
        d = {i:s[0:i]+s[i+1:len_s] for i in range(len_s) if s[i]!=rev[i]}
        for k,v in d.items():
            if v == v[::-1]:
                return k
        if v!= v[::-1]:
            return -1
                
    


s = 'abab'
print(palindromeIndex(s))

'''
lst = []
def gridChallenge(grid):
    s =''
    for word in grid:
        for l in word:
            if ord(l)>96:
                lst.append(l)
        s1 = ''.join(sorted(lst))
        for i in range(0, len(s1), n):
            lst.append(s1[i:i+n])
           
    return lst

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
n=5
print(gridChallenge(grid))

'''