#Find the number of odds between a range of numbers
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low
        low_mod = low%2
        high_mod = high%2
        
        if low_mod==0 and high_mod==0:
            return diff//2
        elif (low_mod==0 and high_mod!=0) or (low_mod!=0 and high_mod==0):
            return (diff+1)//2
        elif low_mod!=0 and high_mod!=0:
            return (diff//2)+1
       
s = Solution()
print(s.countOdds(111,116))
