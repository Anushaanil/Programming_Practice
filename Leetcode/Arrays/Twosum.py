#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.

#Brute force -- O(n2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j]==target:
                    return [j,i]

# Using hashmap --- O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i, val in enumerate(nums):
            remaining = target - val

            if remaining in seen:
                return [i,seen[val]]
            seen[val] = i
            
        

            
        