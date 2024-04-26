data=list(list(input().split()) for _ in range(15))
for i in range(15):
    for j in range(15):
        if data[i][j]=='w':
            print("chunbae")
            exit(0)
        elif data[i][j]=='b':
            print("nabi")
            exit(0)
        elif data[i][j]=='g':
            print("yeongcheol")
            exit(0)