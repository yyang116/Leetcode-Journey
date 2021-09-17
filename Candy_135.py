class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=len(ratings)
        if(l<2): return l
        candy=[1 for x in range(l)]
        for i in range(l-1):
            if(ratings[i]<ratings[i+1]): 
                candy[i+1]=candy[i]+1
        for i in range(1,l):
            if(ratings[l-i-1]>ratings[l-i] and candy[l-i-1]<=candy[l-i]): 
                candy[l-i-1]=candy[l-i]+1
        return sum(candy)
