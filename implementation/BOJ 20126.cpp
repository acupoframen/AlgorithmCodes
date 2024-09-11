#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n,m,s;
    cin>>n>>m>>s;
    vector<pair<int,int>> data;
    for (int i=0;i<n;i++){
        int x,y;
        cin>>x>>y;
        data.push_back({x,y});
    }
    sort(data.begin(),data.end());
    if (data[0].first>=m){
        cout<<0;
        return 0;
    }
    int temp=0;
    for (int i=0;i<n;i++){
        if (data[i].first-temp>=m){
            cout<<temp;
            return 0;
        }
        temp=data[i].first+data[i].second;

    }
    if (s-temp>=m){
        cout<<temp;
    }
    else
        cout<<-1;
    return 0;
}