#include <iostream>
using namespace std;

double dp[101];
int main(){
    int n, m;
    double a,b,c,d;
    cin>>n>>m;
    cin>>a>>b>>c>>d;
    dp[0]=m;
    for (int i=1;i<=n;i++){
        dp[i]=(1-dp[i-1])*b+dp[i-1]*d;
    }
    dp[n]*=1000;
    cout<<(int)(1000-dp[n])<<endl<<(int)dp[n];
}