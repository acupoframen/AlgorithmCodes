#include <iostream>
#include <stack>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin>>n;
    int cmd, num;
    stack <int> s;

    while (n--){
        cin>>cmd;
        if (cmd==1){
            cin>>num;
            s.push(num);
        }
        else if (cmd==2){
            if (s.empty()){
                cout<<"-1\n";
            }
            else{
                cout<< s.top()<<"\n";
                s.pop();
            }
        }
        else if (cmd ==3){
            cout << (int)s.size()<<"\n";
        }
        else if (cmd == 4){
            if (s.empty()){
                cout<<"1\n";
            }
            else{
                cout<<"0\n";
            }
        }
        else{
            if (s.empty()){
                cout<<"-1\n";
            }
            else{
                cout<<s.top()<<"\n";
            }
        }
    }
    return 0;
}