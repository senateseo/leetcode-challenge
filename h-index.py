class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # Sort
        citations = sorted(citations)
        hIdx=0
        for i in range(len(citations)):
            hIdx=max(hIdx, min(len(citations)-i, citations[i]))
        return hIdx

# TC: O(nlogn)
# SC: O(1)
