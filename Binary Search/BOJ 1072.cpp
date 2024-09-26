#include <iostream>
using namespace std;
int main(){
    long long x, y;
    cin>>x>>y;
    long long curr= (y*100)/x;
    if (curr>=99){
        cout<<-1; 
        return 0;
    }
    long long left=0,right=1000000000;
    while (left<=right){
        long long mid=(left+right)/2;
        long long temp=(y+mid)*100 / (x+mid);
        if (curr<temp)
            right=mid-1;
        else
            left=mid+1;
    }
    cout<<left;
    return 0;
}