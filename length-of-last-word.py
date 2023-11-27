class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s=s.split(' ')
        
        lastIdx=0
        for i in range(len(s)):
            if s[i]!='':
                lastIdx=i
        
        return len(s[lastIdx])

# TC: O(N)
# SC: O(1)