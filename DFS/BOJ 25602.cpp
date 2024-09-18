#include <iostream>
#include <algorithm>
using namespace std;

int n,k;
int a[6];
int r[6][6];
int m[6][6];
int answer=0;
void dfs(int d, int first, int second){
    if (d>k){
        answer=max(answer,first+second);
        return;
    }
    for (int i=1;i<=n;i++){
        int newfirst=first;
        int newsecond=second;
        if (a[i]>0){
            a[i]--;
            newfirst+=r[d][i];
            for (int j=1;j<=n;j++){
                if (a[j]>0){
                    a[j]--;
                    newsecond+=m[d][j];
                    dfs(d+1,newfirst,newsecond);
                    newsecond-=m[d][j];
                    a[j]++;
                }
            }
            newfirst-=r[d][i];
            a[i]++;
        }
    }
}
int main(){
    cin>>n>>k;
    for (int i=1;i<=n;i++){
            cin>>a[i];
    }
    for (int i=1;i<=k;i++){
        for (int j=1;j<=n;j++){
            cin>>r[i][j];
        }
    }
    for (int i=1;i<=k;i++){
        for (int j=1;j<=n;j++){
            cin>>m[i][j];
        }
    }

    dfs(1,0,0);
    cout<<answer;
    return 0;
}
