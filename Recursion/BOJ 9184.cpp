#include <iostream>
using namespace std;

int dp[21][21][21];
int f(int a,int b, int c){
    int temp;
    if  (a<=0 || b<=0 || c<=0){
        return 1;
    }
    else if (a>20 || b>20 || c >20){
        dp[20][20][20]=f(20,20,20);
        return dp[20][20][20];
    
    }
    else if (dp[a][b][c]!=0){
        return dp[a][b][c];}
    else{
        if (a<b && b<c){
            temp= f(a,b,c-1)+f(a,b-1,c-1)-f(a,b-1,c);
            dp[a][b][c]=temp;
            return temp;
        }
        else{
            temp= f(a-1,b,c)+f(a-1,b-1,c)+f(a-1,b,c-1)-f(a-1,b-1,c-1);
            dp[a][b][c]=temp;
            return temp;
        }
    }
}
int main(){
    while (true){
        int a,b,c;
        cin>>a>>b>>c;
        if (a==-1 && b==-1 && c==-1){
            break;
        }
        printf("w(%d, %d, %d) = %d\n", a,b,c,f(a,b,c));
    }
}