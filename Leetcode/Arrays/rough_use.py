def find_index(nums,target):
	start, end = 0, len(nums) - 1
		
	while start <= end:
		print(start,end)
		mid = start + (end-start) // 2
		#print(mid,(end-start) // 2)
		
		if nums[mid] == target:
			return mid
		
		elif nums[mid] >= nums[start]:
			if target <= nums[mid] and target >=nums[start]:
				end = mid - 1
			else:
				start = mid + 1
		else:
			if target >= nums[mid] and target <= nums[end]:
				start = mid + 1
			else:
				end = mid - 1
	return -1

#print(find_index([4,5,6,7,0,1,2],0))

class Solution:
    def call_max_sum(self,c_sum,m_sum,nums):
        for i in nums:
                c_sum = c_sum * i
                if c_sum>=m_sum:
                    m_sum = c_sum
                
        return m_sum
    
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]*nums[i],nums[i])
        return nums

s = Solution()
print(s.maxSubArray([2,-5,-2,-4,3]))