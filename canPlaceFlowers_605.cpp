class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int counter=0;
        int left=0;
        int right=0;
        for(int i=0;i<flowerbed.size()-1;++i){
            right = flowerbed[i+1];
            if((left+right+flowerbed[i])==0){
                counter+=1;
                left=1;
            }
            else
                left=flowerbed[i];
        }
        if(left+flowerbed[flowerbed.size()-1]==0)
            counter+=1;
    return counter>=n;
    }
};
