class Solution:
    def isValid(self, s: str) -> bool:

        stk=[]

        for c in s:
            if c in ')]}':
                if not stk:
                    return False
                if c==')' and stk[-1]=='(':
                    stk.pop()
                elif c=='}' and stk[-1]=='{':
                    stk.pop()
                elif c==']' and stk[-1]=='[':
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return not stk

# TC: O(N)
# SC: O(N)