#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int main(){
    long long n,q;
    long long m;
    cin>>n>>m>>q;
    unordered_map <string,long long> stockprice;
    unordered_map <long long, vector<string>> stockgroup;
    unordered_map <string,long long> userstock;
    long long stocknumber;
    string stockname;
    long long price;
    while (n--){
        cin>>stocknumber>>stockname>>price;
        stockprice[stockname]=price;
        stockgroup[stocknumber].push_back(stockname);
    }
    long long option;
    string a;
    long long b;
    while (q--){
        cin>>option;
        if (option==1){
            cin>>a>>b;
            if (stockprice[a]*b>m)
                continue;
            else{
                m-=stockprice[a]*b;
                userstock[a]+=b;
            }
        }
        else if (option==2){
            cin>>a>>b;
            if (userstock[a]==0)
                continue;
            if (b>=userstock[a]){
                m+=stockprice[a]*userstock[a];
                userstock[a]=0;
            }
            else{
                m+=stockprice[a]*b;
                userstock[a]-=b;
            }
        }
        else if (option==3){
            cin>>a>>b;
            stockprice[a]+=b;
        }
        else if (option==4){
            long long num;
            cin>>num>>b;
            for (auto& i: stockgroup[num]){
                stockprice[i]+=b;
            }
        }
        else if (option==5){
            long long num;
            cin>>num>>b;
            for (auto& i: stockgroup[num]){
                stockprice[i]=stockprice[i]*(100+b)/100;
                stockprice[i]-=(stockprice[i])%10;
            }
        }
        else if (option==6){
            cout<<m<<endl;
        }
        else{
            long long temp=m;
            for (auto& i: userstock){
                temp+=stockprice[i.first]*i.second;
            }
            cout<<temp<<endl;
        }
    }
}