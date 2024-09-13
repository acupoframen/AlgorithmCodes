#include <iostream>
#include <algorithm>
#include <string>

bool compare(char a, char b){
    return a>b;
}
using namespace std;
int main(){
    int num;
    cin>>num;
    string a=to_string(num);
    sort(a.begin(), a.end(),compare);
    cout<<a;
}