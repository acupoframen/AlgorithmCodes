#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int gcd(int a, int b){
    while (b!=0){
        int temp=a%b;
        a=b;
        b=temp;
    }
    return a;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    int maxgcd=-1;
    int temp;
    string line;
    string num;
    vector <int> v;
    cin>>t;
    cin.ignore();
    while (t--){
        v.clear();
        maxgcd=-1;
        getline(cin,line);
        stringstream sstream(line);
        while (getline(sstream,num,' ')){
            v.push_back(stoi(num));
        }
        for (int i=0; i<v.size()-1;++i){
            for (int j=i+1;j<v.size();++j){
                temp=gcd(v[i],v[j]);
                maxgcd=maxgcd < temp ? temp: maxgcd;
            }
        }
        cout<<maxgcd<<" \n";
    }

}