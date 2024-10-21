#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int n;
    cin >> n;
    cin.ignore();  
    for (int i = 1; i <= n; i++){
        string a, b;
        int acount[26] = {0}; 
        int bcount[26] = {0};
        
        getline(cin, a);
        getline(cin, b);

        for (char ch : a) {
            acount[ch - 'a']++;
        }
        for (char ch : b) {
            bcount[ch - 'a']++;
        }

        int answer = 0;
        for (int j = 0; j < 26; j++) {
            answer += abs(acount[j] - bcount[j]);
        }

        cout << "Case #" << i << ": " << answer << "\n";
    }
    return 0;
}
