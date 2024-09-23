#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(){
    map<string,bool> ma;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n,m;
    cin>>n>>m;
    for (int i=0;i<n;i++){
        string st;
        cin>>st;
        ma.insert({st,true});
    }
    int answer=0;
    for (int i=0;i<m;i++){
        string test;
        cin>>test;
        if (ma[test]==true) answer++;
    }
    cout<<answer;
}