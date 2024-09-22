#include <iostream>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    long long answer=1;
    n-=1;
    m-=1;
    for (int i = 0; i < m; i++) {
        answer *= (n - i);
        answer /= (i + 1);
    }
    cout<<answer;
    return 0;

}