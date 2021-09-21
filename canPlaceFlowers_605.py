class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter=0
        left = 0
        for i in range(len(flowerbed)-1):
            right=flowerbed[i+1]
            if((left+right+flowerbed[i])==0): 
                counter+=1
                left=1
            else:
                left=flowerbed[i]
        if(left+flowerbed[len(flowerbed)-1]==0):
            counter+=1
        return counter>=n
