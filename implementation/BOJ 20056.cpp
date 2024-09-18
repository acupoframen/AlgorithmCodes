#include <iostream>
#include <vector>
using namespace std;
int dy[]={0,1,1,1,0,-1,-1,-1};
int dx[]={-1,-1,0,1,1,1,0,-1};
typedef struct fireball{
    int weight;
    int speed;
    int dir;
    fireball(int w, int s, int d){
        this->weight=w;
        this->speed=s;
        this->dir=d;
    }
}Fireball;

vector<vector<vector<struct fireball>>> map;

int move(int n, int m, int k){
    int mass=0;
    int order=k;
    while (order>0){
        order--;
        vector<vector<vector<Fireball>>> moved(n+1, vector<vector<Fireball>>(n+1));
        for (int i=1;i<=n;++i){
            for (int j=1;j<=n;++j){
                if (map[i][j].empty())
                    continue;
                for (int k=0; k<map[i][j].size();++k){
                    int m=map[i][j][k].weight;
                    int s=map[i][j][k].speed;
                    int d=map[i][j][k].dir;
                    int nx=i+dx[d]*(s%n);
                    if (nx<1)
                        nx+=n;
                    if (nx>n)
                        nx-=n;
                    int ny=j+dy[d]*(s%n);
                    if (ny<1)
                        ny+=n;
                    if (ny>n)
                        ny-=n;
                    moved[nx][ny].push_back(Fireball(m,s,d));
                }
            }
        }
        map.clear();
        map.assign(n+1,vector<vector<Fireball>>(n+1));
        for (int i=1; i<=n; ++i){
            for (int j=1; j<=n;++j){
                if (moved[i][j].empty())
                    continue;
                if (moved[i][j].size()==1){
                    map[i][j].push_back(Fireball(moved[i][j][0].weight,moved[i][j][0].speed,moved[i][j][0].dir));
                    if (order==0)
                        mass+=moved[i][j][0].weight;
                    continue;
                }
                int masssum=0;
                int speedsum=0;
                bool samedir=true;
                for (int k=0;k<moved[i][j].size();++k){
                    masssum+=moved[i][j][k].weight;
                    speedsum+=moved[i][j][k].speed;
                    if (k>0 && samedir){
                        if (moved[i][j][k-1].dir%2!=moved[i][j][k].dir%2)
                        samedir=false;
                    }
                }
                masssum=masssum/5;
                if( masssum==0)
                    continue;
                speedsum=speedsum/moved[i][j].size();
                int dirbase=-1;
                if (samedir) dirbase=0;
                else dirbase=1;
                for (int k=0;k<=6;k+=2){
                    map[i][j].push_back(Fireball(masssum,speedsum,dirbase+k));
                    if (order==0) mass+=masssum;
                }
            }
        }
    }
    return mass;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n,m,k;
    cin>>n>>m>>k;
    map.assign(n+1,vector<vector<Fireball>>(n+1));
    int r,c,m1,s,d;
    for (int i=0;i<m;++i){
        cin>>r>>c>>m1>>s>>d;
        map[r][c].push_back(Fireball(m1,s,d));
    }
    cout<<move(n,m,k);
    return 0;
}