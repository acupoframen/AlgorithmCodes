n=input()
for i in range(len(n)):
    if n[i]!=n[len(n)-i-1]:
        print(0)
        exit(0)
print(1)