class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        hsm={}

        for c in s:
            if c in hsm:
                hsm[c]+=1
            else:
                hsm[c]=1
        
        for c in t:
            if c not in hsm or hsm[c]==0:
                return False
            else:
                hsm[c]-=1
        
        return True