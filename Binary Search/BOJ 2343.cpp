#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    vector <int> nums;
    int temp;
    for (int i=0;i<n;i++){
        cin>>temp;
        nums.push_back(temp);
    }
    long long left=*max_element(nums.begin(),nums.end());

    long long right=100000*10000;
    while (left<=right){
        long long mid=(left+right)/2;
        temp=1;
        long long oneset=0;
        for (int i=0;i<n;i++){
            if (oneset+nums[i]<=mid){
                oneset+=nums[i];
            }
            else{
                oneset=nums[i];
                temp+=1;
            }
        }
        if (temp<=m){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
    }
    cout<<left;
}