#include <iostream>
using namespace std;

int map[20][20];
bool check(int x, int y, int dx, int dy) {
    int color = map[x][y];
    if (color == 0) return false;
    for (int k = 1; k < 5; k++) {
        int nx = x + k * dx;
        int ny = y + k * dy;
        if (nx < 0 || nx >= 20 || ny < 0 || ny >= 20) 
            return false;
        if (map[nx][ny] != color) 
            return false;
    }

    if (x - dx >= 0 && x - dx < 20 && y - dy >= 0 && y - dy < 20) {
        if (map[x - dx][y - dy] == color) 
            return false;
    }
    if (x + 5 * dx >= 0 && x + 5 * dx < 20 && y + 5 * dy >= 0 && y + 5 * dy < 20) {
        if (map[x + 5 * dx][y + 5 * dy] == color) 
            return false;
    }

    cout << color << endl;
    cout << x << " " << y << endl;
    return true;
}

int main() {
    for (int i = 1; i < 20; i++) {
        for (int j = 1; j < 20; j++) {
            cin >> map[i][j];
        }
    }

    for (int i = 1; i <= 19; i++) {
        for (int j = 1; j <= 19; j++) {
            if (check(i, j, 0, 1)) return 0;   
            if (check(i, j, 1, 0)) return 0;   
            if (check(i, j, 1, 1)) return 0;  
            if (check(i, j, -1, 1)) return 0;  
        }
    }

    cout << 0;
    return 0;
}
