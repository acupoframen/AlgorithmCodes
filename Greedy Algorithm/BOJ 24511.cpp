#include <iostream>
using namespace std;

long long data1[10001];
long long data2[10001];
long long temp1,temp2,total;
long long answer;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n,m,k;
    cin>>n>>m>>k;

    for (int i=1;i<=n;i++){
        cin>>data1[i];
        temp1+=data1[i];
    }
    for (int i=1;i<=m;i++){
        cin>>data2[i];
        temp2+=data2[i];
    }
    total=min(temp1,temp2);
    temp1=temp2=total;
    for (long long i=1;temp1>0;i++){
        if (data1[i]<temp1){
            answer+=i*data1[i];
            temp1-=data1[i];
        }
        else{
            answer+=i*temp1;
            temp1=0;
        }
    }
    for (long long i=1;temp2>0;i++){
        if (data2[i]<temp2){
            answer+=i*data2[i];
            temp2-=data2[i];
        }
        else{
            answer+=i*temp2;
            temp2=0;
        }
    }
    cout<<total<<' '<<answer;
}