#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

    int n;
    cin>>n;
    vector <int> data;
    int num;
    for (int i=0;i<n;i++){
        cin>>num;
        data.push_back(num);
    }    
    sort(data.begin(), data.end());
    for (int i=0; i<n;i++){
        cout<< data[i]<<" ";
    }
}