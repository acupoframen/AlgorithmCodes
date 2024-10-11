#include <iostream>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <cmath>
using namespace std;

int map[500001];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n,a,b;
    cin>>n>>a>>b;
    int answer=-1;
    queue <pair<int,int>> q;
    q.push({a,0});
    q.push({b,0});
    while (!q.empty()){
        int loc=q.front().first;
        int day=q.front().second;
        q.pop();
        int dist=pow(2,day);
        int next=loc+dist;
        if (next<=n){
            if (map[next]==day+1){
                answer=day+1;
                break;
            }
            else{
                map[next]=day+1;
                q.push({next,day+1});
            }
        }
        next=loc-dist;
        if (next>0){
            if (map[next]==day+1){
                answer=day+1;
                break;
            }
            else{
                map[next]=day+1;
                q.push({next,day+1});
            }
        }
    }
    cout<<answer;
    return 0;


}