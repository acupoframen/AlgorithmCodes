while True:
    try:
        s,t=input().strip().split()
        flag=0
        temp=0
        for char in t:
            if char==s[temp]:
                temp+=1
            if temp==len(s):
                flag=1
                break
        if flag:
            print("Yes")
        else:
            print("No")
    except:
        break