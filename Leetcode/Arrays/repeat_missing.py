from time import time


def repeat_missing(A):
    l=[]
    n  = len(A)

    #print(sum_val,cons_sum)
    for i in A:
        if i not in l:
            l.append(i)
        else:
            r = i

    sum_val = sum(l)
    cons_sum = (n)*(n+1)//2

    return r, cons_sum-sum_val

def repeat_m(A):
    n = len(A)
    x = sum(A) - sum(set(A))
    k = int(n*(n+1)/2) - sum(set(A))

    #print(k)
    return [x,k]

A = [3,2,1,3,5]
st = time()
print(repeat_m(A))
et = time()
tt = et-st
print(tt)