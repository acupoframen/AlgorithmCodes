#include <iostream>
#include <cmath>
#include <limits.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[16]={0};
    arr[1]=2;
    for (int i=2;i<16;i++){
        arr[i]=arr[i-1]*2;
    }
    long long answer=pow((arr[n]+1),2);
    cout<<answer;
}