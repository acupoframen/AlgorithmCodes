#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    vector <int> data={};
    for (int i=0; i<m;i++){
        int temp;
        cin>>temp;
        data.push_back(temp);
    }
    int answer=data[0];
    answer=max(answer,n-data[m-1]);
    for (int i=1; i<m;i++){
        if ((data[i]-data[i-1])%2)
            answer=max(answer,(data[i]-data[i-1])/2+1);
        else
            answer=max(answer,(data[i]-data[i-1])/2);
    }
    cout<<answer;
}