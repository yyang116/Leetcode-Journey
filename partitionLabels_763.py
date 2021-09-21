class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return ''
        ranges=[]
        letters=set(x for x in s)
        for letter in letters:
            left = s.find(letter)
            right = s.rfind(letter)
            ranges.append([left, right])
        ranges.sort()
        [left,right] = ranges[0]
        result=[]

        for i in range(1,len(ranges)):
            if ranges[i][0]>right:
                result.append(right-left+1)
                [left,right] = ranges[i]
            else:
                right = max(right,ranges[i][1])

        result.append(right-left+1)
        return result
