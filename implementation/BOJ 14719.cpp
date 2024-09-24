#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;
int f(int left, int right, int* data){
    int ret=0;
    for (int i=left;i<=right;i++){
        ret=max(data[i],ret);
    }
    return ret;
}
int main(){
    int h,w;
    int data[501];
    cin>>h>>w;
    for (int i=0; i<w; i++) cin>>data[i];
    int answer=0;
    for (int i=1; i<w-1;i++){
        int k=min(f(0,i-1,data),f(i+1,w-1,data));
        if (data[i]<k) answer+=k-data[i];
    }
    cout<<answer;
    return 0;
}