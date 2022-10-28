""" This code is brute force method which works really fine for almost all cases but throws memory limit exceeded due to space issues for a large input"""
"""
import sys
def max_subarray(l):
    m = []
    max_sum = -sys.maxsize - 1
    if len(l)<=1:
        return sum(l)

    for i in range(0,len(l)):
        for j in range(1,len(l)+1):
            sum_val = sum(l[i:j])
            max_sum = sum_val if sum_val>max_sum else max_sum
            #m.append(l[i:j])
    return max_sum
    
    

  
    sum_arr = {sum(ele):ele for ele in m}
    #max_key = max(sum_arr)
    #return sum_arr[max_key]
    if 0 in l and 0==max(sum_arr):
        return 0
    else:
        sum_arr.pop(0)
        return sum_arr,max(sum_arr)
     """
def call_max_sum(c_sum,m_sum,nums):
    for i in nums:
            c_sum = c_sum + i
            if c_sum>=m_sum:
                m_sum = c_sum
            if c_sum<0:
                c_sum = 0
    return m_sum

def find_subarray(nums):
    c_sum = 0
    m_sum = 0
    if all(x<0 for x in nums):
        m_sum = nums[0]
        return call_max_sum(c_sum,m_sum,nums)
    else:
        return call_max_sum(c_sum,m_sum,nums)

def max_val(nums):
    for i in range(1, len(nums)):
        print(nums[i-1]+nums[i])
        nums[i] = max(nums[i-1] + nums[i], nums[i])
    return nums

nums = [-5,4,6,-3,4,-1]
#print(find_subarray(nums))
print(max_val(nums))