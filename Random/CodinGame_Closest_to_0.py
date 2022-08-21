import sys
import math

l1 = []
l2 = []

try:
    n = int(input())
    m = input().split()
    [l1.append(int(x)) if int(x)>0 else l2.append(int(x)) for x in m ]
    
    if (len(l1)!=0) and (len(l2)!=0):
        if abs(min(l1))==abs(min(l2)):
            print(min(l1))

        elif(min(l1))<(0-min(l2)):
            print(min(l1))

        else:
            print(min(l2))    
       
    elif len(l2) == 0:
        print(min(l1))
    
    elif len(l1) == 0:
        print(max(l2))
      
except EOFError as e:
    print("0")
