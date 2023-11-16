class Solution:
    def candy(self, ratings: List[int]) -> int:
        mark=[0]*len(ratings)

        for i in range(len(ratings)):
            # If the number of candies was not decided
            if mark[i]==0:
                mark[i] = self.getMark(ratings, mark, i)
        return sum(mark)
    
    def getMark(self, ratings, mark, i):
        if len(ratings)==1:
            mark[i]=1
            return mark[i]
        
        if mark[i]!=0:
            return mark[i]
        if i==0:
            if ratings[i] <= ratings[i+1]:
                mark[i] = 1
                return mark[i]
            else:
                mark[i] = self.getMark(ratings, mark, i+1)+1
                return mark[i]
        if i==len(ratings)-1:
            if ratings[i] <= ratings[i-1]:
                mark[i] = 1
                return mark[i]
            else:
                mark[i] = self.getMark(ratings, mark, i-1)+1
                return mark[i]
                
        if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
            mark[i] = max(self.getMark(ratings, mark, i+1), self.getMark(ratings, mark, i-1))+1
        elif ratings[i] > ratings[i+1]:
            mark[i] = self.getMark(ratings, mark, i+1)+1
        elif ratings[i] > ratings[i-1]:
            mark[i] = self.getMark(ratings, mark, i-1)+1
        else:
            mark[i] = 1

        return mark[i]
            
    
        