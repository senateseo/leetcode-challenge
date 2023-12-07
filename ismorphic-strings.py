class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hsm={}
        t_hsm={}
        
        for i in range(len(s)):
            if s[i] in s_hsm:
                if s_hsm[s[i]] != t[i]:
                    return False
            else:
                s_hsm[s[i]]=t[i]

            if t[i] in t_hsm:
                if t_hsm[t[i]] != s[i]:
                    return False
            else:
                t_hsm[t[i]]=s[i]
        return True

        
        # badc
        # baba


        # When Key is not found in Hashmap
        # - put key as s[i] and value as t[i]
        # TC: O(N)
        # SC: O(N)