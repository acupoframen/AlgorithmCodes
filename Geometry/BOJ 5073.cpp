#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    while (true){
        int data[3];
        int a,b,c;
        for (int i=0;i<3;i++)
            cin>>data[i];
        if (data[0]+data[1]+data[2]==0)
            break;
        else{
            sort(data,data+3);
            if (data[0]==data[1]&&data[1]==data[2])
                cout<<"Equilateral\n";
            else if (data[0]+data[1]<=data[2])
                cout<<"Invalid\n";
            else if (data[0]==data[1]||data[1]==data[2])
                cout<<"Isosceles\n";
            else
                cout<<"Scalene\n";
        }
    }
}