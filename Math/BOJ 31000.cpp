#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int answer=(2*n+1)*(2*n+1);
    //a==0 or a+b+c==1 
    //a=-1 -> b+c=2 or a=1 b+c=0 
    for (int a=-n;a<=n;a++){
        if (a==0)
            continue;
        for (int b=-n;b<=n;b++){
            int c=1-b-a;
            if (c>=-n && c<=n){
                answer++;
            }
        }
    }
    cout<<answer<<endl;
}