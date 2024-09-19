#include <iostream>

using namespace std;
int main(){
    string name,grade;
    double howmany;
    double score;
    double realanswer;
    for (int i=0;i<20;i++){
        double answer=0;
        cin>>name>>score>>grade;
        if (grade=="P")
            continue;
        howmany+=score;
        if (grade=="F")
            continue;
        if (grade[0]=='A')
            answer+=4;
        else if (grade[0]=='B')
            answer+=3;
        else if (grade[0]=='C')
            answer+=2;
        else
            answer+=1;
        if (grade[1]=='+')
            answer+=0.5;
        realanswer+=answer*score;
    }
    cout<<realanswer/howmany;
    return 0;
}