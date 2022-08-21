'''
# Python implementation of program
from math import sqrt


# Function to calculate gcd of two numbers
def gcd(a, b):
	
	if a == 0:
		return b
	return gcd(b % a, a)

# Function to calculate all common divisors
# of two given numbers
# a, b --> input integer numbers
def commDiv(a, b):
	
	# find GCD of a, b
	n = gcd(a, b)
	# Count divisors of n
	result = 0
	for i in range(1,int(sqrt(n))+1):
		if n % i == 0:
			if n/i == i:
				result += 1  
			else:
				result += 2
				
	return result, int(sqrt(n))

# Driver program to run the case
if __name__ == "__main__":
	a = 9
	b = 18
	print(commDiv(a, b))

'''
'''
l =[]
T = int(input())
for i in range(T):
    w,i1,i2 = input().split()
    i1=int(i1)
    i2=int(i2)
    s = w[:i1]
    s += ''.join(sorted(w[i1:i2+1],reverse=True))
    s+= w[i2+1:]
    l.append(s)
for i in l:
    print(i)
'''

'''
T = int(input())
l1 = []
for i in range(T):
    n,k= input().split()
    n = int(n)
    l= list(range(n))
    k=int(k)
    a = input().split()
    for j in range(n):
        ind = (j+k)%n
        l[ind] = a[j]
    l1.append(l)

for i in l1:
    print(' '.join(map(str,i)))
    
'''
def NewYear(q):
    l=[]
    initial = q.copy()
    initial.sort()
    d = {initial[i]:q[i] for i in range(len(initial))}
    for k,v in d.items():
        diff = abs(k-v)
        if diff>2:
            return "Too chaotic"
        l.append(diff)
    return sum(l)//2

q = [2,5,1,3,4]
print(NewYear(q))