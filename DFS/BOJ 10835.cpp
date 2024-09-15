#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int leftdata[2001];
int rightdata[2001];
int dp[2001][2001];
int n;
int f(int i, int j){
    if (i>n || j>n)
        return 0;
    if (dp[i][j]!=-1) 
        return dp[i][j];
    dp[i][j]=max(f(i+1,j+1),f(i+1,j));
    if ( leftdata[i]>rightdata[j])
        dp[i][j]=max(dp[i][j],f(i,j+1)+rightdata[j]);
    return dp[i][j];
}

int main(int argc, char** argv){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    memset(dp,-1,sizeof(dp));
    cin>>n;
    for (int i=1; i<=n;i++) cin>>leftdata[i];
    for (int i=1; i<=n;i++) cin>>rightdata[i];
    cout<<f(1,1);
    return 0;
}