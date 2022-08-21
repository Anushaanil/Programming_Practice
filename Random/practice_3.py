N, Q = input().split()
N,Q = int(N),int(Q)
S = input()
l = []
for i in range(Q):
    i1,i2 = input().split()
    i1,i2 = int(i1),int(i2)
    s1 = len(set(S[i1-1:i2]))
    s2 = len(S[i1-1:i2])
    l.append(s2-s1)

for j in l:
    print(j)



'''
N,Q = 8,2
S = 'abcdabcd'
l = []
for i in range(Q):
    i1,i2 = input().split()
    i1,i2 = int(i1),int(i2)
    print(S[i1-1:i2],set(S[i1-1:i2]))
'''