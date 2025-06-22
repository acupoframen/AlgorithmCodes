n=input()
leng=len(n)
for i in range(leng//10+1):
    print(n[i*10:(i+1)*10])  