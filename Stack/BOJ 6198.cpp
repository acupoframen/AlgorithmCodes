#include <iostream>
#include <deque>

using namespace std;

int main(){
    int n;
    cin>>n;
    deque <int> s;
    long long answer=0;
    int num;
    for (int i=0;i<n;i++){
        cin>>num;
        if (s.empty()){
            s.push_back(num);
            continue;
        }
        while (!s.empty() && s.back()<=num){
            s.pop_back();
        }
        answer+=s.size();
        s.push_back(num);
    }
    cout<<answer;
}