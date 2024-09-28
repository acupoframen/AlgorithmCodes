#include <iostream>
using namespace std;

int main(){
    string s;
    cin>>s;
    int data[26]={0,};
    for (int i=0; i<s.size();i++){
        data[s[i]-'A']+=1;
    }
    int cnt=0;
    int odd=0;
    for (int i=0;i<26;i++){
        if (data[i]%2){
            cnt++;
            odd=i;
        }
    }
    if (cnt>1){
        cout<<"I'm Sorry Hansoo";
        return 0;
    }
    string answer;
    for (int i=0;i<26;i++){
        for (int j=0;j<data[i]/2;j++){
            answer+='A'+i;
        }
    }
    if (cnt)
        answer+='A'+odd;
    for (int i=25;i>=0;i--){
        for (int j=0;j<data[i]/2;j++)
        answer+='A'+i;
    }
    cout<<answer;
    return 0;

}