data=list(input() for _ in range(3))
data.sort()
if data[0][0]=='k' and data[1][0]=='l'  and data[2][0]=='p':
    print("GLOBAL")
else:
    print("PONIX")