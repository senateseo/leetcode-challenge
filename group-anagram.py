class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsm={}
        gs=[]

        for s in strs:
            sorted_s = sorted(s)
            if str(sorted_s) in hsm:
                hsm[str(sorted_s)].append(s)
            else:
                hsm[str(sorted_s)]=[s]
        
        for key in hsm:
            gs.append(hsm[key])
        return gs

# TC : O(N)
# SC : O(N)