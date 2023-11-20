class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        if len(s) != len(pattern):
            return False
        
        p_map={}
        s_map={}

        for i in range(len(pattern)):
            if pattern[i] not in p_map:
                p_map[pattern[i]]=s[i]
            else:
                if p_map[pattern[i]] != s[i]:
                    return False
            
            if s[i] not in s_map:
                s_map[s[i]] = pattern[i]
            else:
                if s_map[s[i]]!=pattern[i]:
                    return False
        
        return True