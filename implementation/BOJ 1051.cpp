#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    char data[51][51];

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> data[i][j];
        }
    }

    int maxSide = 1;

    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < m - 1; ++j) {
            for (int k = i + 1; k < n; ++k) {
                for (int a = j + 1; a < m; ++a) {
                    if (k - i == a - j) { 
                        if (data[i][j] == data[i][a] && data[i][j] == data[k][j] && data[i][j] == data[k][a]) {
                            maxSide = max(maxSide, k - i+1);
                        }
                    }
                }
            }
        }
    }
    cout << maxSide * maxSide << endl;

    return 0;
}
