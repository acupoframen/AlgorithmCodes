#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>  
#include <climits>

using namespace std;

int main() {
    int t;
    cin >> t; 
    int n;

    for (int i = 0; i < t; i++) {
        vector<int> map;
        int dp[501][501];
        memset(dp, 0, sizeof(dp));
        cin >> n;
        int temp;
        map.push_back(0);
        for (int j = 1; j <= n; j++) {
            cin >> temp;
            map.push_back(map[j - 1] + temp);
        }
        for (int len = 2; len <= n; len++) {
            for (int st = 1; st <= n + 1 - len; st++) {
                int end = st + len - 1;
                dp[st][end] =INT_MAX;
                for (int k = st; k < end; k++) {
                    dp[st][end] = min(dp[st][end], dp[st][k] + dp[k + 1][end] + map[end] - map[st - 1]);
                }
            }
        }
        cout << dp[1][n] << endl;
    }

    return 0;
}
