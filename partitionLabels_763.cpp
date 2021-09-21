class Solution {
public:
    vector<int> partitionLabels(string s) {
    int last[26];
    for(int i=0;i<s.size();++i){
        last[s[i]-'a']=i;
    }
    int start=0;
    int end=0;
    std::vector<int> partition;
    for(int i=0;i<s.size();++i){
        end=std::max(end,last[s[i]-'a']);
        if(end==i){
            partition.push_back(end-start+1);
            start=end+1;
        }
    }
    return partition;
    }
};
