#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){

    int n;
    cin>>n;
    vector <pair<int,int>> map={};
    for (int i=0;i<n;i++){
        int temp,dur;
        cin>>temp>>dur;
        map.push_back({temp,dur});
    }
    sort(map.begin(),map.end());
    int answer=0;
    for (int i=0;i<n;i++){
        if (answer<=map[i].first){
            answer=map[i].second+map[i].first;
        }
        else{
            answer+=map[i].second;
        }

    }
    cout<<answer;
}
