#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<double> array1(n);
    for (int i=0;i<n;i++){
        cin>>array1[i];
    }
    sort(array1.begin(),array1.end());
    for (int i = 0; i < 7; ++i) {
        printf("%.3f\n", array1[i]);
    }
}
