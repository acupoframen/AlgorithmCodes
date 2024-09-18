#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin>>n;
    long long map [10001];
    long long temp;
    for (int i=0; i<n;i++){
        cin>>temp;
        map[i]=temp;
    }   
    long long answer=0;
    sort(map,map+n);
    if (n%2){
        answer=max(answer,map[n]);
        for (int i=0;i<n/2;i++){
            answer=max(answer,map[i]+map[n-2-i]);
        }
    }
    else{
        for (int i=0;i<n/2;i++){
            answer=max(answer,map[i]+map[n-1-i]);
        }
    }
    cout<<answer;
}