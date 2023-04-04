#include <iostream>
using namespace std;
int main(){
    int num;
    long long arr[101]={0,1,1,1,2,2};
    for (int i=6;i<101;i++){
        arr[i]=arr[i-5]+arr[i-1];
    }
    cin>>num;
    for (int i=num;i>0;i--){
        int n;
        cin>> n;
        cout<<arr[n]<<endl;
    }
    return 0;
}