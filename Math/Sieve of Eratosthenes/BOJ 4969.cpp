#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main(){
    int nums[300001]={};
    fill(nums,nums+300001,0);
    for (int i=2;i<300000+1;i++){
        if (i%7==1 || i%7==6){
            nums[i]=1;
        }
    }
    for (int i=2;i<sqrt(300001)+1;i++){
        if (nums[i]){
            for (int j=2*i;j<300001;j+=i)
                nums[j]=0;
        }
    }
    while (1){
        int n;
        cin>>n;
        if (n==1) return 0;
        vector <int> answer={};
        for (int i = 2; i <= sqrt(n); ++i) {
            if (n % i == 0) {
                if (nums[i]) answer.push_back(i);
                if (i != n / i && nums[n / i]) answer.push_back(n / i); 
            }
        }
        if (nums[n]) answer.push_back(n);
        sort(answer.begin(),answer.end());
        cout<<n<<": ";
        for (int i=0;i<answer.size();i++){
            cout<<answer[i]<<" ";
        }
        cout<<"\n";
    }
}