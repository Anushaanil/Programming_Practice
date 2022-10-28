# Python3 implementation


class pair:
	def __init__(self):
		self.min = 0
		self.max = 0

def find_min_max(l):
    p = pair()
    p.min = l[0]
    p.min = l[0]

    for ele in l:
        if ele<p.min:
            p.min=ele
        elif ele>p.max:
            p.max=ele
    return p.min,p.max
        

a = find_min_max([9,5,4,3,7])
print(a)


# This code contributed by phasing17
