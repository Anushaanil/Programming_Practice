class Solution:
    def maxProduct(self, nums) -> int:
        ans = nums[0]
        temp = 1
        for num in nums:
            temp *= num
            ans = max(ans,temp)
            if temp == 0:
                temp = 1
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            temp *= nums[i]
            ans = max(ans,temp)
            if temp == 0:
                temp = 1
        return ans
s= Solution()
print(s.maxProduct([2,-5,-2,-4,3]))