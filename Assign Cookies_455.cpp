class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s);
};

int Solution::findContentChildren(vector<int>& g, vector<int>& s)
{
        int child=0;
        int cookie=0;
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        while(child<g.size()&&cookie<s.size()){  # made mistake here. <= was wrong. g[g.size()] is exceeding the length.
            if(g[child]<=s[cookie]) ++child;
            ++cookie;
        }
        return child;
    }
