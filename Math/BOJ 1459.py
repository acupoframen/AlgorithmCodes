x,y,w,s=map(int,input().split())

if (x+y)%2==0:
    print(min((max(x,y))*s,(x+y)*w,(min(x,y)*s+(max(x,y)-min(x,y))*w)))
else:
    print(min((max(x,y)-1)*s+w,(x+y)*w,(min(x,y)*s+(max(x,y)-min(x,y)-1)*w)+w))

    