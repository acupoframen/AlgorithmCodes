x,y,w,h=map(int,input().split())
print(min(x,y,abs(h-y),abs(w-x)))