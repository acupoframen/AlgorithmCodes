#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int data[101]={0,};
    int i,j,k;
    for (int temp=0;temp<m;temp++){
        cin>>i>>j>>k;
        for (int t=i-1;t<j;t++){
            data[t]=k;
        }
    }
    for (int i=0;i<n;i++){
        cout << data[i] << " ";
    }
    return 0;
}