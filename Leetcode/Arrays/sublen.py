class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        l = []
        #[l.append(ele) for ele in s if ele not in l]
        #new_sub = ''.join(l)
       
        for i in range(len(s)):
            #print(s[i:len(s)])
            #[l.append(ele) for ele in s[i:len(s)] if ele not in l]
            #new_sub = ''.join(l)
            #print(new_sub)
            if s[i:len(s)] in s and len(set(s[i:len(s)]))==len(s[i:len(s)]):
                return len(s[i:len(s)])

S  = Solution()
print(S.lengthOfLongestSubstring('bbbb'))
            