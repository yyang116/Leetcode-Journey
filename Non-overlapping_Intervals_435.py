class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[1])
        end=intervals[0][1]
        ans=1
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]>=end:
                ans+=1
                end=intervals[i][1]    
        return n-ans
