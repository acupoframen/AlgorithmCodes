s=input()
length=len(s)
if s==s[0]*length:
    print(-1)
elif s==s[::-1]:
    print(length-1)
else:
    print(length)