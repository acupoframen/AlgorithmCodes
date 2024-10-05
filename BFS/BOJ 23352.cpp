#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
int r,c;
int map[51][51];
int dist[51][51];
int dx[4]={0,0,-1,1};
int dy[4]={-1,1,0,0};
int answer=0;
int temp=0;
queue <pair<int,int>> q;

void bfs(int orix,int oriy){
    memset(dist,0,sizeof(dist));
    q.push(make_pair(orix,oriy));
    dist[orix][oriy]=1;
    while (q.size()>=1){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();
        if (dist[x][y]>temp){
            temp=dist[x][y];
            answer=map[x][y]+map[orix][oriy];
        }
        else if (dist[x][y]==temp){
            answer=max(answer,map[x][y]+map[orix][oriy]);
        }
        for (int i=0;i<4;i++){
            int nx=x+dx[i];
            int ny=y+dy[i];
            if (0<=nx&&nx<r&&0<=ny&&ny<c){
                if (!map[nx][ny] || dist[nx][ny])
                    continue;
                dist[nx][ny]=dist[x][y]+1;
                q.push(make_pair(nx,ny));
            }
        }

    }
}
int main(){
    cin>>r>>c;
    for (int i=0;i<r;i++){
        for (int j=0;j<c;j++){
            cin>>map[i][j];
        }
    }
    for (int i=0;i<r;i++){
        for (int j=0;j<c;j++){
            if (map[i][j]) bfs(i,j);
        }
    }

    cout<<answer;
}