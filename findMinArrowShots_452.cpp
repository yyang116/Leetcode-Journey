class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if(points.empty()) return 0;
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b){return a[1] < b[1];});
        int counter=1;
        int right=points[0][1];
        for(int i=0;i<points.size();++i){
            if(points[i][0]>right){
                counter++;
                right=points[i][1];
            }
        }
        return counter;
    }
};
