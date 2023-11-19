class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hsm={}

        for letter in magazine:
            if letter in hsm:
                hsm[letter]+=1
            else:
                hsm[letter]=1
        
        for letter in ransomNote:
            if letter not in hsm:
                return False
            elif hsm[letter]==0:
                return False
            else:
                hsm[letter]-=1
        
        return True
            